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
#Here is one variation with statuscode check and shorter length code
websiteaddressurl = "https://innovateinfinitely.com/"
i = 1
def makesoup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata
#call function makesoup with website address url to get the html code
soup = makesoup(websiteaddressurl)
#get all img tags html code
for img in soup.findAll('img'):
	try:
		print(img) #print <img alt="Steve Jobs Stay Hungry Stay Foolish" class="imagelinkhover" src="stevejobs.jpg"/>
		#get the html image file name
		imagefilename = img.get("src")
		imagefilename = websiteaddressurl+imagefilename
		print(imagefilename) #print https://innovateinfinitely.com/stevejobs.jpg
		#image description alt html tag is going to be the image filename savedimagefilename
		savedimagefilename = img.get("alt")
		#RM:  https://kite.com/python/answers/how-to-get-the-status-code-of-a-website-using-urllib-in-python to check url status code
		urlsrc = urllib.request.urlopen(imagefilename)
		statuscode = urlsrc.getcode()
		print(statuscode)
		if statuscode == 200:
			savingimage = open(savedimagefilename+".jpg","wb")
			savingimage.write(urllib.request.urlopen(imagefilename).read())
			savingimage.close()
	except:
		pass
#Here is a second variation downloading pics from myphotoalbum.html directly with statuscode check
import urllib
from bs4 import BeautifulSoup
websiteaddressurl = "https://www.innovateinfinitely.com/myphotoalbum.html"
i = 1
def makesoup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata
#call function makesoup with website address url to get the html code
soup = makesoup(websiteaddressurl)
#get all img tags html code
for img in soup.findAll('img'):
	try:
		print(img) #print <img alt="Selfie First Hike McNee Ranch State Park Overlooking Pacific Ocean" border="0" height="150" src="myphotoalbum/sanpedrovalleypark.jpg" width="200"/>
		#get the html image file name
		print(img.get("src")) #print myphotoalbum/sanpedrovalleypark.jpg
		imagefilename = img.get("src")		
		print(imagefilename+" imagefilename") #print myphotoalbum/sanpedrovalleypark.jpg imagefilename
		imagefilename = websiteaddressurl[0:35]+imagefilename
		print(imagefilename) #print https://www.innovateinfinitely.com/myphotoalbum/sanpedrovalleypark.jpg
		#image description alt html tag is going to be the image filename savedimagefilename
		savedimagefilename = img.get("alt")
		#RM:  https://kite.com/python/answers/how-to-get-the-status-code-of-a-website-using-urllib-in-python to check url status code
		urlsrc = urllib.request.urlopen(imagefilename)
		statuscode = urlsrc.getcode()
		print(statuscode)
		if statuscode == 200:
			savingimage = open(savedimagefilename+".jpg","wb")
			savingimage.write(urllib.request.urlopen(imagefilename).read())
			savingimage.close()
	except:
		pass
#Here is a third variation downloading full size photos from myphotoalbum.html
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
#Try except checking status code is 200
import urllib
from bs4 import BeautifulSoup
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
	try:
		#print(img) #print <img alt="Selfie First Hike McNee Ranch State Park Overlooking Pacific Ocean" border="0" height="150" src="myphotoalbum/sanpedrovalleypark.jpg" width="200"/> . . . 
		#print(img.get("src")) #print myphotoalbum/sanpedrovalleypark.jpg\n myphotoalbum/oaklandathletics2019.jpg\n  . . .
		#get the html image file name and write correct Python code to download correct html file name
		imagefilename = img.get("src")
		imagefilename = websiteaddressurl[0:43] + "/" + imagefilename
		print(imagefilename+" imagefilename") #print https://innovateinfinitely.com/myphotoalbum/myphotoalbum/sanpedrovalleypark.jpg imagefilename . . . 
		#image description alt html tag is going to be the image filename savedimagefilename
		savedimagefilename = img.get("alt")
		#RM:  https://kite.com/python/answers/how-to-get-the-status-code-of-a-website-using-urllib-in-python to check url status code
		urlsrc = urllib.request.urlopen(imagefilename)
		statuscode = urlsrc.getcode()
		print(statuscode) #print 200
		if statuscode == 200:
			savingimage = open(savedimagefilename+".jpg","wb")
			savingimage.write(urllib.request.urlopen(imagefilename).read())
			savingimage.close()
	except:
		pass

#Python 3 Tutorial for Beginners 29 - Downloading Images
import urllib.request
from random import randint
def downloadjpg(websiteaddressurl, filedirectory, filename):
	fullfiledirectory = filedirectory+filename+".jpg"
	urllib.request.urlretrieve(websiteaddressurl, fullfiledirectory)
websiteaddressurl = "https://innovateinfinitely.com/stevejobs.jpg"
filename = str(randint(10000,9rm9999))
downloadjpg(websiteaddressurl,"tempimagesfolder/",filename)
#https://stackoverflow.com/questions/34957748/http-error-403-forbidden-with-urlretrieve, https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
#RM:  I can't confirm it works.
def downloadjpg(websiteaddressurl, filedirectory, filename):
	fullfiledirectory = filedirectory+filename+".jpg"
	print(fullfiledirectory)
	opener = urllib.request.URLopener()
	opener.addheader("User-Agent", "anything text here")
	opener.retrieve(websiteaddressurl, fullfiledirectory)
#websiteaddressurl = "https://innovateinfinitely.com/stevejobs.jpg"
#websiteaddressurl = "https://imx.to/i/21kaiy"  #RM:  doesn't work because user must click a second time at https://imx.to/i/21kaiy
websiteaddressurl = "https://ist5-1.filesor.com/pimpandhost.com/1/_/_/_/1/6/M/1/T/6M1TP/Angioletta-2.jpg"
filename = str(randint(10000,99999))
downloadjpg(websiteaddressurl,"tempimagesfolder/",filename)