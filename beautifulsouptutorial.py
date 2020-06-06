#Beautiful Soup Tutorial - Web Scraping in Python LucidProgramming
import requests
from bs4 import BeautifulSoup
#The requests module we use the get function to provide access to webpages
result = requests.get("https://www.innovateinfinitely.com")
#Check the webpage status code.  Status code 200 means webpage is good.
print(result.status_code) #print 200
#Webpage headers.  HTTP header information https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
#print(result.headers)
'''
{'Date': 'Sat, 23 May 2020 19:34:04 GMT', 'Server': 'Apache', 'Last-Modified': 'Wed, 29 Apr 2020 20:37:46 GMT', 'Accept-Ranges': 'bytes', 'Vary': 'Accept-Encoding,User-Agent', 'Content-Encoding': 'gzip', 'Content-Length': '2661', 'Keep-Alive': 'timeout=2, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html'}
'''
#print(type(result.headers)) #print <class 'requests.structures.CaseInsensitiveDict'>
#print(result.headers["Content-Type"]) #print text/html
#Extract the webpage content
webpagecontent = result.content
#print(webpagecontent)
'''
b'<!doctype html>\n<head>\n<link rel="stylesheet" type="text/css" href="csstemplate.css">\n<style type="text/css">\n</style>\n<meta charset="utf-8"/>\n<meta name="author" content="Raymond Mar">\n<meta name="description" content="Raymond Mar\'s Innovate Infinitely (ININ) Home Page, the web site that never stops innovating.">\n<meta name="keywords" content="Innovate Infinitely, Innovation, Never Stop Innovating, Infinite, Infinity, Innovate,  Favorite Quotes, Cooking 101, About Raymond Mar, About ININ, About Innovate Infinitely, Blog, Web Log">\n<meta name="pastmodifieddate" content="October 25, 2016">\n<meta name="pastmodifieddate" content="February 28, 2017">\n<meta name="pastmodifieddate" content="September 23, 2017">\n<meta name="pastmodifieddate" content="March 31, 2019"> . . . 
'''
#Use BeautifulSoup to parse and process the webpage content.  Create a BeautifulSoup object.
soup = BeautifulSoup(webpagecontent,"lxml")
#Access information from BeautifulSoup object variable soup.  List all links using findAll() method.
links = soup.findAll("a")
#print(links)
'''
[<a href="index.html">Innovate Infinitely</a>, <a href="favoritequotes.html">Favorite Quotes</a>, <a href="myphotoalbum.html">My Photo Album</a>, <a href="policecarphotoalbum.html">Police Car Photo Album</a>, . . .
'''
#print(type(links)) #print <class 'bs4.element.ResultSet'>
#Extract each link
# for eachlinks in links:
# 	print(eachlinks)
'''
	<a href="index.html">Innovate Infinitely</a>
	<a href="favoritequotes.html">Favorite Quotes</a>
	<a href="myphotoalbum.html">My Photo Album</a>
	<a href="policecarphotoalbum.html">Police Car Photo Album</a> . . .
'''
#Extract link containing text About.  Use the built-in text function to access the text between the <a> tags.  Case sensitive.
for eachlinks in links:
	if ("About" or "about") in eachlinks.text:
		print(eachlinks) #print <a href="aboutme.html">About Me</a>
		print(eachlinks.attrs['href']) #print aboutme.html
#Exercise.  Extract links from White House Briefings & Statements.  The links are enclosed in h2 tags class name is briefing-statement__title.  Export to a list.
exercise = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = exercise.content
soup = BeautifulSoup(src,"lxml")
linklist = []
#findAll returns a list all tags in the page.  find returns first tag in the page.
for h2tag in soup.findAll("h2",{"class":"briefing-statement__title"}):
	print(h2tag) #print <h2 class="briefing-statement__title"><a href="https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/">Presidential Message on Eid al-Fitr, 2020</a></h2>
	atag = h2tag.find("a")
	print(atag) #print <a href="https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/">Presidential Message on Eid al-Fitr, 2020</a>
	print(atag.attrs["href"]) #print https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/
	print(atag.text) #print Presidential Message on Eid al-Fitr, 2020
	linklist.append(atag.attrs["href"])
print(linklist) #print ['https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/', 'https://www.whitehouse.gov/briefings-statements/remarks-president-trump-rolling-remember-ceremony-honoring-nations-veterans-pow-mia/', 'https://www.whitehouse.gov/briefings-statements/remarks-president-trump-ford-rawsonville-components-plant/', . . . ]
htmldocument = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""
with open('index.html', 'w') as file:
    file.write(htmldocument)
