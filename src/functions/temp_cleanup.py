import os, shutil
from pathlib import Path

userDir = Path.home()

tempDirOne = 'C:/Windows/Temp'
tempDirTwo = str(userDir) + '/AppData/Local/Temp'

def winTempCleanup():
    print("Deleting Windows/Temp")
    for filename in os.listdir(tempDirOne):
        file_path = os.path.join(tempDirOne, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print("Done!")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
def localTempCleanup():
    print("Deleting /AppData/Local/Temp")
    for filename in os.listdir(tempDirTwo):
        file_path = os.path.join(tempDirTwo, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print("Done!")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def tmpCln():
    winTempCleanup()
    localTempCleanup()
    os.system("pause")
