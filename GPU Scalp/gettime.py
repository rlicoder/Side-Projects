from time import localtime

def gettime():
    return str(localtime().tm_hour) + ' ' + str(localtime().tm_min) + ' ' + str(localtime().tm_sec)
