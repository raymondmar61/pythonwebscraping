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
        imagefilename = websiteaddressurl + "/" + imagefilename
    print(imagefilename + " imagefilename")
    #image description alt html tag is going to be the image filename savedimagefilename
    imagealt = img.get("alt")
    #if there is no image description, then assign a number as the image filename
    if len(imagealt) == 0:
        savedimagefilename = str(i)
        i += 1
    else:
        savedimagefilename = imagealt
    #saving the image file to present directory
    savingimage = open(savedimagefilename + ".jpg", "wb")
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
        imagefilename = websiteaddressurl + imagefilename
        print(imagefilename) #print https://innovateinfinitely.com/stevejobs.jpg
        #image description alt html tag is going to be the image filename savedimagefilename
        savedimagefilename = img.get("alt")
        #RM:  https://kite.com/python/answers/how-to-get-the-status-code-of-a-website-using-urllib-in-python to check url status code
        urlsrc = urllib.request.urlopen(imagefilename)
        statuscode = urlsrc.getcode()
        print(statuscode)
        if statuscode == 200:
            savingimage = open(savedimagefilename + ".jpg", "wb")
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
        print(imagefilename + " imagefilename") #print myphotoalbum/sanpedrovalleypark.jpg imagefilename
        imagefilename = websiteaddressurl[0:35] + imagefilename
        print(imagefilename) #print https://www.innovateinfinitely.com/myphotoalbum/sanpedrovalleypark.jpg
        #image description alt html tag is going to be the image filename savedimagefilename
        savedimagefilename = img.get("alt")
        #RM:  https://kite.com/python/answers/how-to-get-the-status-code-of-a-website-using-urllib-in-python to check url status code
        urlsrc = urllib.request.urlopen(imagefilename)
        statuscode = urlsrc.getcode()
        print(statuscode)
        if statuscode == 200:
            savingimage = open(savedimagefilename + ".jpg", "wb")
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
        print(imagefilename + " imagefilename") #print https://innovateinfinitely.com/myphotoalbum/myphotoalbum/sanpedrovalleypark.jpg imagefilename . . .
        #image description alt html tag is going to be the image filename savedimagefilename
        savedimagefilename = img.get("alt")
        #saving the image file to present directory
        savingimage = open(savedimagefilename + ".jpg", "wb")
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
        print(imagefilename + " imagefilename") #print https://innovateinfinitely.com/myphotoalbum/myphotoalbum/sanpedrovalleypark.jpg imagefilename . . .
        #image description alt html tag is going to be the image filename savedimagefilename
        savedimagefilename = img.get("alt")
        #RM:  https://kite.com/python/answers/how-to-get-the-status-code-of-a-website-using-urllib-in-python to check url status code
        urlsrc = urllib.request.urlopen(imagefilename)
        statuscode = urlsrc.getcode()
        print(statuscode) #print 200
        if statuscode == 200:
            savingimage = open(savedimagefilename + ".jpg", "wb")
            savingimage.write(urllib.request.urlopen(imagefilename).read())
            savingimage.close()
    except:
        pass

#Python 3 Tutorial for Beginners 29 - Downloading Images
import urllib.request
from random import randint
def downloadjpg(websiteaddressurl, filedirectory, filename):
    fullfiledirectory = filedirectory + filename + ".jpg"
    urllib.request.urlretrieve(websiteaddressurl, fullfiledirectory)


websiteaddressurl = "https://innovateinfinitely.com/stevejobs.jpg"
filename = str(randint(10000, 9rm9999))
downloadjpg(websiteaddressurl, "tempimagesfolder/", filename)
#https://stackoverflow.com/questions/34957748/http-error-403-forbidden-with-urlretrieve, https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
#RM:  I can't confirm it works.
def downloadjpg(websiteaddressurl, filedirectory, filename):
    fullfiledirectory = filedirectory + filename + ".jpg"
    print(fullfiledirectory)
    opener = urllib.request.URLopener()
    opener.addheader("User-Agent", "anything text here")
    opener.retrieve(websiteaddressurl, fullfiledirectory)


#websiteaddressurl = "https://innovateinfinitely.com/stevejobs.jpg"
#websiteaddressurl = "https://imx.to/i/21kaiy"  #RM:  doesn't work because user must click a second time at https://imx.to/i/21kaiy
websiteaddressurl = "https://ist5-1.filesor.com/pimpandhost.com/1/_/_/_/1/6/M/1/T/6M1TP/Angioletta-2.jpg"
filename = str(randint(10000, 99999))
downloadjpg(websiteaddressurl, "tempimagesfolder/", filename)

from urllib.request import urlopen
with open(imagename, "wb") as imagefile: #wb is write bytes
    imagefile.write(urlopen(imageurl).read())

#https://stackoverflow.com/questions/30229231/python-save-image-from-url/30229298
import requests
with open(imagename, "wb") as f:
    f.write(requests.get(imageurl).content)

#https://www.kite.com/python/answers/how-to-download-an-image-using-requests-in-python#:~:text=Use%20requests.,()%20to%20download%20an%20image&text=get(url)%20with%20url%20as,write%2Dand%2Dbinary%20mode.
response = requests.get("https://i.imgur.com/ExdKOOz.png")
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()

