from PIL import Image
import os


class Size():
    def __init__(self, canvas_width, canvas_height, image_apect_ratio=1.5):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas_size = (canvas_width, canvas_height)
        self.photo_width = int(canvas_width / 2.3)
        self.photo_height = int(self.photo_width / image_apect_ratio)
        self.photo_size = (self.photo_width, self.photo_height)

    @property
    def quadrants(self):
        return [
            (0, 0),
            (self.canvas_width / 2, 0),
            (0, self.canvas_height / 2),
            (self.canvas_width / 2, self.canvas_height / 2)
        ]




def main():
    canvas = Size(1500, 900)

    for i in range(0,4):
        print(canvas.quadrants[i])


if __name__ == '__main__':
    main()

#########################
# PHOTO PASTE TESTING
#########################
# photo_dir = os.path.join(os.getcwd(),"photos")
# photo_name = ("photo1.JPG", "photo8.png")
# new_photo_dir = os.path.join(os.getcwd(),"new_photos")
#
# photo = Image.open(os.path.join(photo_dir, photo_name[1])) # type: Image.Image
# resized_photo = photo.resize((652, 435))
# #background = Image.open(os.path.join(photo_dir, photo_name[1]))
#
# new_image = Image.new("RGB",(1500, 900),(256,256,256))
# logo = Image.new("RGB",(100,100),(231,188,102))
# new_image.paste(logo,(600,450))
