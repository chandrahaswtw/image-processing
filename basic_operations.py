from PIL import Image, ImageFilter, ImageOps

# CREATING THE IMAGE OBJECT
im = Image.open('./Images/coconut.jpg')
print(im)

# PRINTING FORMAT, SIZE & MODE
print(im.format, im.size, im.mode)

# BLUR THE IMAGE AND STORE IN THE MEMORY
im1 = im.filter(ImageFilter.BLUR)
im1.show()   # THIS JUST SHOWS THE IMAGE
im1.save("./Images/Blur.png", "png")  # THIS STORES THE IMAGE IN A SPECIFIED LOCATION

# GRAYSCALE
im2 = ImageOps.grayscale(im)
im2.show()

# CROP THE IMAGE
im_crop = im.crop((20, 20, 100, 100))   # The values are the pixels
im_crop.show()

# RESIZE THE IMAGE .resize() doesn't respect the aspect ratio
im_resize = im.resize((300, 300)) # The values are the pixels
im_resize.show()

# RESIZE THE IMAGE .resize() respect the aspect ratio
# This alters the original image
im.thumbnail((300, 300)) # The values are the pixels
im.show()

# CLOSING THE IMAGE
im.close()
