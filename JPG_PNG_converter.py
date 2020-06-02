import os
from PIL import Image

oldDir = "./Images/"
newDir = "./Images/New/"

if not os.path.exists(newDir):
    os.mkdir(newDir)

image_list = os.listdir("./Images/")

for el in image_list:
    if os.path.isfile(os.path.join(oldDir, el)):
        im = Image.open(os.path.join(oldDir, el))
        im.save(os.path.join(newDir, el.split(".")[0] + ".png"), "png")