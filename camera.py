import cv2

from config import SETTINGS


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(SETTINGS["camera"])

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,
                     SETTINGS["width"])

        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,
                     SETTINGS["height"])

    def read(self):

        return self.cap.read()

    def release(self):

        self.cap.release()