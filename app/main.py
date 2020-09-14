import os
from app.killaCam import CameraManager, CAMERAMODEL
from app.photoUtilities import PhotoManager
from app.collage import Collage


class PhotoBooth:

    def __init__(self):

        # Capture Camera Photos
        self.camera = CameraManager(CAMERAMODEL)

        # Read in photo, logo and footer name and directory data
        self.photo_data = dict(
            # Read in photos to add to collage
            photo_dir = os.path.join(os.getcwd(), "temp"),
            photo_names = ("photo1.JPG", "photo2.JPG", "photo3.JPG", "photo4.JPG"),
            logo_dir = os.path.join(os.getcwd(), "images"),
            logo_name = "logo.png",
            footer_dir = os.path.join(os.getcwd(), "images"),
            footer_name = "WeddingInfo.png",
            collage_dir = os.path.join(os.getcwd(), "static", "images"),
            collage_name = "collage",
            )

        # Set the size of the collage (width, height)
        self.canvas_size = (1800, 1200)


    def run_photo_booth(self):
        self.take_photos()
        self.build_collage()
        self.send_to_printer(debug=True)


    def take_photos(self):
        self.camera.takePhotos()
        PhotoManager.move_to_temp()

    def build_collage(self):
        self.clg = Collage(self.canvas_size, self.photo_data, has_logo = True, has_footer = True)
        self.clg.build()

    @property
    def collage_filename(self):
        print(self.clg.collage_filename + " has been saved")
        return self.clg.collage_filename

    def send_to_printer(self,debug: bool):
        # Send to Printer
        PRINTER_NAME = 'MG3100-series' # Use '$ lpstat -p' in terminal to get available printer name

        if debug:
            print('lpr -P {0} -o media=d-o400x600 {1}'.format(PRINTER_NAME, self.clg.collage_path))
        else:
            os.system('lpr -P {0} -o media=d-o400x600 {1}'.format(PRINTER_NAME, self.clg.collage_path))

    def send_to_app(self):
        pass


if __name__ == '__main__':
    RunPhotoBooth()