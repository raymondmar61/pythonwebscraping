from urllib.request import urlopen
from bs4 import BeautifulSoup
localhtml = urlopen("file:///home/mar/python/myphotoalbum.html")  #RM:  Complete url from Firefox browser
soup = BeautifulSoup(localhtml, "html.parser")
for eachimage in soup.findAll("td", {"id": "picture"}):
    print(eachimage)
    '''
    <td id="picture"><a href="myphotoalbum/myphotoalbum/minihomegym.jpg"><img alt="I'm Posing With Two Weight Plates And Exercise Mat" border="0" height="200" src="myphotoalbum/minihomegym.jpg" width="150"/></a>
    <br/>
    <a href="myphotoalbum/myphotoalbum/minihomegym.jpg">Exercise Mat, 45-Pound Plate, 25-Pound Plate</a>
    </td>
    '''
    hrefstring = str(eachimage.findAll("a")[1])
    print(hrefstring) #print <a href="myphotoalbum/myphotoalbum/minihomegym.jpg">Exercise Mat, 45-Pound Plate, 25-Pound Plate</a>
    rightcarot = hrefstring.find(">") - 1
    print(str(eachimage.findAll("a")[1])[9:rightcarot]) #print myphotoalbum/myphotoalbum/minihomegym.jpg
    imagename = (eachimage.findAll("a")[1].text) + ".jpg"
    print(imagename) #print Exercise Mat, 45-Pound Plate, 25-Pound Plate.jpg
    #/home/mar/python/myphotoalbum/myphotoalbum
    imageurl = "file:///home/mar/python/" + str(eachimage.findAll("a")[1])[9:rightcarot]
    print(imageurl) #print file:///home/mar/python/myphotoalbum/myphotoalbum/minihomegym.jpg
    savingimage = open(imagename, "wb")
    savingimage.write(urlopen(imageurl).read())
    savingimage.close()

import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.innovateinfinitely.com")
soup = BeautifulSoup(page.content, "html.parser")
for mypageslinks in soup.findAll("a", {"class": "backgroundcolornone"}):
    print(mypageslinks)
    print(mypageslinks.attrs["href"])
    '''
    <a class="backgroundcolornone" href="favoritequotes.html"><img alt="Steve Jobs Stay Hungry Stay Foolish" class="imagelinkhover" src="stevejobs.jpg"/></a>
    favoritequotes.html
    <a class="backgroundcolornone" href="myphotoalbum.html"><img alt="Paul McCartney Concert" class="imagelinkhover" src="raymondmarmyphotoalbum.jpg"/></a>
    myphotoalbum.html
    <a class="backgroundcolornone" href="policecarphotoalbum.html"><img alt="Campbell, CA Police Car" class="imagelinkhover" src="policecarphotoalbumindex.jpg"/></a>
    policecarphotoalbum.html
    '''