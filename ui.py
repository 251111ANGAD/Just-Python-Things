import cv2
from datetime import datetime

FONT = cv2.FONT_HERSHEY_SIMPLEX


def draw(frame, fps):

    h, w = frame.shape[:2]

    cv2.rectangle(frame, (0, 0), (w, 90), (25, 25, 25), -1)

    cv2.putText(frame,
                "Security Camera AI",
                (15, 30),
                FONT,
                0.8,
                (0, 255, 0),
                2)

    cv2.putText(frame,
                f"FPS: {int(fps)}",
                (15, 60),
                FONT,
                0.6,
                (255,255,255),
                2)

    cv2.putText(frame,
                datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                (w-270,30),
                FONT,
                0.6,
                (255,255,255),
                2)