#soup = BeautifulSoup(htmldocument, "lxml")
soup = BeautifulSoup(htmldocument, "lxml")
#Print the webpage in a readable format
#print(soup.prettify())
'''
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b> . . .
'''
#Find the first bold tag
print(soup.b) #print <b>The Dormouse's story</b>
#Find the first paragraph tag
print(soup.p) #print <p class="title"><b>The Dormouse's story</b></p>
#Find the first bold tag using the find funciton
print(soup.find("b")) #print <b>The Dormouse's story</b>
print(type(soup.find("b"))) #print <class 'bs4.element.Tag'>
#Find all bold tag using the findAll funciton which is a list
print(soup.findAll("b")) #print [<b>The Dormouse's story</b>, <b class="boldest">Extremely bold</b>, <b id="1">Test 1</b>, <b another-attribute="1" id="verybold">Test 2</b>]
print(type(soup.findAll("b"))) #print <class 'bs4.element.ResultSet'>
print(soup.findAll("b")[2]) #print <b id="1">Test 1</b>
#The name property gives the tag name
print(soup.b.name) #print b
print(soup.p.name) #print p
#We can alter the tag name and reflect the alteration in the source
tag = soup.b
print(tag) #print <b>The Dormouse's story</b>
tag.name = "Give the tag another name blockquote"
print(tag) #print <Give the tag another name blockquote>The Dormouse's story</Give the tag another name blockquote>
tag.name = "b"  #RM:  Replace altered tag with correct tag <b>
print(tag) #print <b>The Dormouse's story</b>
gethtmlattribute = soup.findAll("b")[3]
print(gethtmlattribute) #print <b another-attribute="1" id="verybold">Test 2</b>
print(gethtmlattribute["id"]) #print verybold
print(gethtmlattribute["another-attribute"]) #print 1
getallhtmlattributes = soup.findAll("b")[3]
print(getallhtmlattributes.attrs) #print {'another-attribute': '1', 'id': 'verybold'}
print(getallhtmlattributes.attrs["id"]) #print verybold
getallhtmlattributes["another-attribute"] = "alter attribute name because mutable"
print(getallhtmlattributes["another-attribute"]) #print alter attribute name because mutable
print(getallhtmlattributes) #print <b another-attribute="alter attribute name because mutable" id="verybold">Test 2</b>
#del command for lists to remove attributes
del getallhtmlattributes["id"]
print(getallhtmlattributes) #print <b another-attribute="alter attribute name because mutable">Test 2</b>
gettagstring = soup.findAll("b")[1]
print(gettagstring) #print <b class="boldest">Extremely bold</b>
print(gettagstring.string) #print Extremely bold
print(gettagstring.text) #print Extremely bold
gettagstring.string.replace_with("Replace original string with another string")
print(gettagstring.string) #print Replace original string with another string
gettagstring.string.replace_with("Replace original string with another text printing with .text")
print(gettagstring.text) #print Replace original text with another text
print(gettagstring) #print <b class="boldest">Replace original string with another text printing with .text</b>

#Web scraping and parsing with Beautiful Soup _ Python Introduction p.1
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = BeautifulSoup(sauce,"lxml")
print(soup.title) #print <title>Python Programming Tutorials</title>
print(soup.title.name) #print title
print(soup.title.string) #print Python Programming Tutorials
print(soup.title.text) #print Python Programming Tutorials
print(soup.p)
'''
<p class="introduction">Oh, hello! This is a <span style="font-size:115%">wonderful</span> page meant to let you practice web scraping. This page was originally created to help people work with the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="blank"><strong>Beautiful Soup 4</strong></a> library.</p>
'''
# print(soup.findAll("p"))
'''
[<p class="introduction">Oh, hello! This is a <span style="font-size:115%">wonderful</span> page meant to let you practice web scraping. This page was originally created to help people work with the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="blank"><strong>Beautiful Soup 4</strong></a> library.</p>, <p>The following table gives some general information for the following <code>programming languages</code>:</p>, <p>I think it's clear that, on a scale of 1-10, python is:</p>, <p>Javascript (dynamic data) test:</p>, <p class="jstest" id="yesnojs">y u bad tho?</p>, <p>Whᶐt hαppéns now¿</p>, <p><a href="/sitemap.xml" target="blank"><strong>sitemap</strong></a></p>, <p class="grey-text text-lighten-4">Contact: Harrison@pythonprogramming.net.</p>, <p class="grey-text right" style="padding-right:10px">Programming is a superpower.</p>]
'''
for eachparagraph in soup.findAll("p"):
	print(eachparagraph)
	'''
	<p class="introduction">Oh, hello! This is a <span style="font-size:115%">wonderful</span> page meant to let you practice web scraping. This page was originally created to help people work with the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="blank"><strong>Beautiful Soup 4</strong></a> library.</p>
	'''
	print(eachparagraph.text) #print Oh, hello! This is a wonderful page meant to let you practice web scraping. This page was originally created to help people work with the Beautiful Soup 4 library.
