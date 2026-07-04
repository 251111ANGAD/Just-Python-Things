import cv2
import os
from datetime import datetime

from logger import log


class Recorder:

    def __init__(self, fps=30):

        self.writer = None
        self.recording = False
        self.filename = ""
        self.start_time = None
        self.fps = fps

    def start(self, frame):

        if self.recording:
            return

        os.makedirs("recordings", exist_ok=True)

        h, w = frame.shape[:2]

        self.filename = datetime.now().strftime(
            "recordings/%Y-%m-%d_%H-%M-%S.mp4"
        )

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        self.writer = cv2.VideoWriter(
            self.filename,
            fourcc,
            self.fps,
            (w, h)
        )

        self.recording = True
        self.start_time = datetime.now()

        log(f"Recording started: {self.filename}")

    def write(self, frame):

        if self.recording:
            self.writer.write(frame)

    def stop(self):

        if not self.recording:
            return

        self.writer.release()

        self.recording = False

        log("Recording stopped")

    def release(self):

        if self.recording:
            self.stop()