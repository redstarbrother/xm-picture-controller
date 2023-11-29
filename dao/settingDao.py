import jsonFileControl as jfc

setting_g = {}

settingFilePath = 'db/setting.json'


def settingInit():
    global setting_g
    setting_g = jfc.loadFile(settingFilePath)


def setSetting(setting):
    return jfc.saveToFile(settingFilePath, setting)


def getSetting():
    global setting_g
    return setting_g