for eachparagraph in soup.findAll("p"):
	print(eachparagraph.string) #print None #RM:  .string works if eachparagraph doesn't have child html tags or html tags inside <p>
#print(soup.get_text()) #all the text only in the webpage
for eachurl in soup.findAll("a"):
	print(eachurl)
	print(eachurl.text)
	print(eachurl.get("href"))
	'''
	<a class="brand-logo" href="/"><img class="img-responsive" src="/static/images/mainlogowhitethick.jpg" style="width:50px; height;50px; margin-top:5px"/></a>
	
	/
	...
	<a class="grey-text text-lighten-3" href="/support-donate/">Support this Website!</a>
	Support this Website!
	/support-donate/
	...
	<a href="https://xkcd.com/353/" target="blank"><p class="grey-text right" style="padding-right:10px">Programming is a superpower.</p></a>
	Programming is a superpower.
	https://xkcd.com/353/
	'''

#Navigating Tags - Web scraping with Beautiful Soup 4 p.2
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = BeautifulSoup(sauce,"lxml")
navigationpage = soup.nav
#print(navigationpage)
'''
<nav style="background-color:#003F72">
<div class="nav-wrapper container">
<a class="brand-logo" href="/"><img class="img-responsive" src="/static/images/mainlogowhitethick.jpg" style="width:50px; height;50px; margin-top:5px"/></a>
<a class="button-collapse" data-activates="navsidebar" href="#"><i class="mdi-navigation-menu"></i></a> . . . 
'''
for navigationurls in navigationpage.findAll("a"):
	print(navigationurls.get("href"))
	'''
	/
	#
	/
	/+=1/
	'''
bodycontent = soup.body
for paragraphtags in bodycontent.findAll("p"):
	print(paragraphtags.text) #print Oh, hello! This is a wonderful page meant to let you practice web scraping. This page was originally created to help people work with the Beautiful Soup 4 library. . . .
for divtags in soup.findAll("div"):
	print(divtags.text)
	'''
	Oh, hello! This is a wonderful page meant to let you practice web scraping. This page was originally created to help people work with the Beautiful Soup 4 library.
	The following table gives some general information for the following programming languages:

	Python
	Pascal
	Lisp
	D#
	Cobol
	Fortran
	Haskell
	'''
for divtagsbody in soup.findAll("div", class_="body"):
	print(divtagsbody.text)
	'''
	Oh, hello! This is a wonderful page meant to let you practice web scraping. This page was originally created to help people work with the Beautiful Soup 4 library.
	The following table gives some general information for the following programming languages:

	Python
	Pascal
	Lisp
	D#
	Cobol
	Fortran
	Haskell
	'''
for divtagsbody in soup.findAll("div",{"class":"body"}):
	print(divtagsbody)
	'''
	<div class="body">
	<p class="introduction">Oh, hello! This is a <span style="font-size:115%">wonderful</span> page meant to let you practice web scraping. This page was originally created to help people work with the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="blank"><strong>Beautiful Soup 4</strong></a> library.</p>
	<p>The following table gives some general information for the following <code>programming languages</code>:</p>
	<ul>
	<li>Python</li>
	<li>Pascal</li>
	<li>Lisp</li>
	<li>D#</li>
	<li>Cobol</li>
	<li>Fortran</li>
	<li>Haskell</li>
	'''
for divtagsbody in soup.findAll("div",{"class":"body"}):
	for eachul in divtagsbody.findAll("ul"):
		printli = eachul.findAll("li")
		print(printli) #print [<li>Python</li>, <li>Pascal</li>, <li>Lisp</li>, <li>D#</li>, <li>Cobol</li>, <li>Fortran</li>, <li>Haskell</li>]
		for eachprintli in printli:
			print(eachprintli) #print <li>Python</li>
			print(eachprintli.text) #print Python

