import jsonFileControl as jfc

imageList_g = {}

imageFilePath = 'db/setting.json'


def imageListInit():
    global imageList_g
    imageList_g = jfc.loadFile(imageFilePath)


def setImageList(imageList):
    return jfc.saveToFile(imageFilePath, imageList)


def getImageList():
    global imageList_g
    return imageList_g
