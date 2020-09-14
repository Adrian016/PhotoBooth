import os

photo_data= dict(
# Read in photos to add to collage
    photo_dir = os.path.join(os.getcwd(), "temp"),
    photo_names = ("photo1.JPG", "photo2.JPG", "photo3.JPG", "photo4.JPG"),
    logo_dir = os.path.join(os.getcwd(), "images"),
    logo_name = "logo.png",
    footer_dir = os.path.join(os.getcwd(), "images"),
    footer_name = "WeddingInfo.png",
    collage_dir = os.path.join(os.getcwd(), "collages"),
    collage_name = "collage"
    )

print(photo_data)