#Tables and XML - Web scraping with Beautiful Soup 4 p.3
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = BeautifulSoup(sauce,"lxml")
completetablesouptable = soup.table
print(completetablesouptable)
'''
<table style="width:100%">
<tr>
<th>Program Name</th>
<th>Internet Points</th>
<th>Kittens?</th>
</tr>
<tr>
<td>Python</td>
<td>932914021</td>
<td>Definitely</td>
</tr>
<tr>
<td>Pascal</td>
<td>532</td>
<td>Unlikely</td>
</tr>
<tr>
<td>Lisp</td>
<td>1522</td>
<td>Uncertain</td>
</tr>
<tr>
<td>D#</td>
<td>12</td>
<td>Possibly</td>
</tr>
<tr>
<td>Cobol</td>
<td>3</td>
<td>No.</td>
</tr>
<tr>
<td>Fortran</td>
<td>52124</td>
<td>Yes.</td>
</tr>
<tr>
<td>Haskell</td>
<td>24</td>
<td>lol.</td>
</tr>
</table>
'''
completetable = soup.find("table")
print(completetable)
'''
<table style="width:100%">
<tr>
<th>Program Name</th>
<th>Internet Points</th>
<th>Kittens?</th>
</tr>
<tr>
<td>Python</td>
<td>932914021</td>
<td>Definitely</td>
</tr>
<tr>
<td>Pascal</td>
<td>532</td>
<td>Unlikely</td>
</tr>
<tr>
<td>Lisp</td>
<td>1522</td>
<td>Uncertain</td>
</tr>
<tr>
<td>D#</td>
<td>12</td>
<td>Possibly</td>
</tr>
<tr>
<td>Cobol</td>
<td>3</td>
<td>No.</td>
</tr>
<tr>
<td>Fortran</td>
<td>52124</td>
<td>Yes.</td>
</tr>
<tr>
<td>Haskell</td>
<td>24</td>
<td>lol.</td>
</tr>
</table>
'''
tablerows = completetable.findAll("tr")
for eachtr in tablerows:
	tabledata = eachtr.findAll("td")
	arow = [eachtabledata.text for eachtabledata in tabledata]
	print(arow)
	'''
	[]
	['Python', '932914021', 'Definitely']
	['Pascal', '532', 'Unlikely']
	['Lisp', '1522', 'Uncertain']
	['D#', '12', 'Possibly']
	['Cobol', '3', 'No.']
	['Fortran', '52124', 'Yes.']
	['Haskell', '24', 'lol.']
	'''
saucexml = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
soup = BeautifulSoup(saucexml,"xml")
#print(soup)
'''
<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
<loc>https://pythonprogramming.net/downloads/intraQuarter.zip/</loc>
<lastmod>2020-05-24</lastmod>
</url>
<url>
<loc>https://pythonprogramming.net/downloads/knowledgeBase.db</loc>
<lastmod>2020-05-24</lastmod>
</url>
<url>
<loc>https://pythonprogramming.net/downloads/key_stats.csv</loc>
<lastmod>2020-05-24</lastmod>
</url>
<url>
<loc>https://pythonprogramming.net/downloads/style.zip</loc>
<lastmod>2020-05-24</lastmod>
</url>
...
<url>
<loc>https://pythonprogramming.net/go/</loc>
<lastmod>2020-05-24</lastmod>
</url>
<url>
<loc>https://pythonprogramming.net/</loc>
<lastmod>2020-05-24</lastmod>
</url>
</urlset>
'''
for url in soup.findAll("loc"):
	print(url.text)
	'''
	https://pythonprogramming.net/downloads/intraQuarter.zip/
	https://pythonprogramming.net/downloads/knowledgeBase.db
	https://pythonprogramming.net/downloads/key_stats.csv
	https://pythonprogramming.net/downloads/style.zip
	...
	https://pythonprogramming.net/qe/
	https://pythonprogramming.net/go/
	https://pythonprogramming.net/
	'''

#Dynamic Javascript Scraping - Web scraping with Beautiful Soup 4 p.4
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
soup = BeautifulSoup(sauce,"lxml")
javascripttest = soup.find("p", class_="jstest")
print(javascripttest.text) #print y u bad tho?  Website displays Look at you shinin!

