import subprocess
from enum import Enum
from app.photoUtilities import PhotoManager
CAMERAMODEL = "Nikon DSC D3100" # DSLR Camera (Nikon D100)
PHOTODIR = "/home/adrian/PycharmProjects/PhotoBooth/Photos"


def main():
    camera = CameraManager(CAMERAMODEL)
    camera.detectCamera()
    camera.readCameraInfo()
    #camera.getConfig("focusmode")
    #camera.setConfigProporties("focusmode",FocusMode.Manual)
    camera.takePhotos()
    PhotoManager.move_to_temp()


class CameraManager:
    # Camera Connection Manager is a set of methods used to interface directly with the camera
    def __init__(self, cameraModel):
        self.cameraModel = cameraModel

    def detectCamera(self):
        message = "gphoto2 --auto-detect"
        cameraReadout = TalkToTerminal(message)
        if self.cameraModel in cameraReadout:
            print(self.cameraModel + " was detected.")
            return True
        else:
            print(self.cameraModel + " was not detected. Please check your connection and try again")
            return False

    def readCameraInfo(self):
        message = "gphoto2 --summary"
        cameraReadout = TalkToTerminal(message,stderr=True)
        return cameraReadout
        # implement error handling here. Should read the stderr signal from the Popen function
        # if <<ERROR>> then print("The USB is currently being used. The connection is being reset")

    def takePhotos(self,qty=4):
        for photo in range(1,qty+1):
            print("Taking Photo #%i" %photo)
            message = "gphoto2 --capture-image-and-download"
            stdout, stderr = TalkToTerminal(message,stderr=True)
            print(stdout)
            photo +=1

    def getConfig(self,name):
        message = "gphoto2 --get-config " + name
        stdout = TalkToTerminal(message)
        print(stdout)

    def setConfigProporties(self,name,value):
        message = "gphoto2 --set-config " + name +"="+value.value
        stdout = TalkToTerminal(message)
        print(stdout)

def TalkToTerminal(messageToTerminal,stderr=False):
    # This function creates a simiplified communication method to interact from Python to the command line
    if stderr == False:
        messageFromTerminal = subprocess.Popen(messageToTerminal.split(" "), stdout=subprocess.PIPE, encoding='UTF-8',
                                           universal_newlines=True)
        return messageFromTerminal.stdout.read()
    else:
        messageFromTerminal =  subprocess.Popen(messageToTerminal.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding='UTF-8',
                                           universal_newlines=True)
        return messageFromTerminal.stdout.read(), messageFromTerminal.stderr.read()


class FlashMode(Enum):
    NoFlash = "0"
    RedEyeAutomatic = "1"
    Auto = "2"

class FocusMode(Enum):
    Manual= "0" # Manual focus mode
    AF_Single = "1" # Used for subjects that don't move
    AF_Continuous = 2 # Used for moving objects
    AF_Auto = "3" # Automatic selection of AF mode

if __name__ == '__main__':
    main()
