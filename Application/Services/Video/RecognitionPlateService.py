import cv2

from Domain.Interfaces.Services.Video.IRecognitionPlateService import IRecognitionPlateService
from Application.Utils.Images.ImageConvertUtils import ImageConvertUtils
from ultralytics import YOLO
import easyocr
import os


class RecognitionPlateService(IRecognitionPlateService):
    __dictCharToInt = {'O': '0',
                       'I': '1',
                       'J': '3',
                       'A': '4',
                       'G': '6',
                       'S': '5'}

    __dictIntToChar = {'0': 'O',
                       '1': 'I',
                       '3': 'J',
                       '4': 'A',
                       '6': 'G',
                       '5': 'S'}

    def GetTextPlateFromImage(self, carImage):
        carImage = ImageConvertUtils.SetImageToRgb(carImage)
        plates = self.__GetLicensePlates(carImage)

        for plate in plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = plate
            x1 = int(round(x1))
            y1 = int(round(y1))
            x2 = int(round(x2))
            y2 = int(round(y2))

            licensePlateCrop = carImage[y1:y2, x1:x2, :]
            licensePlateCrop = ImageConvertUtils.SetImageToGray(licensePlateCrop)
            #cv2.imshow('2', licensePlateCrop)
            licensePlateCrop = ImageConvertUtils.ApplyThreshold(licensePlateCrop, 100)
            #cv2.imshow('3', licensePlateCrop)
            licensePlateText, licensePlateScore = self.__ReadLicensePlate(self, licensePlateCrop)
            #cv2.waitKey(1)
            return licensePlateText, licensePlateScore

        return None, None

    @staticmethod
    def __GetLicensePlates(carImage):
        parentDirectoryTest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        directoryModelYolo = os.path.join(parentDirectoryTest, 'Utils', 'Files', 'Models', 'license_plate_detector.pt')
        modelLicensePlate = YOLO(directoryModelYolo)

        return modelLicensePlate(carImage)[0]

    @staticmethod
    def __ReadLicensePlate(self, license_plate_crop):
        reader = easyocr.Reader(['pt'], gpu=True)
        license_plate_crop = ImageConvertUtils.ApplyThresholdInv(license_plate_crop, 0)
        detections = reader.readtext(license_plate_crop)

        # cv2.imshow('letter', license_plate_crop)
        # cv2.waitKey(1)

        for detection in detections:
            bbox, text, score = detection

            x1 = int(round(bbox[0][0]))
            y1 = int(round(bbox[0][1]))
            x2 = int(round(bbox[1][0]))
            y2 = int(round(bbox[1][1]))
            x3 = int(round(bbox[2][0]))
            y3 = int(round(bbox[2][1]))
            x4 = int(round(bbox[3][0]))
            y4 = int(round(bbox[3][1]))
            x_min = min(x1, x2, x3, x4)
            y_min = min(y1, y2, y3, y4) + 12
            x_max = max(x1, x2, x3, x4)
            y_max = max(y1, y2, y3, y4)

            license_plate_crop_improved = license_plate_crop[y_min:y_max, x_min:x_max]
            license_plate_crop_improved = ImageConvertUtils.ApplyThresholdInv(license_plate_crop_improved, 0)

            detections_improved = reader.readtext(license_plate_crop_improved)
            for detection_improved in detections_improved:
                bbox_improved, text_improved, score_improved = detection_improved
                text_improved = text_improved.upper().replace(' ', '')

                if self.__LicenseCompliesFormat(text_improved):
                    return self.__FormatLicense(self, text_improved), score_improved

        return None, None

    @staticmethod
    def __LicenseCompliesFormat(text):
        if len(text) != 7 and len(text) != 8:
            return False

        return True

    @staticmethod
    def __FormatLicense(self, text):
        containsHyphen = '-' in text
        if containsHyphen:
            return self.__FormatOldPlate(self, text)
        else:
            return self.__FormatNewPlate(self, text)

    @staticmethod
    def __FormatOldPlate(self, text):
        mapping = {0: self.__dictIntToChar, 1: self.__dictIntToChar, 2: self.__dictIntToChar,
                   4: self.__dictCharToInt, 5: self.__dictCharToInt, 6: self.__dictCharToInt, 7: self.__dictCharToInt}

        positionsPlateValid = [0, 1, 2, 4, 5, 6, 7]

        return self.__MapingLicensePlate(text, mapping, positionsPlateValid)

    @staticmethod
    def __FormatNewPlate(self, text):
        mapping = {0: self.__dictIntToChar, 1: self.__dictIntToChar, 2: self.__dictIntToChar, 3: self.__dictCharToInt,
                   4: self.__dictIntToChar, 5: self.__dictCharToInt, 6: self.__dictCharToInt, }

        positionsPlateValid = [0, 1, 2, 3, 4, 5, 6]

        return self.__MapingLicensePlate(text, mapping, positionsPlateValid)

    @staticmethod
    def __MapingLicensePlate(text, mapping, positionsPlateValid):
        license_plate = ''

        for j in positionsPlateValid:
            if text[j] in mapping[j].keys():
                license_plate += mapping[j][text[j]]
            else:
                license_plate += text[j]

        return license_plate