#20 - web scraping with python using beautiful soup _ requests (Python tutorial for beginners 2019)
import requests
from bs4 import BeautifulSoup
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=36.97493920000005&lon=-121.90341819999998")
soup = BeautifulSoup(page.content, "html.parser")
#print(soup)
'''
<!DOCTYPE html>

<html class="no-js">
<head>
<!-- Meta -->
<meta content="width=device-width" name="viewport"/>
<link href="http://purl.org/dc/elements/1.1/" rel="schema.DC"/><title>National Weather Service</title><meta content="National Weather Service" name="DC.title"><meta content="NOAA National Weather Service National Weather Service" name="DC.description"/><meta content="US Department of Commerce, NOAA, National Weather Service" name="DC.creator"/><meta content="" name="DC.date.created" scheme="ISO8601"/><meta content="EN-US" name="DC.language" scheme="DCTERMS.RFC1766"/><meta content="weather, National Weather Service" name="DC.keywords"/><meta content="NOAA's National Weather Service" name="DC.publisher"/><meta content="National Weather Service" name="DC.contributor"/><meta content="http://www.weather.gov/disclaimer.php" name="DC.rights"/><meta content="General" name="rating"/><meta content="index,follow" name="robots"/>
<!-- Icons -->
<link href="./images/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
<!-- CSS -->
<link href="css/bootstrap-3.2.0.min.css" rel="stylesheet"/>
<link href="css/bootstrap-theme-3.2.0.min.css" rel="stylesheet"/>
<link href="css/font-awesome-4.3.0.min.css" rel="stylesheet"/>
<link href="css/ol-4.6.4.css" rel="stylesheet" type="text/css"/>
<link href="css/mapclick.css" rel="stylesheet" type="text/css">
'''
weekweather = soup.find(id="seven-day-forecast-body")
#print(weekweather)
'''
<div class="panel-body" id="seven-day-forecast-body">
<div id="seven-day-forecast-container"><ul class="list-unstyled" id="seven-day-forecast-list"><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Tonight<br/><br/></p>
<p><img alt="Tonight: Increasing clouds, with a low around 57. South southwest wind 9 to 14 mph becoming light and variable  in the evening. Winds could gust as high as 18 mph. " class="forecast-icon" src="newimages/medium/nbkn.png" title="Tonight: Increasing clouds, with a low around 57. South southwest wind 9 to 14 mph becoming light and variable  in the evening. Winds could gust as high as 18 mph. "/></p><p class="short-desc">Increasing<br/>Clouds</p><p class="temp temp-low">Low: 57 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Sunday<br/><br/></p>
<p><img alt="Sunday: Mostly cloudy, with a high near 75. Calm wind becoming north northwest around 6 mph in the afternoon. " class="forecast-icon" src="newimages/medium/bkn.png" title="Sunday: Mostly cloudy, with a high near 75. Calm wind becoming north northwest around 6 mph in the afternoon. "/></p><p class="short-desc">Mostly Cloudy</p><p class="temp temp-high">High: 75 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Sunday<br/>Night</p>
<p><img alt="Sunday Night: Mostly cloudy, with a low around 56. North northwest wind around 6 mph becoming calm  in the evening. " class="forecast-icon" src="newimages/medium/nbkn.png" title="Sunday Night: Mostly cloudy, with a low around 56. North northwest wind around 6 mph becoming calm  in the evening. "/></p><p class="short-desc">Mostly Cloudy</p><p class="temp temp-low">Low: 56 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Monday<br/><br/></p>
...
'''
#print(weekweather.findAll("li"))
'''
[<li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Tonight<br/><br/></p>
<p><img alt="Tonight: Increasing clouds, with a low around 57. South southwest wind 9 to 14 mph becoming light and variable  in the evening. Winds could gust as high as 18 mph. " class="forecast-icon" src="newimages/medium/nbkn.png" title="Tonight: Increasing clouds, with a low around 57. South southwest wind 9 to 14 mph becoming light and variable  in the evening. Winds could gust as high as 18 mph. "/></p><p class="short-desc">Increasing<br/>Clouds</p><p class="temp temp-low">Low: 57 °F</p></div></li>, <li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Sunday<br/><br/></p>
<p><img alt="Sunday: Mostly cloudy, with a high near 75. Calm wind becoming north northwest around 6 mph in the afternoon. " class="forecast-icon" src="newimages/medium/bkn.png" title="Sunday: Mostly cloudy, with a high near 75. Calm wind becoming north northwest around 6 mph in the afternoon. "/></p><p class="short-desc">Mostly Cloudy</p><p class="temp temp-high">High: 75 °F</p></div></li>, <li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Sunday<br/>Night</p>
<p><img alt="Sunday Night: Mostly cloudy, with a low around 56. North northwest wind around 6 mph becoming calm  in the evening. " class="forecast-icon" src="newimages/medium/nbkn.png" title="Sunday Night: Mostly cloudy, with a low around 56. North northwest wind around 6 mph becoming calm  in the evening. "/></p><p class="short-desc">Mostly Cloudy</p><p class="temp temp-low">Low: 56 °F</p></div></li>, <li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Monday<br/><br/></p>
...
'''
#print(weekweather.findAll(class_="tombstone-container"))
'''
[<div class="tombstone-container">
<p class="period-name">Tonight<br/><br/></p>
<p><img alt="Tonight: Increasing clouds, with a low around 57. South southwest wind 9 to 14 mph becoming light and variable  in the evening. Winds could gust as high as 18 mph. " class="forecast-icon" src="newimages/medium/nbkn.png" title="Tonight: Increasing clouds, with a low around 57. South southwest wind 9 to 14 mph becoming light and variable  in the evening. Winds could gust as high as 18 mph. "/></p><p class="short-desc">Increasing<br/>Clouds</p><p class="temp temp-low">Low: 57 °F</p></div>, <div class="tombstone-container">
<p class="period-name">Sunday<br/><br/></p>
<p><img alt="Sunday: Mostly cloudy, with a high near 75. Calm wind becoming north northwest around 6 mph in the afternoon. " class="forecast-icon" src="newimages/medium/bkn.png" title="Sunday: Mostly cloudy, with a high near 75. Calm wind becoming north northwest around 6 mph in the afternoon. "/></p><p class="short-desc">Mostly Cloudy</p><p class="temp temp-high">High: 75 °F</p></div>, <div class="tombstone-container">
<p class="period-name">Sunday<br/>Night</p>
<p><img alt="Sunday Night: Mostly cloudy, with a low around 56. North northwest wind around 6 mph becoming calm  in the evening. " class="forecast-icon" src="newimages/medium/nbkn.png" title="Sunday Night: Mostly cloudy, with a low around 56. North northwest wind around 6 mph becoming calm  in the evening. "/></p><p class="short-desc">Mostly Cloudy</p><p class="temp temp-low">Low: 56 °F</p></div>, <div class="tombstone-container">
<p class="period-name">Monday<br/><br/></p>
...
'''
dailytemperatures = weekweather.findAll(class_="tombstone-container")
#print(type(dailytemperatures)) #print <class 'bs4.element.ResultSet'>  #RM:  It's a list.  Notice the comma after the tombstone-container
print(dailytemperatures[0].find(class_="period-name").get_text()) #print Low: Tonight
print(dailytemperatures[0].find(class_="short-desc").get_text()) #print IncreasingClouds
print(dailytemperatures[0].find(class_="temp").get_text()) #print Low: 57 F
#for eachdailytemperatures in dailytemperatures.findAll(class_="period-name"):
#	print(eachdailytemperatures) #print AttributeError: ResultSet object has no attribute 'findAll'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
for eachdailytemperatures in dailytemperatures:
	print(eachdailytemperatures.find(class_="period-name").get_text())
	print(eachdailytemperatures.find(class_="short-desc").text)
	print(eachdailytemperatures.find(class_="temp").get_text())
	print(eachdailytemperatures.find(class_="period-name").get_text(),"\t",eachdailytemperatures.find(class_="short-desc").text,"\t",eachdailytemperatures.find(class_="temp").get_text()) #print Tonight 	 IncreasingClouds 	 Low: 57 °F
	linetemperature = eachdailytemperatures.find(class_="period-name").get_text(),",",eachdailytemperatures.find(class_="short-desc").text,",",eachdailytemperatures.find(class_="temp").get_text()
	print(linetemperature) #print ('Tonight', ',', 'IncreasingClouds', ',', 'Low: 57 °F')  #RM:  saves a tuple.
	#Write each data point separately ending with a comma and a new line \n as a csv text file.
	with open("csvtext.txt","a") as fileobject:
		fileobject.write(eachdailytemperatures.find(class_="period-name").get_text()+",")
		fileobject.write(eachdailytemperatures.find(class_="short-desc").text+",")
		fileobject.write(eachdailytemperatures.find(class_="temp").get_text()+"\n")