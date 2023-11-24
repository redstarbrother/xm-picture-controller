from flask import Flask
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
# from flask.ext.cors import CORS
import fileOption

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

# app.db['SECRET_KEY'] = 'some-super-secret-key'
# app.db['DEFAULT_PARSERS'] = [
#     'flask.ext.api.parsers.JSONParser',
#     'flask.ext.api.parsers.URLEncodedParser',
#     'flask.ext.api.parsers.FormParser',
#     'flask.ext.api.parsers.MultiPartParser'
# ]
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# socketio = SocketIO(app)

# socketio = SocketIO(app)
# CORS(app)

baseConfig = {}
userInfo = {}


@app.route('/')
def index():
    return 'hello world'


@socketio.on('showImg')
def changeCurShow(index):
    print("show img index = ", index)
    emit('changeCurShow', index, broadcast=True)


@socketio.on('connect')
def test_connect():
    print("client connect")


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


# 获取设置
@socketio.on('getbaseConfig')
def getbaseConfig():
    send(baseConfig)


# 更改设置
@socketio.on('changeConfig')
def changeConfig(type, configItem):
    if type == 'baseConfig':
        for key in configItem:
            baseConfig[key] = configItem[key]
    else:
        for key in configItem:
            userInfo[key] = configItem[key]
    fileOption.setConfig(type, baseConfig)
    mes = {
        'type': type,
        'configItem': configItem
    }
    emit('configChanged', mes, broadcast=True)


@socketio.on('getConfig')
def getConfig():
    data = {"baseConfig": baseConfig, "userInfo": userInfo}
    res = {"status": True, "data": data}
    print(str(res))
    return res


if __name__ == '__main__':
    baseConfig = fileOption.getConfig('baseConfig')
    userInfo = fileOption.getConfig('userInfo')
    print('baseConfig: ' + str(baseConfig))
    print('userInfo: ' + str(userInfo))
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
