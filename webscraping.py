#Introduction to Web Scraping (Python) - Lesson 01 (BeautifulSoup, Twitter)
import urllib
import urllib.request
from bs4 import BeautifulSoup

webpageurl = "https://twitter.com/realDonaldTrump"
page = urllib.request.urlopen(webpageurl)
soup = BeautifulSoup(page,"html.parser")
print(soup.title) #print <title>Donald J. Trump (@realDonaldTrump) | Twitter</title>  RM:  search in Inspect <title>.  See the title Donald J. Trump (@realDonaldTrump) | Twitter between the <title> tags 
print(soup.title.text) #print Donald J. Trump (@realDonaldTrump) | Twitter
#print(soup.findAll("a")) #print [<a class="u-hiddenVisually focusable" href="#timeline">Skip to content</a>, <a class="js-nav js-tooltip js-dynamic-tooltip" data-component-context="home_nav" data-nav="home" data-placement="bottom" href="/"><span class="Icon Icon--bird Icon--large"></span><span aria-hidden="true" class="text">Home</span> . . .
#for eacha in soup.findAll("a"):
	#print(eacha.get("href")) #print #timeline\n /\n /i/moments\n . . .
	#print(eacha.text) #print Skip to content\n . . .
#Write Beautiful Soup to a .json file https://stackoverflow.com/questions/40529848/how-to-write-the-output-to-html-file-with-python-beautifulsoup.  Write Beautiful Soup to .html file works, too.  .html is better.
# filewrite = open("tempdelete.json","w")
# filewrite.write(str(soup))
# filewrite.close()
print(soup.find("p",{"class":"ProfileHeaderCard-bio u-dir"}).text) #print 45th President of the United States of America  #RM:  found the HTML code by writing the soup as a json string file and finding 45th President of the United States of America.
#RM found the HTML code by writing the soup as a HTML string file and finding 45th President of the United States of America.
#print(soup.find("div",{"class":"ProfileHeaderCard"})) #print <div class="ProfileHeaderCard">\n <h1 class="ProfileHeaderCard-name"> . . .
print(soup.find("div",{"class":"ProfileHeaderCard"}).find("p").text) #45th President of the United States of America
#print(soup.find("div",{"class":"ProfileHeaderCard"}).find("p",{"class":"ProfileHeaderCard-bio u-dir"})) #print <p class="ProfileHeaderCard-bio u-dir" dir="ltr">45th President of the United States of America<img alt="🇺🇸" aria-label="Emoji: Flag of United States" class="Emoji Emoji--forText" draggable="false" src="https://abs.twimg.com/emoji/v2/72x72/1f1fa-1f1f8.png" title="Flag of United States"/></p>
print(soup.find("div",{"class":"ProfileHeaderCard"}).find("p",{"class":"ProfileHeaderCard-bio u-dir"}).text) #45th President of the United States of America
for alltweets in soup.findAll("p",{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
	print(alltweets.text,end="\n\n")
	'''
	Had a great call with Catholic Leaders and Educators earlier today. I will be online tomorrow at 10:15 A.M. (Eastern) for Sunday Mass celebrated by @CardinalDolan at St. Patrick’s Cathedral (@StPatsNYC) in New York City. Join me: https://saintpatrickscathedral.org/live pic.twitter.com/iQy5iH5Lk6

	I never said the pandemic was a Hoax! Who would say such a thing? I said that the Do Nothing Democrats, together with their Mainstream Media partners, are the Hoax. They have been called out & embarrassed on this, even admitting they were wrong, but continue to spread the lie!
	...
	'''

#Intro to Web Scraping with Python and Beautiful Soup
from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as soup
myurl = "https://www.newegg.com/p/pl?d=graphics+cards"
#opening up connecting, grap the webpage
uClient = uRequest(myurl)
rawhtml = uClient.read()
#closing connection
uClient.close()
#html parse or the html code for the webpage
htmlparsed = soup(rawhtml, "html.parser")
print(htmlparsed.h1) #print <h1 class="page-title-text">"graphics cards"</h1>
print(htmlparsed.p) #print <p>Newegg.com - A great place to buy computers, computer parts, electronics, software, accessories, and DVDs online. With great prices, fast shipping, and top-rated customer service - Newegg shopping upgraded ™</p>
#instructor says inspect website's html code and its elements
#print(htmlparsed.body) #prints all the body
print(htmlparsed.body.span) #print <span class="noCSS">Skip to:</span>
#instructor found the div class named item-container which has the html code for one of the graphics card and its complete information.  I saved a sample of the div class named item-container in file name /home/mar/python/divclassitemcontainersample.html
classcontainer = htmlparsed.findAll("div",{"class":"item-container"})
print(len(classcontainer)) #print 41.  The 41 includes the four graphics cards under "You May Also Be Interested In:"
print(type(classcontainer[0].div)) #print <class 'bs4.element.Tag'>
print(classcontainer[0])
'''
<div class="item-container" data-itemnumber="20-231-941">
<a class="item-img" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards">
<img alt="G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB" src="//c1.neweggimages.com/ProductImageCompressAll300/20-231-941-03.jpg" title="G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB"/>
</a>
<div class="item-info">
<div class="item-branding">
<a class="item-rating" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards&amp;IsFeedbackTab=true#scrollFullInfo"><i class="rating rating-4"></i><span class="item-rating-num">(245)</span></a>
</div>
<a class="item-title" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards">
                            
                            G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 256...
                        </a>
</div>
</div>
'''
#instructor in the tutorial picked the graphics cards with all consistent information; otherwise, if else or try except are required such as some graphics cards don't have a price and don't have a review.
print(classcontainer[0].a)
'''
<a class="item-img" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards">
<img alt="G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB" src="//c1.neweggimages.com/ProductImageCompressAll300/20-231-941-03.jpg" title="G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB"/>
</a>
'''
print(classcontainer[0].div)
'''
<div class="item-info">
<div class="item-branding">
<a class="item-rating" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards&amp;IsFeedbackTab=true#scrollFullInfo"><i class="rating rating-4"></i><span class="item-rating-num">(245)</span></a>
</div>
<a class="item-title" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards">
                            
                            G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 256...
                        </a>
</div>
'''
print(classcontainer[0].div.div)
'''
<div class="item-branding">
<a class="item-rating" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards&amp;IsFeedbackTab=true#scrollFullInfo"><i class="rating rating-4"></i><span class="item-rating-num">(245)</span></a>
</div>
'''
print(classcontainer[0].div.div.a)
'''
<a class="item-rating" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards&amp;IsFeedbackTab=true#scrollFullInfo"><i class="rating rating-4"></i><span class="item-rating-num">(245)</span></a>
'''
print(classcontainer[0].img)
'''
<img alt="G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB" src="//c1.neweggimages.com/ProductImageCompressAll300/20-231-941-03.jpg" title="G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB"/>
'''
print(classcontainer[0].img["title"])
'''
G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB
'''
print(classcontainer[0].a.img["title"])
'''
G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16D-16GVKB
'''
print("\n")
print(classcontainer[0].findAll("a",{"class":"item-title"}))
'''
[<a class="item-title" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards">
                            
                            G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 256...
                        </a>]
'''
print(classcontainer[0].findAll("a",{"class":"item-title"})[0].text) #print G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 256...
print(classcontainer.findAll("li",{"class":"price-ship"}))



classbranding = htmlparsed.findAll("div",{"class":"item-branding"}.text)
print(classbranding[0])
'''
<div class="item-branding">
<a class="item-rating" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards&amp;IsFeedbackTab=true#scrollFullInfo"><i class="rating rating-4"></i><span class="item-rating-num">(245)</span></a>
</div>
'''

for eachclasscontainer in classcontainer:
	#brand = eachclasscontainer.a.img["title"]
	titlecontainer = eachclasscontainer.findAll("a",{"class":"item-title"})[0].text