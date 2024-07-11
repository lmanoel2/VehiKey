import cv2
from PIL import Image


class ColorService:
    def GetColorFromImage(self, image):
        rgb = self.__AverageImageColor(image)
        my_color = (rgb[0], rgb[1], rgb[2])
        color_name = self.__GetColorName(my_color)
        if color_name in self.__silver_colors:
            return "Silver"
        elif color_name in self.__blue_colors:
            return "Blue"
        elif color_name in self.__black_colors:
            return "Black"
        elif color_name in self.__cyan_colors:
            return "Cyan"
        elif color_name in self.__green_colors:
            return "Green"
        elif color_name in self.__brown_colors:
            return "Brown"
        elif color_name in self.__purple_colors:
            return "Purple"
        elif color_name in self.__pink_colors:
            return "Pink"
        elif color_name in self.__red_colors:
            return "Red"
        elif color_name in self.__orange_colors:
            return "Orange"
        elif color_name in self.__yellow_colors:
            return "Yellow"
        else:
            return color_name

    def __GetColorName(self, color) -> str:
        """ guess color name using the closest match from KNOWN_COLORS """
        differences = [
            [self.__ColorDifference(color, known_color), known_name]
            for known_name, known_color in self.__know_colors.items()
        ]
        differences.sort()  # sorted by the first element of inner lists
        return differences[0][1]  # the second element is the name

    def __ColorDifference(self, color1, color2) -> int:
        """ calculate the difference between two colors as sum of per-channel differences """
        return sum([abs(component1 - component2) for component1, component2 in zip(color1, color2)])

    def __AverageImageColor(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)

        h = image_pil.histogram()

        # split into red, green, blue
        r = h[0:256]
        g = h[256:256 * 2]
        b = h[256 * 2: 256 * 3]

        # perform the weighted average of each channel:
        # the *index* is the channel value, and the *value* is its weight
        return (
            sum(i * w for i, w in enumerate(r)) / sum(r),
            sum(i * w for i, w in enumerate(g)) / sum(g),
            sum(i * w for i, w in enumerate(b)) / sum(b)
        )

    __black_colors = ["Black", "grey11", "grey21", "grey31"]
    __silver_colors = ["DimGray", "DarkGray", "Silver", "LightGrey", "Gainsboro", "SlateGray", "LightSlateGray"]
    __blue_colors = [
        "SlateBlue", "SlateBlue1", "SlateBlue3", "DarkSlateBlue", "MidnightBlue",
        "Navy", "DarkBlue", "MediumBlue", "Blue", "CornflowerBlue", "RoyalBlue",
        "DodgerBlue", "DeepSkyBlue", "LightSkyBlue", "SkyBlue", "LightBlue",
        "SteelBlue", "LightSteelBlue"
    ]
    __cyan_colors = [
        "Cyan", "DarkTurquoise", "Turquoise", "MediumTurquoise", "LightSeaGreen",
        "DarkCyan", "Teal", "Aquamarine", "MediumAquamarine", "CadetBlue"
    ]
    __green_colors = [
        "DarkSlateGray", "MediumSpringGreen", "SpringGreen", "PaleGreen", "LightGreen",
        "DarkSeaGreen", "MediumSeaGreen", "SeaGreen", "DarkGreen", "Green",
        "ForestGreen", "LimeGreen", "Lime", "LawnGreen", "Chartreuse",
        "GreenYellow", "YellowGreen", "OliveDrab", "DarkOliveGreen", "Olive"
    ]
    __brown_colors = [
        "DarkKhaki", "Goldenrod", "DarkGoldenrod", "SaddleBrown", "Sienna",
        "RosyBrown", "Peru", "Chocolate", "SandyBrown", "NavajoWhite",
        "Wheat", "BurlyWood", "Tan"
    ]
    __purple_colors = [
        "MediumSlateBlue", "MediumPurple", "BlueViolet", "Indigo", "DarkViolet",
        "DarkOrchid", "MediumOrchid", "Purple", "DarkMagenta", "Magenta",
        "Fuchsia", "Violet", "Orchid", "Plum"
    ]
    __pink_colors = [
        "MediumVioletRed", "DeepPink", "HotPink", "PaleVioletRed", "LightPink",
        "Pink", "LightCoral", "IndianRed", "Crimson"
    ]
    __red_colors = [
        "Maroon", "DarkRed", "FireBrick", "Brown", "Salmon",
        "DarkSalmon", "LightSalmon", "Coral", "Tomato", "Red"
    ]
    __orange_colors = [
        "OrangeRed", "DarkOrange", "Orange"
    ]
    __yellow_colors = [
        "Gold", "Yellow", "Khaki"
    ]

    __know_colors = {
        "Black": (0, 0, 0),
        "grey11": (28, 28, 28),
        "grey21": (54, 54, 54),
        "grey31": (79, 79, 79),

        "DimGray": (105, 105, 105),
        "DarkGray": (169, 169, 169),
        "Silver": (192, 192, 192),
        "LightGrey": (211, 211, 211),
        "Gainsboro": (220, 220, 220),

        "SlateBlue": (106, 90, 205),
        "SlateBlue1": (131, 111, 255),
        "SlateBlue3": (105, 89, 205),
        "DarkSlateBlue": (72, 61, 139),
        "MidnightBlue": (25, 25, 112),
        "Navy": (0, 0, 128),
        "DarkBlue": (0, 0, 139),
        "MediumBlue": (0, 0, 205),
        "Blue": (0, 0, 255),
        "CornflowerBlue": (100, 149, 237),
        "RoyalBlue": (65, 105, 225),
        "DodgerBlue": (30, 144, 255),
        "DeepSkyBlue": (0, 191, 255),
        "LightSkyBlue": (135, 206, 250),
        "SkyBlue": (135, 206, 235),
        "LightBlue": (173, 216, 230),
        "SteelBlue": (70, 130, 180),
        "LightSteelBlue": (176, 196, 222),
        "SlateGray": (112, 128, 144),
        "LightSlateGray": (119, 136, 153),

        "Cyan": (0, 255, 255),
        "DarkTurquoise": (0, 206, 209),
        "Turquoise": (64, 224, 208),
        "MediumTurquoise": (72, 209, 204),
        "LightSeaGreen": (32, 178, 170),
        "DarkCyan": (0, 139, 139),
        "Teal": (0, 128, 128),
        "Aquamarine": (127, 255, 212),
        "MediumAquamarine": (102, 205, 170),
        "CadetBlue": (95, 158, 160),

        "DarkSlateGray": (47, 79, 79),
        "MediumSpringGreen": (0, 250, 154),
        "SpringGreen": (0, 255, 127),
        "PaleGreen": (152, 251, 152),
        "LightGreen": (144, 238, 144),
        "DarkSeaGreen": (143, 188, 143),
        "MediumSeaGreen": (60, 179, 113),
        "SeaGreen": (46, 139, 87),
        "DarkGreen": (0, 100, 0),
        "Green": (0, 128, 0),
        "ForestGreen": (34, 139, 34),
        "LimeGreen": (50, 205, 50),
        "Lime": (0, 255, 0),
        "LawnGreen": (124, 252, 0),
        "Chartreuse": (127, 255, 0),
        "GreenYellow": (173, 255, 47),
        "YellowGreen": (154, 205, 50),
        "OliveDrab": (107, 142, 35),
        "DarkOliveGreen": (85, 107, 47),
        "Olive": (128, 128, 0),

        "DarkKhaki": (189, 183, 107),
        "Goldenrod": (218, 165, 32),
        "DarkGoldenrod": (184, 134, 11),
        "SaddleBrown": (139, 69, 19),
        "Sienna": (160, 82, 45),
        "RosyBrown": (188, 143, 143),
        "Peru": (205, 133, 63),
        "Chocolate": (210, 105, 30),
        "SandyBrown": (244, 164, 96),
        "NavajoWhite": (255, 222, 173),
        "Wheat": (245, 222, 179),
        "BurlyWood": (222, 184, 135),
        "Tan": (210, 180, 140),

        "MediumSlateBlue": (123, 104, 238),
        "MediumPurple": (147, 112, 219),
        "BlueViolet": (138, 43, 226),
        "Indigo": (75, 0, 130),
        "DarkViolet": (148, 0, 211),
        "DarkOrchid": (153, 50, 204),
        "MediumOrchid": (186, 85, 211),
        "Purple": (128, 0, 128),
        "DarkMagenta": (139, 0, 139),
        "Magenta": (255, 0, 255),
        "Fuchsia": (255, 0, 255),  # Magenta / Fuchsia são o mesmo (por convenção)
        "Violet": (238, 130, 238),
        "Orchid": (218, 112, 214),
        "Plum": (221, 160, 221),

        "MediumVioletRed": (199, 21, 133),
        "DeepPink": (255, 20, 147),
        "HotPink": (255, 105, 180),
        "PaleVioletRed": (219, 112, 147),
        "LightPink": (255, 182, 193),
        "Pink": (255, 192, 203),
        "LightCoral": (240, 128, 128),
        "IndianRed": (205, 92, 92),
        "Crimson": (220, 20, 60),

        "Maroon": (128, 0, 0),
        "DarkRed": (139, 0, 0),
        "FireBrick": (178, 34, 34),
        "Brown": (165, 42, 42),
        "Salmon": (250, 128, 114),
        "DarkSalmon": (233, 150, 122),
        "LightSalmon": (255, 160, 122),
        "Coral": (255, 127, 80),
        "Tomato": (255, 99, 71),
        "Red": (255, 0, 0),

        "OrangeRed": (255, 69, 0),
        "DarkOrange": (255, 140, 0),
        "Orange": (255, 165, 0),

        "Gold": (255, 215, 0),
        "Yellow": (255, 255, 0),
        "Khaki": (240, 230, 140),
    }