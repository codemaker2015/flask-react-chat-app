from flask import Flask, jsonify;
from flask_socketio import SocketIO, send
from flask_cors import CORS
import logging
logging.getLogger('requests').setLevel(logging.ERROR)
logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False)

app.debug = True
app.host = 'localhost'

@socketIo.on("message")
def handleMessage(msg):
    print(msg)
    msg = input("Enter your message: ")
    send(msg, broadcast=True)
    return None

if __name__ == '__main__':
    socketIo.run(app)
