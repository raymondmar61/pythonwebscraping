import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

start = time.perf_counter()
mainwebpage = "https://innovateinfinitely.com/"
page = requests.get(mainwebpage + "myphotoalbum.html")
soup = BeautifulSoup(page.content, "html.parser")

#no threading
# def downloadimages(imagename, imageurl):
#     with open(imagename, "wb") as imagefile:   #wb is write bytes
#         imagefile.write(urlopen(imageurl).read())
#     time.sleep(3)


# # print(soup.find("td", {"id": "picture"}).findAll("a")[1]) #print <a href="myphotoalbum/myphotoalbum/minihomegym.jpg">Exercise Mat, 45-Pound Plate, 25-Pound Plate</a>
# # print(type(soup.find("td", {"id": "picture"}).findAll("a")[1])) #print <class 'bs4.element.Tag'>
# # print(soup.find("td", {"id": "picture"}).findAll("a")[1]["href"]) #print myphotoalbum/myphotoalbum/minihomegym.jpg
# individualpics = soup.findAll("td", {"id": "picture"})
# for eachindividualpics in individualpics:
#     #print(eachindividualpics.findAll("a")[1]) #print <a href="myphotoalbum/myphotoalbum/minihomegym.jpg">Exercise Mat, 45-Pound Plate, 25-Pound Plate</a>
#     eachindividualpicsurls = eachindividualpics.findAll("a")[1]["href"]
#     print(mainwebpage + eachindividualpicsurls) #print https://innovateinfinitely.com/myphotoalbum/myphotoalbum/minihomegym.jpg
#     imageurl = mainwebpage + eachindividualpicsurls
#     #print(eachindividualpics.text) #print Exercise Mat, 45-Pound Plate, 25-Pound Plate
#     imagename = eachindividualpics.text + ".jpg"
#     downloadimages(imagename, imageurl)
# finish = time.perf_counter()
# print(f"Finished in {round(finish-start,2)} second(s).") #print Finished in 148.51 second(s).

#yes threading
import concurrent.futures
def downloadimages(imageurl):
    imagename = imageurl[57:]
    print(imagename) #print minihomegym.jpg
    with open(imagename, "wb") as imagefile:   #wb is write bytes
        imagefile.write(urlopen(imageurl).read())
    #time.sleep(3)


imageurllist = []
individualpics = soup.findAll("td", {"id": "picture"})
for eachindividualpics in individualpics:
    #print(eachindividualpics.findAll("a")[1]) #print <a href="myphotoalbum/myphotoalbum/minihomegym.jpg">Exercise Mat, 45-Pound Plate, 25-Pound Plate</a>
    eachindividualpicsurls = eachindividualpics.findAll("a")[1]["href"]
    #print(mainwebpage + eachindividualpicsurls) #print https://innovateinfinitely.com/myphotoalbum/myphotoalbum/minihomegym.jpg
    imageurl = mainwebpage + eachindividualpicsurls
    imageurllist.append(imageurl)
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(downloadimages, imageurllist)
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).") #print Finished in 18.94 second(s).  RM:  without time.sleep(3) is 4.05 second(s).

