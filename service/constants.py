import os


TMP_FILE_PATH = os.getenv("TMP_FILE_PATH", "tmp")

if not os.path.exists(TMP_FILE_PATH):
    os.mkdir(TMP_FILE_PATH)


VIDEO_PATH = AUDIO_PATH = os.path.abspath(TMP_FILE_PATH)
PICTURES_FORMAT = ("jpg", "png")
VIDEOS_FORMAT = ("mp4", "avi", "mkv")
AUDIOS_FORMAT = ("mp3",)


class Color:
    all = ("white", "black", "gery")
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]
    GERY = [127, 127, 127]
    mapping = {
        "white": WHITE,
        "black": BLACK,
        "gery": GERY,
    }

    @classmethod
    def get(cls, color):
        assert color in cls.all
        return cls.mapping.get(color)


class Size:
    P720 = (720, 1280)
    P1080 = (1080, 1920)
    P1440 = (1440, 2560)
    P2160 = (2160, 3840)
    P4320 = (4320, 7680)
    size = P720
