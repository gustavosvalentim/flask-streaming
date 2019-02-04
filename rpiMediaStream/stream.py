from .camera import rpiCamera
from .mic import rpiMicrophone



def camStreaming():
    startCamera = rpiCamera()
    while True:
        frame = startCamera.getFrame()
        data = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

        yield data


def micStreaming():
    startMic = rpiMicrophone()
    while True:
        yield startMic.streamAudio()