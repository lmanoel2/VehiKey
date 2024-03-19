import cv2
class ImageConvertUtils:
    @staticmethod
    def SetImageToGray(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def SetImageToRgb(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @staticmethod
    def ApplyThreshold(image):
        _, thresh = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY_INV)
        return thresh