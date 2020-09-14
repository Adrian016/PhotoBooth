import subprocess
from enum import Enum

CAMERAMODEL = "Nikon DSC D3100" # DSLR Camera (Nikon D100)
PHOTODIR = "/home/adrian/PycharmProjects/PhotoBooth/Photos"


def TalkToTerminal(messageToTerminal,stderr=False):
    if stderr == False:
        messageFromTerminal = subprocess.Popen(messageToTerminal.split(" "), stdout=subprocess.PIPE, encoding='UTF-8',
                                           universal_newlines=True)
        return messageFromTerminal.stdout.read()
    else:
        messageFromTerminal =  subprocess.Popen(messageToTerminal.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding='UTF-8',
                                           universal_newlines=True)
        return messageFromTerminal.stdout.read(), messageFromTerminal.stderr.read()

class CameraConnectionManager:
    def __init__(self, cameraModel):
        self.cameraModel = cameraModel
        #TODO Include any other specific

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

    #
    # def terminateConnection(self):
    #     # TODO End camera connection

    def takePhotos(self):
        for photo in range(1,5):
            print("Taking Photo #%i" %photo)
            message = "gphoto2 --capture-image-and-download"
            stdout, stderr = TalkToTerminal(message,stderr=True)
            print(stdout)
            photo +=1

        # TODO Tell camera to take a photo from the command line

    def setPhotoDirectory(self,dir):
        pprint("Setting the photo download directory to "+dir)
        #subprocess.call(["cd",dir])


if __name__ == '__main__':
    main()

# Create camera object
camera   = CameraConnectionManager(CAMERAMODEL)
camera.detectCamera()
camera.readCameraInfo()
camera.takePhotos()

