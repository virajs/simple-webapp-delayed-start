from flask import Flask
from flask import render_template
import socket
import json
import os
import requests
import time

app = Flask(__name__)

# Get start delay from Environment variable
DELAY_FROM_ENV = os.environ.get('APP_START_DELAY') or 0

@app.route("/")
def main():
    # return 'Hello'
    return render_template('hello.html', name=socket.gethostname(), color='#16a085')


@app.route("/hostname")
def hostname():
    return socket.gethostname()


@app.route("/ready")
def ready():
    return "Message from {0} : I am ready!".format(socket.gethostname())


@app.route("/live")
def live():
    return "Message from {0} : I am live!".format(socket.gethostname())


@app.route("/freeze")
def fail():
    while True:
        print("Message from {0} : I am stuck!".format(socket.gethostname()))
        time.sleep(1)


if __name__ == "__main__":

    if DELAY_FROM_ENV:
        print("Warming Up Application. Will take {0} seconds to finish.".format(DELAY_FROM_ENV))
        time.sleep(int(DELAY_FROM_ENV))

    print("Application Ready!")
    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)