import cv2
import eel
import base64
from threading import Thread

eel.init('web')

class CameraThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.camera = cv2.VideoCapture(0)
        self.frame = None
        self.running = True

    def run(self):
        while self.running:
            success, frame = self.camera.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = base64.b64encode(buffer.tobytes()).decode('utf-8')
            self.frame = 'data:image/jpeg;base64,' + frame
            eel.updateImage(self.frame)

    def stop(self):
        self.running = False
        self.join()

@eel.expose
def start_camera():
    global camera_thread
    camera_thread = CameraThread()
    camera_thread.start()

@eel.expose
def stop_camera():
    global camera_thread
    camera_thread.stop()

eel.start('index.html', size=(1500, 900))
