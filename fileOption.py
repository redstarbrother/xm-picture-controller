import json


# 获取配置文件并转换为dict对象
def getConfig(type):
    if type == 'baseConfig':
        with open('./config/baseConfig.json', encoding='utf-8') as f:
            return json.load(f)
    else:
        with open('./config/userInfo.json', encoding='utf-8') as f:
            return json.load(f)


# 将配置对象转换为json格式并保存至文件
def setConfig(type, config):
    if type == 'baseConfig':
        with open('./config/baseConfig.json', 'w', encoding='utf-8') as f:
            f.write(str(json.dumps(config)))
    else:
        with open('./config/userInfo.json', 'w', encoding='utf-8') as f:
            f.write(str(json.dumps(config)))
