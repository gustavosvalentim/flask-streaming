import cv2


class rpiCamera:

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    
    def __del__(self):
        self.video.release()
    

    def getFrame(self):
        status, frame = self.video.read()
        value, buffer = cv2.imencode('.jpg', frame)
        return buffer.tobytes()