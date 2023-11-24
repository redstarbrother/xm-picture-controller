import jsonFileControl as jfc

userInfo_g = {}

userInfoFilePath = 'db/userInfo.json'


def userInfoInit():
    global userInfo_g
    userInfo_g = jfc.loadFile(userInfoFilePath)


def setUserInfo(userInfo):
    return jfc.saveToFile(userInfoFilePath, userInfo)


# 判断用户信息是否为空, 为空则说明首次进入系统
def hasUserInfo():
    global userInfo_g
    return userInfo_g is not None


userInfoInit()
