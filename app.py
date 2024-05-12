from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
MAX_BUFFER_SIZE = 50 * 1000 * 1000  # 50 MB
socketio = SocketIO(app, max_http_buffer_size=MAX_BUFFER_SIZE)

ip = "0.0.0.0"
port = os.environ['PORT']


@socketio.on('eventServer')
def test_connect(data):
    print("Чет пришло")
    print(data)
    emit('eventClient', {'data': 'пашол'})


@socketio.on('screenShare')
def test_connect(data):
    print("Пришла картинка")
    print(data)
    emit('getScreen', {'blob': data}, broadcast=True, include_self=False)

@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.info("client connected")

@socketio.on('nigger')
def send_niggers():
    emit('echo', {'echo': 'Server Says: '+ "NIGGERS"}, broadcast=True, include_self=False)


@app.route('/test_screen')
def test_screen():
    data = {'ip': ip, 'port': port}
    return render_template('test_screen.html', data=data)

@app.route('/login')
def user_profile():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    socketio.run(app, host = ip, port=port, allow_unsafe_werkzeug=True)