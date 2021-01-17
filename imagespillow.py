#Python Tutorial - Image Manipulation with Pillow-6Qs3wObeWwc

import urllib.request
from PIL import Image
from urllib.request import urlopen
url = "https://innovateinfinitely.com/policecarphotoalbum/policecarphotoalbumca/policecarphotoalbumca/campbellpolicecar017.jpg"
image = Image.open(urllib.request.urlopen(url))
width, height = image.size
print(width, height) #print 1600 1200
print(type(image.size)) #print <class 'tuple'>
if (width >= 1024 and height >= 768) or (width >= 768 and height >= 1024):
    print("love")
    imagename = "campbellpd.jpg"
    savingimage = open(imagename, "wb")
    savingimage.write(urlopen(url).read())
    savingimage.close()

from urllib.request import urlopen
imageurl = "https://innovateinfinitely.com/policecarphotoalbum/policecarphotoalbumca/policecarphotoalbumca/campbellpolicecar017.jpg"
imagename = "campbellpd.jpg"
savingimage = open(imagename, "wb")
savingimage.write(urlopen(imageurl).read())
savingimage.close()

from PIL import Image
import os
imageobject = Image.open("campbellpd.jpg")
imageobject.show()
imageobject.save("campbellpd.png") #save picture as another file name and/or another file extension
for loopeachimage in os.listdir("."):  #"." means current directory
    if loopeachimage.endswith(".jpg"):
        print(loopeachimage)
        createobjectimage = Image.open(loopeachimage)
        filename, fileextension = os.path.splitext(loopeachimage)
        print("filename: " + filename)
        print("filename extension: " + fileextension)
        createobjectimage.save("{}.png".format(filename)) #save the .jpg files as .png files
        #createobjectimage.save("directorybelow/{}.png".format(filename)) #save the .jpg files as .png files in directorybelow current directory
        #createobjectimage.save("myphotoalbum/{}.png".format(filename)) #save the .jpg files as .png files in directorybelow current directory
resizeimage400pixels = (400, 400)
resizeimage200pixels = (200, 200)
for loopeachimage in os.listdir("."):  #"." means current directory
    if loopeachimage.endswith(".jpg"):
        originalimage = Image.open(loopeachimage)
        filename, fileextension = os.path.splitext(loopeachimage)
        newfilename400 = filename + "_resized400pixels"
        originalimage.thumbnail(resizeimage400pixels) #resize image to 400 pixels
        originalimage.save("{}{}".format(newfilename400, fileextension)) #save the .jpg files with newfilename.fileextension
        newfilename200 = filename + "_resized200pixels"
        originalimage.thumbnail(resizeimage200pixels) #resize image to 200 pixels
        originalimage.save("{}{}".format(newfilename200, fileextension)) #save the .jpg files with newfilename.fileextension

imageobject = Image.open("campbellpd.jpg")
imageobject.rotate(90).save("campbellpd90.jpg")
imageobject90 = Image.open("campbellpd90.jpg")
imageobject.convert(mode="L").save("campbellpdblackandwhite.jpg")
imageblackandwhite = Image.open("campbellpdblackandwhite.jpg")
from PIL import Image, ImageFilter
imageobject = Image.open("campbellpd.jpg")
imageobject.filter(ImageFilter.GaussianBlur(radius=15)).save("campbellpdgaussianblur.jpg")
imagegaussianblur = Image.open("campbellpdgaussianblur.jpg")
imagegaussianblur.show()

#Python Working with Images using Pillow-k3-0pHqFOBo
from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter
import glob
imageobject = Image.open("campbellpd.jpg")
print("format: " + imageobject.format) #print format: JPEG
print("size:", imageobject.size) #print size: (1600, 1200) #RM:  (width, height)
print("mode: " + imageobject.mode) #print mode: RGB
#imageobject.show()
rgbaimageobject = imageobject.convert("RGBA")
for (i, filename) in enumerate(glob.glob("zion*.jpg")): #.glob(can write any directory with correct path)
    print(filename) #print all files with zion and *.jpg in directory
    resizeimage800x600 = Image.open(filename).resize((800, 600))
    resizeimage800x600.save(filename[:-4] + "800x600.jpg")
