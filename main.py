import cv2
import time

from camera import Camera
from logger import log
from utils import create_folders
from ui import draw
from motion_detector import MotionDetector
from recorder import Recorder
from face_detector import FaceDetector


# ----------------------------
# Setup
# ----------------------------
create_folders()
log("Application started")

camera = Camera()
motion_detector = MotionDetector()
recorder = Recorder()
face_detector = FaceDetector()

last_motion_time = 0
RECORD_AFTER_SECONDS = 5

previous_time = time.time()


# ----------------------------
# Main Loop
# ----------------------------
while True:

    success, frame = camera.read()

    if not success:
        log("Failed to read camera frame")
        break

    # ----------------------------
    # FPS Calculation
    # ----------------------------
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    # ----------------------------
    # Motion Detection
    # ----------------------------
    motion, boxes = motion_detector.detect(frame)

    if motion:
        last_motion_time = time.time()

        if not recorder.recording:
            recorder.start(frame)
            log("Motion detected --> recording started")

    # Draw motion boxes
    for x, y, w, h in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # ----------------------------
    # Recording Logic
    # ----------------------------
    if recorder.recording:

        recorder.write(frame)

        if time.time() - last_motion_time > RECORD_AFTER_SECONDS:
            recorder.stop()
            log("No motion --> recording stopped")

    # ----------------------------
    # UI Overlay
    # ----------------------------
    draw(frame, fps)

    # Motion text
    if motion:
        cv2.putText(
            frame,
            "MOTION DETECTED",
            (15, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # REC indicator
    if recorder.recording:
        cv2.circle(frame, (25, 120), 8, (0, 0, 255), -1)

        cv2.putText(
            frame,
            "REC",
            (40, 126),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    # ----------------------------
    # Show Frame
    # ----------------------------
    cv2.imshow("Security Camera AI", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        log("Quit pressed")
        break

    if key == ord("s"):
        filename = f"snapshots/{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        log(f"Snapshot saved: {filename}")


# ----------------------------
# Cleanup
# ----------------------------
recorder.release()
camera.release()
cv2.destroyAllWindows()

log("Application closed")