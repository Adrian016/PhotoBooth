from math import sqrt
from app.photoUtilities import PhotoManager
from PIL import Image
import os


def main():

    photo_data= dict(
        # Read in photos to add to collage
        photo_dir = os.path.join(os.getcwd(), "temp"),
        photo_names = ("photo1.JPG", "photo2.JPG", "photo3.JPG", "photo4.JPG"),
        logo_dir = os.path.join(os.getcwd(), "images"),
        logo_name = "logo.png",
        footer_dir = os.path.join(os.getcwd(), "images"),
        footer_name = "WeddingInfo.png",
        collage_dir = os.path.join(os.getcwd(), "static",'images'),
        collage_name = "collage"
        )

    canvas_size = (1800, 1200)

    collage = Collage(canvas_size, photo_data, has_logo = True, has_footer = True)
    collage.build()




class Collage:

    def __init__(self, canvas_size, photo_data, image_apect_ratio=3 / 2, centerline_padding_px = 10,
                 upper_padding = 20, footer_padding=100, has_logo = False, has_footer = False, logo_width_ratio=0.15, canvas_whitespace_ratio = 0.2, photo_sizing_method='padding'):
        self.canvas_width = canvas_size[0]
        self.canvas_height = canvas_size[1]
        self.canvas_size = canvas_size
        self.image_aspect_ratio = image_apect_ratio
        self.footer_padding = footer_padding
        self.photo_sizing_method = photo_sizing_method
        self.canvas = self.create_canvas()
        self.photos = []
        self.resized_photos = []
        self.logo = None  # type: Image.Image
        self.footer = None  # type: Image.Image
        self.centerline_padding_px = centerline_padding_px # Padding between centerline and photo sides
        self.padding = upper_padding
        self.logo_width_ratio = logo_width_ratio
        self.has_logo = has_logo
        self.has_footer = has_footer
        self.canvas_whitespace_ratio = canvas_whitespace_ratio
        self.collage_path = ''
        self.collage_filename = ''
        self.collage_id = ''


        # Breakdown photo data
        self.photo_dir = photo_data['photo_dir']
        self.photo_names = photo_data['photo_names']
        self.logo_dir = photo_data['logo_dir']
        self.logo_name = photo_data['logo_name']
        self.footer_dir = photo_data['footer_dir']
        self.footer_name = photo_data['footer_name']
        self.collage_dir = photo_data['collage_dir']
        self.collage_name = photo_data['collage_name']


    def build(self):

        self.load_photos_from_file(self.photo_dir, self.photo_names)
        self.load_logo_from_file(self.logo_dir, self.logo_name)
        self.load_footer_from_file(self.footer_dir, self.footer_name)
        self.resize_photos()
        self.resize_logo()
        self.resize_footer()
        self.paste_photos_to_canvas()
        self.collage_id = self.next_collage_id()
        self.collage_path = os.path.join(self.collage_dir, self.collage_name + self.collage_id)
        self.canvas.save(self.collage_path+".jpeg", format = 'JPEG',)
        self.collage_filename = self.collage_name + self.collage_id + ".jpeg"


    def next_collage_id(self):
        # TODO Build in counter for next collage index number
        next_index = PhotoManager.next_index_from_file_dir(self.collage_dir,self.collage_name)
        print(next_index)
        return next_index


    def create_canvas(self, mode="RGB", color="white"):
        canvas = Image.new(mode, self.canvas_size, color)
        return canvas

    @property
    def quadrants(self):
        midline_x = self.canvas_width/2
        midline_y = (self.canvas_height - self.footer_padding - 2 * self.padding) / 2 + self.padding
        top_y_offset = self.padding
        left_x_offset = midline_x - self.centerline_padding_px - self.photo_width
        mid_x_offset = midline_x + self.centerline_padding_px
        mid_y_offset = midline_y + self.centerline_padding_px

        left_x_offset = int(left_x_offset)
        mid_x_offset = int(mid_x_offset)
        top_y_offset = int(top_y_offset)
        mid_y_offset = int(mid_y_offset)

        # print("The following offsets are being used:\n"
        #       "- Midline are {0} in X and {1} in Y\n"
        #       "- Left X Offset is {2} px\n"
        #       "- Top Y Offset is {3} px\n"
        #       "- Middle X Offset is {4} px\n"
        #       "- Middle Y Offset is {5} px"
        #       .format(midline_x, midline_y, left_x_offset,top_y_offset, mid_x_offset, mid_y_offset))


        return [
            (left_x_offset, top_y_offset),
            (left_x_offset, mid_y_offset),
            (mid_x_offset, top_y_offset),
            (mid_x_offset, mid_y_offset)
        ]

    def load_photos_from_file(self, photo_dir, photo_names):
        # Open 4 photos and create a photo collection
        for i in range(0, 4):
            photo = Image.open(os.path.join(photo_dir, photo_names[i]))  # type: Image.Image
            self.photos.append(photo)
        return self.photos

    def load_logo_from_file(self, logo_dir, logo_name):
        self.logo = Image.open(os.path.join(logo_dir,logo_name)) #type: Image.Image


    def load_footer_from_file(self,footer_dir,footer_name):
        self.footer = Image.open(os.path.join(footer_dir, footer_name))  # type: Image.Image

    def resize_logo(self):
        size = self.logo.size
        aspect_ratio = size[0]/size[1]

        new_logo_width = int(self.canvas_width * self.logo_width_ratio)
        new_logo_height = int(new_logo_width / aspect_ratio)

        new_size = (new_logo_width, new_logo_height)

        print("Original logo size is {0} by {1}".format(self.logo.size[0], self.logo.size[1]))

        self.logo = self.logo.resize(new_size)

        print("New logo size is {0} by {1}".format(self.logo.size[0],self.logo.size[1]))

    def resize_footer(self):
        size = self.footer.size
        aspect_ratio = size[0]/size[1]

        new_footer_height = int(self.footer_padding * 0.8)
        new_footer_width = int(new_footer_height * aspect_ratio)

        new_size = (new_footer_width, new_footer_height)

        print("Original footer size is {0} by {1}".format(self.footer.size[0], self.footer.size[1]))

        self.footer = self.footer.resize(new_size)

        print("New footer size is {0} by {1}".format(self.footer.size[0],self.footer.size[1]))



    @property
    def photo_size(self):

        if self.photo_sizing_method == "padding":
            photo_height = (self.canvas_height - 2 * self.padding - self.footer_padding - 2 * self.centerline_padding_px) / 2
            photo_width = self.image_aspect_ratio * photo_height
        elif self.photo_sizing_method == "area":
            canvas_area = (self.canvas_height - self.footer_padding) * (self.canvas_width)
            photo_area = canvas_area * (1-self.canvas_whitespace_ratio) / 4
            photo_height = sqrt(photo_area / self.image_aspect_ratio)
            photo_width = self.image_aspect_ratio * photo_height

        photo_height = int(photo_height)
        photo_width = int(photo_width)

        return (photo_width, photo_height)

    @property
    def photo_width(self):
        return self.photo_size[0]

    @property
    def photo_height(self):
        return self.photo_size[1]

    def resize_photos(self):
        # Load in photo list object
        for photo in self.photos:
            resized_photo = photo.resize(self.photo_size, resample =3 )
            self.resized_photos.append(resized_photo)
        # print("New photo size is {0} by {1}".format(self.photo_size[0],self.photo_size[1]))

    def paste_photos_to_canvas(self):
        for i in range(0, 4):
            self.canvas.paste(self.resized_photos[i], self.quadrants[i])
        
        if self.has_logo == True:
            self.canvas.paste(self.logo, self.logo_location,self.logo)
        if self.has_footer == True:
            self.canvas.paste(self.footer, self.footer_location, self.footer)

    @property
    def logo_location(self):
        logo_size = self.logo.size
        midline_x_offset = self.canvas_width / 2
        midline_y_offset = (self.canvas_height - self.footer_padding + self.padding) / 2
        logo_x_offset = midline_x_offset - logo_size[0] / 2
        logo_y_offset = midline_y_offset - logo_size[1] / 2

        logo_x_offset = int(logo_x_offset)
        logo_y_offset = int(logo_y_offset)

        return (logo_x_offset, logo_y_offset)

    @property
    def footer_location(self):

        footer_x_offset = self.quadrants[0][0]
        footer_y_offset = self.canvas_height - self.footer_padding - self.padding + 0.2*self.footer_padding

        footer_x_offset = int(footer_x_offset)
        footer_y_offset = int(footer_y_offset)

        return (footer_x_offset, footer_y_offset)








if __name__ == '__main__':
    main()