rotateimage45degrees = imageobject.rotate(45)
mirrorimage = ImageOps.mirror(imageobject) #like flip horizontally or looking at a mirror
flipimagevertically = ImageOps.flip(imageobject)
overlayrectangleonimage = imageobject.copy()
ImageDraw.Draw(overlayrectangleonimage).rectangle([(100, 200), (500, 700)]) #Rectangle coordinates are [(upper left), (bottom right)]
addaborderaroundimage = ImageOps.expand(imageobject.copy(), border=20, fill="black")
cropimage = Image.open("campbellpd.jpg")
cropimagecropped = cropimage.crop((500, 900, 1200, 1500)) #Coordinates are (left x coordinate, upper y coordinate, right x coordinate, lower y coordinate) tuples.  Suggestion open a photo editing to get coordinates.
pasteimageontoanotherimagetop = Image.open("zionthesubway.jpg")
pasteimageontoanotherimagecopybottom = Image.open("zionnarrowsbottomup.jpg")
pasteimageontoanotherimagecopybottom.paste(pasteimageontoanotherimagetop, (300, 600)) #pasteimageontoanotherimagetop is on top of pasteimageontoanotherimagecopybottom
brighterimage = Image.open("campbellpd.jpg")
brighterimageadjusted = ImageEnhance.Brightness(brighterimage).enhance(1.5)
filterimageblur = imageobject.filter(ImageFilter.EMBOSS) #EMBOSS must be CAPS
#other .filter are BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, \nSMOOTH, SMOOTH_MORE, and SHARPEN\n
changecolors = Image.open("campbellpd.jpg")
r, g, b = changecolors.split()
changecolorsadjusted = Image.merge("RGB", (b, g, r)) #change colors to blue, green, red
blackandwhiteimage = Image.open("campbellpd.jpg")
blackandwhiteimageadjusted = blackandwhiteimage.convert("L")
#skipped composite and blend composite images
#blend two images together or combine two images together composite compositing
blendimage1 = Image.open("zionthesubway.jpg")
blendimage2 = Image.open("zionnarrowsbottomup.jpg")
blendimage12 = Image.blend(blendimage1, blendimage2, 0.9) #blendimage1 is priority with 0.1, blendimage2 is priority with 0.9
blendimage12.show()

#How do I read image data from a URL in Python_ - Stack Overflow.pdf
from PIL import Image
import requests
from io import BytesIO
response = requests.get(url)
img = Image.open(BytesIO(response.content))

#Get image size (width, height) with Python, OpenCV, Pillow (PIL) _ note.nkmk.me.pdf
#OpenCV image width and image height obtained as a tuple with the attribute shape of NumpPy array ndarray or ndarray.shape.  The width and height can be acquired by the attribute shape indicating the shape of ndarray.
#PIL.Image image width and image height obtained with attribute size, width, and height

import cv2
imagepic = cv2.imread("campbellpd.jpg")
print(type(imagepic)) #print <class 'numpy.ndarray'>
print(imagepic.shape) #print (1200, 1600, 3)  #RM:  height, width, color(3) which is channel I don't know what channel means
print(type(imagepic.shape)) #print <class 'tuple'>
print((imagepic.shape)[0]) #print 1200
width = imagepic.shape[1]
print(width) #print 1600
imageheight, imagewidth, _ = imagepic.shape
print("width", imagewidth, "height", imageheight)
print(imagepic.shape[1::-1]) #print (1600, 1200)
imagegrayscale = cv2.imread("campbellpdblackandwhite.jpg", cv2.IMREAD_GRAYSCALE) #RM:  IMREAD_GRAYSCALE must be caps
print(imagegrayscale.shape) #print (1200, 1600)
print(type(imagegrayscale.shape)) #print <class 'tuple'>
print("\n")

from PIL import Image
imagepillowpic = Image.open("campbellpd.jpg")
print(imagepillowpic.size) #print (1600, 1200)
print(type(imagepillowpic.size)) #print <class 'tuple'>
imagepillowpicwidth, imagepillpwpicheight = imagepillowpic.size
print("width pillow", imagepillowpicwidth) #print width pillow 1600
print("height pillow", imagepillpwpicheight) #print height pillow 1200
imagepillowpicgrayscale = Image.open("campbellpd.jpg").convert("L")
print(imagepillowpicgrayscale.size) #print (1600, 1200)
print(type(imagepillowpicgrayscale.size)) #print <class 'tuple'>
