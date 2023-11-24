import json


# 获取配置文件并转换为dict对象
import logging


def getConfig(type):
    if type == 'baseConfig':
        with open('db/setting.json', encoding='utf-8') as f:
            return json.load(f)
    else:
        with open('db/userInfo.json', encoding='utf-8') as f:
            return json.load(f)


# 将配置对象转换为json格式并保存至文件
def setConfig(type, config):
    if type == 'baseConfig':
        with open('db/setting.json', 'w', encoding='utf-8') as f:
            f.write(str(json.dumps(config)))
    else:
        with open('db/userInfo.json', 'w', encoding='utf-8') as f:
            f.write(str(json.dumps(config)))


# 获取json文件内容
def loadFile(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


# 存储json文件
def saveToFile(path, fileContent):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(json.dumps(fileContent)))
        return True
    except Exception:
        return False
