from flask import Flask, Response, stream_with_context

from rpiMediaStream.camera import rpiCamera
from rpiMediaStream.stream import camStreaming, micStreaming


app = Flask(__name__)


@app.route('/video')
def video():
    return Response(camStreaming(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/audio')
def audio():
    return Response(micStreaming(), mimetype='audio/x-wav;codec=pcm')