#https://stackoverflow.com/questions/3042757/downloading-a-picture-via-urllib-and-python
import urllib.request
urllib.request.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")
import urllib.request
urllib.request.urlretrieve(url, filename)

#https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
# First import wget python module.
import wget
# Set up the image URL
image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
# Use wget download method to download specified image url.
image_filename = wget.download(image_url)
print('Image Successfully Downloaded: ', image_filename)

#https://www.journaldev.com/39379/python-download-file-from-url
import wget
file_url = 'https://www.journaldev.com/wp-content/uploads/2019/08/Python-Tutorial.png' 
dest_file = '/Users/pankaj/pt.png' 
wget.download(file_url, dest_file)
#Downloading a Large File from URL in Python.  If the file is large, then it’s not a good idea to get all the content in one go. It will require a lot of memory and might cause out of memory error.  We can pass stream=True to requests get() method to open a file stream and download it in chunks. Then we can use a for loop to read the chunks and write it into the local file.
import requests 
file_url = 'https://www.journaldev.com/wp-content/uploads/2019/08/Python-Tutorial.png' 
file_stream = requests.get(file_url, stream=True) 
with open('Python-Tutorial.png', 'wb') as local_file:
    for data in file_stream:
        local_file.write(data) 
print('Done')

#https://gist.github.com/mjdietzx/545fa2874b2688e9bcb71e2ee92cd5a0
import io
from PIL import Image  # https://pillow.readthedocs.io/en/4.3.x/
import requests  # http://docs.python-requests.org/en/master/
# example image url: https://m.media-amazon.com/images/S/aplus-media/vc/6a9569ab-cb8e-46d9-8aea-a7022e58c74a.jpg
def download_image(url, image_file_path):
    r = requests.get(url, timeout=4.0)
    if r.status_code != requests.codes.ok:
        assert False, 'Status code error: {}.'.format(r.status_code)
    with Image.open(io.BytesIO(r.content)) as im:
        im.save(image_file_path)
    print('Image downloaded from url: {} and saved to: {}.'.format(url, image_file_path))

#https://python-forum.io/Thread-save-image-from-link
import requests
from io import open as iopen 
def fetch_image(img_ur, save_filename):
    img = requests.get(img_ur)
    if img.status_code == 200:
        with iopen(save_filename, 'wb') as f:
            f.write(img.content)
    else:
        print('Received error: {}'.format(img.status_code)) 
testlink = 'https://vignette.wikia.nocookie.net/pdsh/images/9/95/Prettygoldilocks.jpg' 
filename = 'Goldilocks.jpg'
fetch_image(testlink, filename)

#https://www.codespeedy.com/read-image-from-url-in-python/
# Importing Required Modules
import sys
import requests
from PIL import Image
# Exception Handling for invalid requests
try:
        # Creating an request object to store the response
        # The URL is refrenced sys.argv[1]
  ImgRequest = requests.get(sys.argv[1])
        # Verifying whether the specified URL exist or not
  if ImgRequest.status_code == requests.codes.ok:
                # Opening a file to write bytes from response content
                # Storing this onject as an image file on the hard drive
    img = open("test.jpg","wb")
    img.write(ImgRequest.content)
    img.close()
                # Opening Inage file using PIL Image
    img = Image.open("test.jpg")
    img.show()
  else:
    print(ImgRequest.status_code)
except Exception as e:
  print(str(e))

#https://likegeeks.com/downloading-files-using-python/
#Download large file in chunks
import requests
url = 'https://www.cs.uky.edu/~keen/115/Haltermanpythonbook.pdf'
r = requests.get(url, stream = True)
with open("PythonBook.pdf", "wb") as Pypdf:
    for chunk in r.iter_content(chunk_size = 1024):
        if chunk:
            Pypdf.write(chunk)
#Download multiple files (Parallel/bulk download)
import os
import requests
from time import time
from multiprocessing.pool import ThreadPool
def url_response(url):
    path, url = url
    r = requests.get(url, stream = True)
    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)
            urls = [("Event1", "https://www.python.org/events/python-events/805/"),("Event2", "https://www.python.org/events/python-events/801/"),("Event3", "https://www.python.org/events/python-events/790/"),("Event4", "https://www.python.org/events/python-events/798/"),("Event5", "https://www.python.org/events/python-events/807/"),("Event6", "https://www.python.org/events/python-events/807/"),("Event7", "https://www.python.org/events/python-events/757/"),("Event8", "https://www.python.org/events/python-user-group/816/")]
start = time()
for x in urls:
    url_response (x)
print(f"Time to download: {time() - start}")
ThreadPool(9).imap_unordered(url_response, urls)
#Download with a progress bar
#The Progress bar is a UI widget of the clint module. To install the clint module, type the following command:  pip install clint
import requests
from clint.textui import progress
url = 'http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf'
r = requests.get(url, stream=True)
with open("LearnPython.pdf", "wb") as Pypdf:
    total_length = int(r.headers.get('content-length'))
    for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
        if ch:
            Pypdf.write(ch)