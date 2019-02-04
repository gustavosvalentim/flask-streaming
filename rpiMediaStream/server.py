from flask import Flask, render_template, Response
from .camera import rpiCamera

import socket


video = rpiCamera()


app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello World'

@app.route('/<int:rpiPort>')
def index(rpiPort):
    serverHost = socket.gethostbyname(socket.gethostname())
    return render_template('index.html', rpiPort=rpiPort, serverHost=serverHost)


@app.route('/<int:rpiPort>/jpg')
def image(rpiPort):
	img_bytes = video.getFrame()
	return Response(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n', mimetype='multipart/x-mixed-replace; boundary=frame')