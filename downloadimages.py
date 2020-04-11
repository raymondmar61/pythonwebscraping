#download pictures from a webpage
import requests
from bs4 import BeautifulSoup
import os

#Introduction to Web Scraping (Python) - Lesson 04 (Download Images)
#RM:  Must look at HTML code and make adjustments to the code because the Python code depends on how the HTML code is written.
#Here is one variation
websiteaddressurl = "https://innovateinfinitely.com"
i = 1
def makesoup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata
#call function makesoup with website address url to get the html code
soup = makesoup(websiteaddressurl)
#get all img tags html code
for img in soup.findAll('img'):
	#print(img) #print <img alt="Raymond Mar" src="raymondmarindex.jpg"/> . . . 
	print(img.get("src")) #print raymondmarindex.jpg\n stevejobs.jpg\n raymondmarmyphotoalbum.jpg\n . . . 
	#if the img src is a relative hyperlink checking the first character is a forward slash
	imagefilename = img.get("src")
	if imagefilename[0] == "/":
		imagefilename = websiteaddressurl + imagefilename
	else:
		imagefilename = websiteaddressurl +"/"+ imagefilename
	print(imagefilename+" imagefilename")
	#image description alt html tag is going to be the image filename savedimagefilename
	imagealt = img.get("alt")
	#if there is no image description, then assign a number as the image filename
	if len(imagealt) == 0:
		savedimagefilename = str(i)
		i+=1
	else:
		savedimagefilename = imagealt
	#saving the image file to present directory
	savingimage = open(savedimagefilename+".jpg","wb")
	savingimage.write(urllib.request.urlopen(imagefilename).read())
	savingimage.close()
#Here is another variation
websiteaddressurl = "https://innovateinfinitely.com/myphotoalbum.html"
i = 1
def makesoup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata
#call function makesoup with website address url to get the html code
soup = makesoup(websiteaddressurl)
#get all img tags html code
for img in soup.findAll('img'):
	print(img) #print <img alt="Selfie First Hike McNee Ranch State Park Overlooking Pacific Ocean" border="0" height="150" src="myphotoalbum/sanpedrovalleypark.jpg" width="200"/> . . . 
	print(img.get("src")) #print myphotoalbum/sanpedrovalleypark.jpg\n myphotoalbum/oaklandathletics2019.jpg\n  . . . 
	#header photo is located in another html file path.  Skip the header photo
	if img.get("src") == "raymondmarmyphotoalbum.jpg":
		pass
	else:
		#get the html image file name and write correct Python code to download correct html file name
		imagefilename = img.get("src")
		imagefilename = websiteaddressurl[0:43] + "/" + imagefilename
		print(imagefilename+" imagefilename") #print https://innovateinfinitely.com/myphotoalbum/myphotoalbum/sanpedrovalleypark.jpg imagefilename . . . 
		#image description alt html tag is going to be the image filename savedimagefilename
		savedimagefilename = img.get("alt")
		#saving the image file to present directory
		savingimage = open(savedimagefilename+".jpg","wb")
		savingimage.write(urllib.request.urlopen(imagefilename).read())
		savingimage.close()

# #url website with pictures
# url  = "https://innovateinfinitely.com/"
# #download website for parsing
# page = requests.get(url)
# soup = bs(page.text, "html.parser")
# #print(page) #print <Response [200]>
# #print(soup) #print the html code
# #locate all elements with image tag or <img>
# imagetags = soup.findAll("img")
# #print(imagetags) #print html code with <img>
# #create directory for pictures
# if not os.path.exists("pictures"):
# 	os.makedirs("pictures")
# #change directory to copy pictures to the changed directory
# os.chdir("pictures")
# #picture file name number variable
# x = 0
# #write images to directory
# for eachimagetags in imagetags:
# 	try:
# 		url = eachimagetags["src"]
# 		print("url "+url)
# 		source = eachimagetags.get(url)
# 		print("source "+source)
# 		#if source.status_code == 200:
# 		with open(os.path.basename(url),"wb") as picturefile:
# 			print(x)
# 			picturefile.write(requests.get(url).content)
# 			picturefile.close()
# 			x += 1
# 	except:
# 		pass

#https://stackoverflow.com/questions/54338681/how-to-download-images-from-websites-using-beautiful-soup
from PIL import Image
url  = "https://innovateinfinitely.com/"
response = requests.get(url)
soup = bs(response.text,"html.parser")
getimage = soup.find("img")
getimageurl = getimage["src"]
print(getimage) #print <img alt="Raymond Mar" src="raymondmarindex.jpg"/>
print(getimageurl) #print raymondmarindex.jpg
#openimage = Image.open(requests.get(getimageurl, stream=True).raw)
#openimage.save("image.jpg")
with open("filename","wb") as saveimage:
	saveimage.write(requests.get(getimageurl).content)
	saveimage.close()

# website with model images
url = 'https://www.pexels.com/search/model/'
# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')
# locate all elements with image tag
image_tags = soup.findAll('img')
# create directory for model images
if not os.path.exists('models'):
	os.makedirs('models')
# move to new directory
os.chdir('models')
# image file name variable
x = 0
# writing images
for image in image_tags:
	try:
		url = image['src']
		response = requests.get(url)
		if response.status_code == 200:
			with open('model-' + str(x) + '.jpg', 'wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x += 1
	except:
		pass