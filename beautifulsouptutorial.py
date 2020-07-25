# Beautiful Soup Tutorial - Web Scraping in Python LucidProgramming
import requests
from bs4 import BeautifulSoup
# The requests module we use the get function to provide access to webpages
result = requests.get("https://www.innovateinfinitely.com")
# Check the webpage status code.  Status code 200 means webpage is good.
print(result.status_code)  # print 200
# Webpage headers.  HTTP header information https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
# print(result.headers)
'''
{'Date': 'Sat, 23 May 2020 19:34:04 GMT', 'Server': 'Apache', 'Last-Modified': 'Wed, 29 Apr 2020 20:37:46 GMT', 'Accept-Ranges': 'bytes', 'Vary': 'Accept-Encoding,User-Agent', 'Content-Encoding': 'gzip', 'Content-Length': '2661', 'Keep-Alive': 'timeout=2, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html'}
'''
# print(type(result.headers)) #print <class 'requests.structures.CaseInsensitiveDict'>
# print(result.headers["Content-Type"]) #print text/html
# Extract the webpage content
webpagecontent = result.content
# print(webpagecontent)
'''
b'<!doctype html>\n<head>\n<link rel="stylesheet" type="text/css" href="csstemplate.css">\n<style type="text/css">\n</style>\n<meta charset="utf-8"/>\n<meta name="author" content="Raymond Mar">\n<meta name="description" content="Raymond Mar\'s Innovate Infinitely (ININ) Home Page, the web site that never stops innovating.">\n<meta name="keywords" content="Innovate Infinitely, Innovation, Never Stop Innovating, Infinite, Infinity, Innovate,  Favorite Quotes, Cooking 101, About Raymond Mar, About ININ, About Innovate Infinitely, Blog, Web Log">\n<meta name="pastmodifieddate" content="October 25, 2016">\n<meta name="pastmodifieddate" content="February 28, 2017">\n<meta name="pastmodifieddate" content="September 23, 2017">\n<meta name="pastmodifieddate" content="March 31, 2019"> . . . 
'''
# Use BeautifulSoup to parse and process the webpage content.  Create a BeautifulSoup object.
soup = BeautifulSoup(webpagecontent, "lxml")
# Access information from BeautifulSoup object variable soup.  List all links using findAll() method.
links = soup.findAll("a")
# print(links)
'''
[<a href="index.html">Innovate Infinitely</a>, <a href="favoritequotes.html">Favorite Quotes</a>, <a href="myphotoalbum.html">My Photo Album</a>, <a href="policecarphotoalbum.html">Police Car Photo Album</a>, . . .
'''
# print(type(links)) #print <class 'bs4.element.ResultSet'>
# Extract each link
# for eachlinks in links:
# 	print(eachlinks)
'''
	<a href="index.html">Innovate Infinitely</a>
	<a href="favoritequotes.html">Favorite Quotes</a>
	<a href="myphotoalbum.html">My Photo Album</a>
	<a href="policecarphotoalbum.html">Police Car Photo Album</a> . . .
'''
# Extract link containing text About.  Use the built-in text function to access the text between the <a> tags.  Case sensitive.
for eachlinks in links:
    if ("About" or "about") in eachlinks.text:
        print(eachlinks)  # print <a href="aboutme.html">About Me</a>
        print(eachlinks.attrs['href'])  # print aboutme.html
# Exercise.  Extract links from White House Briefings & Statements.  The links are enclosed in h2 tags class name is briefing-statement__title.  Export to a list.
exercise = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = exercise.content
soup = BeautifulSoup(src, "lxml")
linklist = []
# findAll returns a list all tags in the page.  find returns first tag in the page.
for h2tag in soup.findAll("h2", {"class": "briefing-statement__title"}):
    print(h2tag)  # print <h2 class="briefing-statement__title"><a href="https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/">Presidential Message on Eid al-Fitr, 2020</a></h2>
    atag = h2tag.find("a")
    print(atag)  # print <a href="https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/">Presidential Message on Eid al-Fitr, 2020</a>
    print(atag.attrs["href"])  # print https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/
    print(atag.text)  # print Presidential Message on Eid al-Fitr, 2020
    linklist.append(atag.attrs["href"])
print(linklist)  # print ['https://www.whitehouse.gov/briefings-statements/presidential-message-eid-al-fitr-2020/', 'https://www.whitehouse.gov/briefings-statements/remarks-president-trump-rolling-remember-ceremony-honoring-nations-veterans-pow-mia/', 'https://www.whitehouse.gov/briefings-statements/remarks-president-trump-ford-rawsonville-components-plant/', . . . ]
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
# Print the webpage in a readable format
# print(soup.prettify())
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
# Find the first bold tag
print(soup.b)  # print <b>The Dormouse's story</b>
# Find the first paragraph tag
print(soup.p)  # print <p class="title"><b>The Dormouse's story</b></p>
# Find the first bold tag using the find funciton
print(soup.find("b"))  # print <b>The Dormouse's story</b>
print(type(soup.find("b")))  # print <class 'bs4.element.Tag'>
# Find all bold tag using the findAll funciton which is a list
print(soup.findAll("b"))  # print [<b>The Dormouse's story</b>, <b class="boldest">Extremely bold</b>, <b id="1">Test 1</b>, <b another-attribute="1" id="verybold">Test 2</b>]
print(type(soup.findAll("b")))  # print <class 'bs4.element.ResultSet'>
print(soup.findAll("b")[2])  # print <b id="1">Test 1</b>
# The name property gives the tag name
print(soup.b.name)  # print b
print(soup.p.name)  # print p
# We can alter the tag name and reflect the alteration in the source
tag = soup.b
print(tag)  # print <b>The Dormouse's story</b>
tag.name = "Give the tag another name blockquote"
print(tag)  # print <Give the tag another name blockquote>The Dormouse's story</Give the tag another name blockquote>
tag.name = "b"  # RM:  Replace altered tag with correct tag <b>
print(tag)  # print <b>The Dormouse's story</b>
gethtmlattribute = soup.findAll("b")[3]
print(gethtmlattribute)  # print <b another-attribute="1" id="verybold">Test 2</b>
print(gethtmlattribute["id"])  # print verybold
print(gethtmlattribute["another-attribute"])  # print 1
getallhtmlattributes = soup.findAll("b")[3]
print(getallhtmlattributes.attrs)  # print {'another-attribute': '1', 'id': 'verybold'}
print(getallhtmlattributes.attrs["id"])  # print verybold
getallhtmlattributes["another-attribute"] = "alter attribute name because mutable"
print(getallhtmlattributes["another-attribute"])  # print alter attribute name because mutable
print(getallhtmlattributes)  # print <b another-attribute="alter attribute name because mutable" id="verybold">Test 2</b>
# del command for lists to remove attributes
del getallhtmlattributes["id"]
print(getallhtmlattributes)  # print <b another-attribute="alter attribute name because mutable">Test 2</b>
gettagstring = soup.findAll("b")[1]
print(gettagstring)  # print <b class="boldest">Extremely bold</b>
print(gettagstring.string)  # print Extremely bold
print(gettagstring.text)  # print Extremely bold
gettagstring.string.replace_with("Replace original string with another string")
print(gettagstring.string)  # print Replace original string with another string
gettagstring.string.replace_with("Replace original string with another text printing with .text")
print(gettagstring.text)  # print Replace original text with another text
print(gettagstring)  # print <b class="boldest">Replace original string with another text printing with .text</b>

# Web scraping and parsing with Beautiful Soup _ Python Introduction p.1
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = BeautifulSoup(sauce, "lxml")
print(soup.title)  # print <title>Python Programming Tutorials</title>
print(soup.title.name)  # print title
print(soup.title.string)  # print Python Programming Tutorials
print(soup.title.text)  # print Python Programming Tutorials
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
    print(eachparagraph.text)  # print Oh, hello! This is a wonderful page meant to let you practice web scraping. This page was originally created to help people work with the Beautiful Soup 4 library.
for eachparagraph in soup.findAll("p"):
    print(eachparagraph.string)  # print None #RM:  .string works if eachparagraph doesn't have child html tags or html tags inside <p>
# print(soup.get_text()) #all the text only in the webpage
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

# Navigating Tags - Web scraping with Beautiful Soup 4 p.2
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = BeautifulSoup(sauce, "lxml")
navigationpage = soup.nav
# print(navigationpage)
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
    print(paragraphtags.text)  # print Oh, hello! This is a wonderful page meant to let you practice web scraping. This page was originally created to help people work with the Beautiful Soup 4 library. . . .
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
for divtagsbody in soup.findAll("div", {"class": "body"}):
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
for divtagsbody in soup.findAll("div", {"class": "body"}):
    for eachul in divtagsbody.findAll("ul"):
        printli = eachul.findAll("li")
        print(printli)  # print [<li>Python</li>, <li>Pascal</li>, <li>Lisp</li>, <li>D#</li>, <li>Cobol</li>, <li>Fortran</li>, <li>Haskell</li>]
        for eachprintli in printli:
            print(eachprintli)  # print <li>Python</li>
            print(eachprintli.text)  # print Python

# Tables and XML - Web scraping with Beautiful Soup 4 p.3
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = BeautifulSoup(sauce, "lxml")
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
soup = BeautifulSoup(saucexml, "xml")
# print(soup)
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

# Dynamic Javascript Scraping - Web scraping with Beautiful Soup 4 p.4
import urllib.request
from bs4 import BeautifulSoup
#sauce is source
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
soup = BeautifulSoup(sauce, "lxml")
javascripttest = soup.find("p", class_="jstest")
print(javascripttest.text)  # print y u bad tho?  Website displays Look at you shinin!

# 20 - web scraping with python using beautiful soup _ requests (Python tutorial for beginners 2019)
import requests
from bs4 import BeautifulSoup
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=36.97493920000005&lon=-121.90341819999998")
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
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
# print(weekweather)
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
# print(weekweather.findAll("li"))
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
# print(weekweather.findAll(class_="tombstone-container"))
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
# print(type(dailytemperatures)) #print <class 'bs4.element.ResultSet'>  #RM:  It's a list.  Notice the comma after the tombstone-container
print(dailytemperatures[0].find(class_="period-name").get_text())  # print Low: Tonight
print(dailytemperatures[0].find(class_="short-desc").get_text())  # print IncreasingClouds
print(dailytemperatures[0].find(class_="temp").get_text())  # print Low: 57 F
# for eachdailytemperatures in dailytemperatures.findAll(class_="period-name"):
#	print(eachdailytemperatures) #print AttributeError: ResultSet object has no attribute 'findAll'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
for eachdailytemperatures in dailytemperatures:
    print(eachdailytemperatures.find(class_="period-name").get_text())
    print(eachdailytemperatures.find(class_="short-desc").text)
    print(eachdailytemperatures.find(class_="temp").get_text())
    print(eachdailytemperatures.find(class_="period-name").get_text(), "\t", eachdailytemperatures.find(class_="short-desc").text, "\t", eachdailytemperatures.find(class_="temp").get_text())  # print Tonight 	 IncreasingClouds 	 Low: 57 °F
    linetemperature = eachdailytemperatures.find(class_="period-name").get_text(), ",", eachdailytemperatures.find(class_="short-desc").text, ",", eachdailytemperatures.find(class_="temp").get_text()
    print(linetemperature)  # print ('Tonight', ',', 'IncreasingClouds', ',', 'Low: 57 °F')  #RM:  saves a tuple.
    # Write each data point separately ending with a comma and a new line \n as a csv text file.
    with open("csvtext.txt", "a") as fileobject:
        fileobject.write(eachdailytemperatures.find(class_="period-name").get_text() + ",")
        fileobject.write(eachdailytemperatures.find(class_="short-desc").text + ",")
        fileobject.write(eachdailytemperatures.find(class_="temp").get_text() + "\n")

# Python Web Scraping with BeautifulSoup BS4 data mining
import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.usclimatedata.com/climate/united-states/us")
print(page)  # print <Response [200]>
print(type(page))  # print <class 'requests.models.Response'>
print(str(page) == "<Response [200]>")  # print True
# print(page.text) #RM:  print the webpage html
soup = BeautifulSoup(page.text, "html.parser")
# print(soup) #print the webpage html.  RM:  what's the difference between print(page.text) and print(soup)?  One difference is <html> and easier to read output in print(page.text).
print(soup.title)  # print <title>Climate United States - Normals and averages</title>
print(soup.title.string)  # print Climate United States - Normals and averages
print(soup.title.text)  # print Climate United States - Normals and averages
print(soup.p)  # print <p class="selection_title">Select a state by name</p>
print(soup.p.text)  # print Select a state by name
print(soup.p.string)  # print Select a state by name
print(soup.a)  # print <a class="navbar-brand" href="/" title="Temperature - Precipitation - Sunshine - Snowfall"><img alt="Temperature - Precipitation - Sunshine - Snowfall" height="34" src="/assets/images/us-climate-data.png" srcset="/assets/images/us-climate-data.png 1x, /assets/images/us-climate-data-2.png 2x" width="31"/><span class="white ml-2">U.S. Climate Data</span></a>
print(type(soup.a))  # print <class 'bs4.element.Tag'>
print(soup.a.title)  # print None
print(soup.a["title"])  # print Temperature - Precipitation - Sunshine - Snowfall
print(soup.a.text)  # print U.S. Climate Data
print(soup.p)  # print <p class="selection_title">Select a state by name</p>
print(soup.p.parent)  # print <div class="float-left mb-4 mt-2"><p class="selection_title">Select a state by name</p></div>
print(soup.p.parent.prettify())
'''
<div class="float-left mb-4 mt-2">
 <p class="selection_title">
  Select a state by name
 </p>
</div>
'''
for eachlink in soup.findAll("a"):
    print(eachlink.get("href"))
    '''
	...
	/climate/united-states/us
	/
	/climate/united-states/us
	/climate/alabama/united-states/3170
	/climate/alaska/united-states/3171
	/climate/arizona/united-states/3172
	...
	'''
statelinks = []
for getstatelinks in soup.findAll("a"):
    stateurl = getstatelinks.get("href")  # RM:  stateurl is a string
    if ("/climate/" in stateurl) and (stateurl != "/climate/united-states/us") and (stateurl != "/climate/washington/district-of-columbia/united-states/usdc0001"):  # RM:  exclude the link '/climate/washington/district-of-columbia/united-states/usdc0001' in the main United States page
        statelinks.append(stateurl)
print(statelinks)  # print ['/climate/alabama/united-states/3170', '/climate/alaska/united-states/3171', '/climate/arizona/united-states/3172', '/climate/arkansas/united-states/3173', '/climate/california/united-states/3174', '/climate/colorado/united-states/3175', '/climate/connecticut/united-states/3176', '/climate/delaware/united-states/3177', '/climate/district-of-columbia/united-states/3178', '/climate/florida/united-states/3179', '/climate/georgia/united-states/3180', '/climate/hawaii/united-states/3181', '/climate/idaho/united-states/3182', '/climate/illinois/united-states/3183', '/climate/indiana/united-states/3184', '/climate/iowa/united-states/3185', '/climate/kansas/united-states/3186', '/climate/kentucky/united-states/3187', '/climate/louisiana/united-states/3188', '/climate/maine/united-states/3189', '/climate/maryland/united-states/1872', '/climate/massachusetts/united-states/3191', '/climate/michigan/united-states/3192', '/climate/minnesota/united-states/3193', '/climate/mississippi/united-states/3194', '/climate/missouri/united-states/3195', '/climate/montana/united-states/919', '/climate/nebraska/united-states/3197', '/climate/nevada/united-states/3198', '/climate/new-hampshire/united-states/3199', '/climate/new-jersey/united-states/3200', '/climate/new-mexico/united-states/3201', '/climate/new-york/united-states/3202', '/climate/north-carolina/united-states/3203', '/climate/north-dakota/united-states/3204', '/climate/ohio/united-states/3205', '/climate/oklahoma/united-states/3206', '/climate/oregon/united-states/3207', '/climate/pennsylvania/united-states/3208', '/climate/puerto-rico/united-states/7335', '/climate/rhode-island/united-states/3209', '/climate/south-carolina/united-states/3210', '/climate/south-dakota/united-states/3211', '/climate/tennessee/united-states/3212', '/climate/texas/united-states/3213', '/climate/utah/united-states/3214', '/climate/vermont/united-states/3215', '/climate/virginia/united-states/3216', '/climate/washington/united-states/3217', '/climate/west-virginia/united-states/3218', '/climate/wisconsin/united-states/3219', '/climate/wyoming/united-states/3220']
# RM:  The webpage changed.  The python code in the video doesn't work to get the average high temperatures for the last 12 months by month.  I modified the code.
monthlytableone = soup.findAll("td", {"class": "high text-right"})
print(type(monthlytableone))  # print <class 'bs4.element.ResultSet'>
print(monthlytableone)  # print [<td class="high text-right">42</td>, <td class="high text-right">44</td>, <td class="high text-right">53</td>, <td class="high text-right">64</td>, <td class="high text-right">75</td>, <td class="high text-right">83</td>, <td class="high text-right">87</td>, <td class="high text-right">84</td>, <td class="high text-right">78</td>, <td class="high text-right">67</td>, <td class="high text-right">55</td>, <td class="high text-right">45</td>]
csvlist = []
for eachmonthlytableone in monthlytableone:
    print(eachmonthlytableone.text)  # print 42\n 44\n 53\n . . . 67\n 55\n 45
for eachstate in statelinks:
    urlstate = "https://www.usclimatedata.com" + eachstate
    page = requests.get(urlstate)
    soup = BeautifulSoup(page.text, "html.parser")
    # print(urlstate) #print https://www.usclimatedata.com/climate/alabama/united-states/3170
    statename = soup.find("p", {"class": "selection_title"})
    statenamehyphen = statename.text.find("-")
    print(statename.text[0:statenamehyphen - 1])  # print Alabama
    statename = statename.text[0:statenamehyphen - 1]
    csvlist.append(statename)
    with open("csvtemperatures.csv", "a") as fileobject:
        fileobject.write(statename + ",")
    twelvehightemperatures = soup.findAll("td", {"class": "high text-right"})
    for eachtwelvehightemperatures in twelvehightemperatures:
        csvlist.append(eachtwelvehightemperatures.text)
        with open("csvtemperatures.csv", "a") as fileobject:
            fileobject.write(eachtwelvehightemperatures.text + ",")
    # create new line for .csv
    with open("csvtemperatures.csv", "a") as fileobject:
        fileobject.write("\n")
print(csvlist)

# Python Web Scraping with BeautifulSoup BS4 data mining
import requests
from bs4 import BeautifulSoup
page = requests.get("https://en.wikipedia.org/wiki/Bill_Gates")
# print(page) #print <Response [200]>
# print(page.content) #print b'\n<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title>Bill Gates - Wikipedia</title>\n<script>document.documentElement.className="client-js"; . . .
soup = BeautifulSoup(page.content, "html.parser")
# print(soup) #print webpage with html tags
# with open("printwebpagehtml.html","w", encoding="utf-8") as fileobject:
# 	fileobject.write(str(soup))
print(soup.h1)  # print <h1 class="firstHeading" id="firstHeading" lang="en">Bill Gates</h1>
print(soup.find("h1"))  # print <h1 class="firstHeading" id="firstHeading" lang="en">Bill Gates</h1>
print(soup.find("h1").text)  # print Bill Gates
print(soup.find("h1").string)  # print Bill Gates
print(soup.find("div"))  # print <div class="noprint" id="mw-page-base"></div>
print(soup.find("div", id="toc"))
'''
<div aria-labelledby="mw-toc-heading" class="toc" id="toc" role="navigation"><input class="toctogglecheckbox" id="toctogglecheckbox" role="button" style="display:none" type="checkbox"/><div class="toctitle" dir="ltr" lang="en"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Early_life"><span class="tocnumber">1</span> <span class="toctext">Early life</span></a></li>
...
'''
print(soup.find("div", {"id": "toc"}))
'''
<div aria-labelledby="mw-toc-heading" class="toc" id="toc" role="navigation"><input class="toctogglecheckbox" id="toctogglecheckbox" role="button" style="display:none" type="checkbox"/><div class="toctitle" dir="ltr" lang="en"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Early_life"><span class="tocnumber">1</span> <span class="toctext">Early life</span></a></li>
...
'''
print(soup.find("li", class_="toclevel-1"))  # print <li class="toclevel-1 tocsection-1"><a href="#Early_life"><span class="tocnumber">1</span> <span class="toctext">Early life</span></a></li>
print(soup.find("li", {"class": "toclevel-1"}))  # print <li class="toclevel-1 tocsection-1"><a href="#Early_life"><span class="tocnumber">1</span> <span class="toctext">Early life</span></a></li>
print(soup.findAll("li", class_="toclevel-1"))  # print [<li class="toclevel-1 tocsection-1"><a href="#Early_life"><span class="tocnumber">1</span> <span class="toctext">Early life</span></a></li>, <li class="toclevel-1 tocsection-2"><a href="#Microsoft"><span class="tocnumber">2</span> <span class="toctext">Microsoft</span></a> <ul> <li class="toclevel-2 tocsection-3"><a href="#BASIC"><span class="tocnumber">2.1</span> <span class="toctext">BASIC</span></a></li> . . .
print(soup.findAll("li", {"class": "toclevel-1"}))  # print [<li class="toclevel-1 tocsection-1"><a href="#Early_life"><span class="tocnumber">1</span> <span class="toctext">Early life</span></a></li>, <li class="toclevel-1 tocsection-2"><a href="#Microsoft"><span class="tocnumber">2</span> <span class="toctext">Microsoft</span></a> <ul> <li class="toclevel-2 tocsection-3"><a href="#BASIC"><span class="tocnumber">2.1</span> <span class="toctext">BASIC</span></a></li> . . .
print(type(soup.findAll("li", {"class": "toclevel-1"})))  # print <class 'bs4.element.ResultSet'>
wikipediacontents = soup.findAll("li", {"class": "toclevel-1"})
for eachwikipediacontents in wikipediacontents:
    print(eachwikipediacontents)
    print(eachwikipediacontents.text)
    '''
	<li class="toclevel-1 tocsection-1"><a href="#Early_life"><span class="tocnumber">1</span> <span class="toctext">Early life</span></a></li>
	1 Early life
	<li class="toclevel-1 tocsection-2"><a href="#Microsoft"><span class="tocnumber">2</span> <span class="toctext">Microsoft</span></a>
	<ul>
	<li class="toclevel-2 tocsection-3"><a href="#BASIC"><span class="tocnumber">2.1</span> <span class="toctext">BASIC</span></a></li>
	<li class="toclevel-2 tocsection-4"><a href="#IBM_partnership"><span class="tocnumber">2.2</span> <span class="toctext">IBM partnership</span></a></li>
	<li class="toclevel-2 tocsection-5"><a href="#Windows"><span class="tocnumber">2.3</span> <span class="toctext">Windows</span></a></li>
	<li class="toclevel-2 tocsection-6"><a href="#Management_style"><span class="tocnumber">2.4</span> <span class="toctext">Management style</span></a></li>
	<li class="toclevel-2 tocsection-7"><a href="#Antitrust_litigation"><span class="tocnumber">2.5</span> <span class="toctext">Antitrust litigation</span></a></li>
	</ul>
	</li>
	2 Microsoft

	2.1 BASIC
	2.2 IBM partnership
	2.3 Windows
	2.4 Management style
	2.5 Antitrust litigation
	...
	'''
#Amazon code which doesn't work anymore at 42:28.  Amazon blocked webscraping.  Note find_all must be changed to findAll.
import csv
page = requests.get("https://www.amazon.com/s?k=graphic+card&ref=nb_sb_noss_2")
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('div', class_='s-result-list')
resultList = content.find_all('div', class_='s-result-item')
with open('output.csv', mode='w', newline='') as outputFile:
    amazon_prices = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    amazon_prices.writerow(['Name', 'Price', 'Currency', 'Stars', 'Number of Ratings'])
    for result in resultList:
        title = result.find('h2').text.strip()
        stars = result.find('div', class_='a-row a-size-small').find_all('span')[0].text.strip()[:3]
        numberRatings = result.find('div', class_='a-row a-size-small').find_all('span')[3].text.strip()
        prices = result.find('span', class_='a-price').find('span', class_='a-offscreen').text.strip()
        currency = prices[:1]
        price = prices[1:]
        amazon_prices.writerow([title, price, currency, stars, numberRatings])

# Intro To Web Scraping With Python
import requests
from bs4 import BeautifulSoup
from csv import writer
page = requests.get("https://innovateinfinitely.com/favoritequotes.html")
soup = BeautifulSoup(page.text, "html.parser")  # initialize BeautifulSoup
# print(soup.body)
# print(soup.head)
# print(soup.head.title)  #print <title>Favorite Quotes</title>
firstdiv = soup.find("div")
# print(firstdiv) #print my first div <div class="navigationbar">...
alldiv = soup.findAll("div")
# print(alldiv)
alldivsecondindexdiv = soup.findAll("div")[2]
print(alldivsecondindexdiv)  #print <div class="header">...
printfirstquote = soup.find("div", {"class": "quote"})
print(printfirstquote)  #print <div class="quote">\n The world didn't come to an end. --Linus, A Boy Name Charlie Brown\n </div>
printfirstquotebyclass = soup.find(class_="quote")  #class is a reserve word.  An underscore is required.
print(printfirstquotebyclass)  #print <div class="quote">\n The world didn't come to an end. --Linus, A Boy Name Charlie Brown\n</div>
findattributes = soup.find(attrs={"type": "text/javascript"})  #json format to find an attribute
print(findattributes) #print <script src="index.js" type="text/javascript"></script>
htmlasalist = soup.select("p", {"class": "headerfont"}) #select returns a list
print(htmlasalist) #print [<p class="headertitle">Favorite Quotes</p>, <p class="headerfont">Steve Jobs is quoted many times for his successes.  Some of my favorites are from his 2005 graduation speech at Stanford University.  They include the following:  (1) You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future. You have to trust in something - your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.   (2) Stay Hungry, Stay Foolish.  (3) Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it.  (4) Have the courage to follow your heart and intuition. They somehow already know what you truly want to become. Everything else is secondary.</p>]
print(len(htmlasalist)) #print 2
htmlasalistnotreally = soup.select("p", {"class": "headerfont"})[0] #select returns a list which I don't want as a list
print(htmlasalistnotreally) #print <p class="headertitle">Favorite Quotes</p>
htmlasalistnotreally = soup.select("p", {"class": "headerfont"})[1] #select returns a list which I don't want as a list
print(htmlasalistnotreally) #print <p class="headerfont">Steve Jobs is quoted many times for his successes.  Some of my favorites are from his 2005 graduation speech at Stanford University.  They include the following:  (1) You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future. You have to trust in something - your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.   (2) Stay Hungry, Stay Foolish.  (3) Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it.  (4) Have the courage to follow your heart and intuition. They somehow already know what you truly want to become. Everything else is secondary.</p>
classasadot = soup.select(".quote")
print(classasadot) #print [<div class="quote">\n The world didn't come to an end. --Linus, A Boy Name Charlie Brown </div>, <div class="quote">He has a right to criticize, who has a heart to help.  --Abraham Lincoln</div>, <div class="quote">Game Over, Man. Game Over . . . . --Hudson, Aliens</div>, . . .
classasadot10th = soup.select(".quote")[10]
print(classasadot10th) #print <div class="quote">\n It is naive to believe you will always get a favorable reaction from other persons when you use [my] approaches, but the experience of most people shows that you are more likely to change attitudes this way than by not using these principles--and if you increase your successes by even a mere 10 percent, you have become 10 percent more effective as a leader than you were before--and that is your benefit.  --Dale Carnegie, How to Win Friends and Influence People</div>
printquotesonly = soup.find(class_="quote").get_text()
print(printquotesonly) #print The world didn't come to an end. --Linus, A Boy Name Charlie Brown
printquotesonly = soup.find(class_="quote").text
print(printquotesonly) #print The world didn't come to an end. --Linus, A Boy Name Charlie Brown
for eachquote in soup.select(".quote"):  #RM:  select returns a list
    #print(eachquote).text #error message
    print(eachquote.text) #print The world didn't come to an end. --Linus, A Boy Name Charlie Brown . . .
    print(eachquote.get_text()) #print The world didn't come to an end. --Linus, A Boy Name Charlie Brown . . .
webpagebody = soup.body.contents
#print(webpagebody) #prints the webpage's body in a list format
webpagebodyheader = soup.body.contents[1]
print(webpagebodyheader) #print my navigation bar starting at <div class="navigationbar">
webpagebodyheaderthirdcontent = soup.body.contents[1].contents[1].contents[3]
print(webpagebodyheaderthirdcontent) #print <li class="presentlinkpage"><a href="favoritequotes.html">Favorite Quotes</a></li>
webpagebodyheaderthirdcontentnextsibling = soup.body.contents[1].contents[1].contents[3].next_sibling.next_sibling
print(webpagebodyheaderthirdcontentnextsibling) #print <li><a href="myphotoalbum.html">My Photo Album</a></li>
webpagebodyheaderthirdcontentfindnextsibling = soup.body.contents[1].contents[1].contents[3].find_next_sibling() #finds actual html element not a line blank
print(webpagebodyheaderthirdcontentfindnextsibling) #print <li><a href="myphotoalbum.html">My Photo Album</a></li>
onequote = soup.find(class_="quote").find_previous_sibling()
print(onequote) #print None
findaparent = soup.find(class_="footerlinks").find_parent()
print(findaparent) #print footer <footer> . . .
findnextquote = soup.find(class_="quote").find_next_sibling("div")
print(findnextquote) #print <div class="quote"> He has a right to criticize, who has a heart to help.  --Abraham Lincoln</div>  #RM:  Abraham Lincoln is the second quote after The world didn't come to an end.
print("\n")
quotesincsv = soup.findAll("div", {"class": "quote"})
with open("quotes.csv", "w") as csvfile:
    csv_writer = writer(csvfile)
    headers = ["Quote", "Person", "Title"]
    csv_writer.writerow(headers)
    for eachquotesincsv in quotesincsv:
        print(eachquotesincsv) #print <div class="quote">The world didn't come to an end. --Linus, A Boy Name Charlie Brown</div><div class="quote">He has a right to criticize, who has a heart to help.  --Abraham Lincoln</div> . . .
        print(eachquotesincsv.get_text()) #print The world didn't come to an end.  --Linus, A Boy Name Charlie Brown He has a right to criticize, who has a heart to help.  --Abraham Lincoln . . .
        #Get the double hyphens separting quotes and person and title index position
        doublehyphens = eachquotesincsv.get_text().find("--")
        #Get the quote only
        quote = eachquotesincsv.get_text()[0:doublehyphens - 2]
        #Get the person only
        person = eachquotesincsv.get_text()[doublehyphens + 2:]
        #Get the comma separting the person and title
        personcomma = person.find(",")
        #Get the person only no quote and no title
        persononly = person[0:personcomma]
        #If person has no title, title is null
        if personcomma == -1:
            title = None
        else:
            title = person[personcomma + 2:]
        print(quote, persononly, title) #print The world didn't come to an end. Linus A Boy Name Charlie Brown\n He has a right to criticize, who has a heart to help. Abraham Lincoln None
        csv_writer.writerow([quote, persononly, title])

# Using BeautifulSoup and Python to navigate an HTML parse tree
# Open local html file https://www.reddit.com/r/learnpython/comments/8khg83/beautifulsoup_works_on_local_file_but_not_on_a_url/
from urllib.request import urlopen
from bs4 import BeautifulSoup
localhtml = urlopen("file:///home/mar/python/localindex.html")  #RM:  Complete url from Firefox browser
soup = BeautifulSoup(localhtml, "html.parser")
#print(soup) #print webpage with html tags
print(soup.p)
'''
<p id = "first" >
<div > Parse me < /div >
<div > Parse me too!< /div >
< / p >
'''
print(soup.p.attrs) #print {'id': 'first'}
print(soup.p.parent)
'''
<body >
<p id = "first" >
<div > Parse me < /div >
<div > Parse me too!< /div >
< / p >
<p id = "second" > Welcome to HTML < /p >
< / body >
'''
print(soup.p.contents) #print ['\n', <div>Parse me</div>, '\n', <div>Parse me too!</div>, '\n']
print(soup.p.text) #print Parse me\n Parse me too!
print(soup.p.div) #print <div>Parse me</div>
print(soup.p["id"]) #print first
localhtml = urlopen("file:///home/mar/python/localsamplewebsite.html")  #RM:  Complete url from Firefox browser
soup = BeautifulSoup(localhtml, "html.parser")
#print(soup.html) #print webpage with html tags
#print(soup.prettify()) #print html webpage each tag and content one line
#print(soup.html.head) #print <head>\n <title>Sample website</title>\n </head>
print(soup.head) #print <head>\n <title>Sample website</title>\n </head>
print(soup.head.parent) #print webpage with html tags
print(soup.head.text) #print Sample website
print(soup.html.body.p) #print <p>Let's practice <b>scraping</b> on this page</p>
print(soup.html.body.div.p) #print <p>Below are some useful links</p>
print(soup.html.body.div) #print the first div containing the <p>Below are some useful links</p>
print(soup.html.body.div.span) #print None because the first soup.html.body.div is the first div Below are some useful links.
print(soup.span) #print <span style="color:red">This page is for demo only</span>
print(soup.span.parent.attrs) #print {'class': ['warning']}
print(type(soup.span.parent.attrs)) #print <class 'dict'>
print(soup.span.attrs) #print {'style': 'color:red'}
print(soup.span.text) #print This page is for demo only
print(soup.ul.li) #print <li><a href="anaconda.com/distribution/" title="Anaconda Distribution">Anaconda Distribution</a></li>
print(soup.ul.li.next_sibling) #print null #RM:  I don't know why single next_sibling is null
print(soup.ul.li.next_sibling.next_sibling) #print <li><a href="learnpython.org" title="Learn Python">Learn Python Basics</a></li>
print(soup.ul.contents) #print ['\n', <li><a href="anaconda.com/distribution/" title="Anaconda Distribution">Anaconda Distribution</a></li>, '\n', <li><a href="learnpython.org" title="Learn Python">Learn Python Basics</a></li>, '\n', <li><a href="simplehtmlguide.com/cheatsheet.php">HTML cheat sheet</a></li>, '\n']
print(soup.table) #print table and its html tags
print(soup.table.parent) #print table and its html tags and its div tag parent
print(soup.find("div", {"class": "sample_table"})) #print table and its html tags and its div tag parent
for child in soup.table.children:
    print(child)
for child in soup.table.contents:
    print(child)
# for child in soup.table:
#     for eachchild in child:
#         print(eachchild.text) #print AttributeError: 'str' object has no attribute 'text'
eachrow = soup.table
print(eachrow.find("tr").find("th")) #print <th>Tag</th>
print(eachrow.find("tr").find("th").text) #print Tag
eachhtmltag = soup.table
print(eachhtmltag.find("tr").find("td")) #print None  #RM:  reason none is the first tr contains a <th>, not a <td>
print(eachhtmltag.findAll("tr")) #print [<tr><th>Tag</th><th>Description</th></tr>, <tr><td>p</td><td>Paragraph</td></tr>, <tr><td>b</td><td>Bold</td></tr>, <tr><td>i</td><td>Italic</td></tr>, <tr><td>br</td><td>Line Break</td></tr>]
#print(eachhtmltag.findAll("tr").find("td")) #print AttributeError: ResultSet object has no attribute 'find'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
for eachhtmltagin in eachhtmltag.findAll("tr"):
    print(eachhtmltagin)
'''
<tr><th>Tag</th><th>Description</th></tr>
<tr><td>p</td><td>Paragraph</td></tr>
<tr><td>b</td><td>Bold</td></tr>
<tr><td>i</td><td>Italic</td></tr>
<tr><td>br</td><td>Line Break</td></tr>
'''
for eachhtmltagin in eachhtmltag.findAll("tr"):
    print(eachhtmltagin.findAll("td"))
    '''
    []
	[<td>p</td>, <td>Paragraph</td>]
	[<td>b</td>, <td>Bold</td>]
	[<td>i</td>, <td>Italic</td>]
	[<td>br</td>, <td>Line Break</td>]
	'''
# for eachhtmltagin in eachhtmltag.findAll("tr"):
#     print(eachhtmltagin.findAll("td").text) #print AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
for eachhtmltagin in eachhtmltag.findAll("tr"):
    for eachtext in eachhtmltagin.findAll("td"):
        print(eachtext.text)
        '''
        p
		Paragraph
		b
		Bold
		i
		Italic
		br
		Line Break
		'''

# BeautifulSoup find-- and find-all-- methods
# Open local html file https://www.reddit.com/r/learnpython/comments/8khg83/beautifulsoup_works_on_local_file_but_not_on_a_url/
from urllib.request import urlopen
from bs4 import BeautifulSoup
localhtml = urlopen("file:///home/mar/python/localindex.html")  #RM:  Complete url from Firefox browser
soup = BeautifulSoup(localhtml, "html.parser")
print(soup) #print webpage with html tags
print(soup.find("p", {"id": "second"})) #print <p id="second">Welcome to HTML</p>
print(soup.findAll("p", {"id": "second"})) #print [<p id="second">Welcome to HTML</p>]
print(soup.findAll("p")) #print [<p id="first"><div>Parse me</div><div>Parse me too!</div></p>, <p id="second">Welcome to HTML</p>]
print(soup.findAll("p")[1]) #print <p id="second">Welcome to HTML</p>
for iteratefindall in soup.findAll("p"):
    print(iteratefindall)
    '''
    <p id="first">
	<div>Parse me</div>
	<div>Parse me too!</div>
	</p>
	<p id="second">Welcome to HTML</p>
	'''
print(soup.find("div")) #print <div>Parse me</div>
print(soup.find("ul"))
'''
<ul>
<li>A</li>
<li>B</li>
</ul>
'''
print(soup.find("li")) #print <li>A</li>
print(soup.find("li").text) #print A
print(soup.find("div", {"class": "second"}))
'''
<div class="second" id="numbers">
<ul>
<li>1</li>
<li>2</li>
</ul>
</div>
'''
print(soup.find("div", {"id": "numbers"}))
'''
<div class="second" id="numbers">
<ul>
<li>1</li>
<li>2</li>
</ul>
</div>
'''
print(soup.find("div", {"class": "end"}))
'''
<div class="third end" id="numbers">
<ul>
<li>101</li>
<li>102</li>
</ul>
</div>
'''
print(soup.findAll("div"))
'''
[<div>Parse me</div>, <div>Parse me too!</div>, <div class="first" id="some letters">
<ul>
<li>A</li>
<li>B</li>
</ul>
</div>, <div class="second" id="numbers">
<ul>
<li>1</li>
<li>2</li>
</ul>
</div>, <div class="third end" id="numbers">
<ul>
<li>101</li>
<li>102</li>
</ul>
</div>]
'''
print(soup.findAll("ul"))
'''
[<ul>
<li>A</li>
<li>B</li>
</ul>, <ul>
<li>1</li>
<li>2</li>
</ul>, <ul>
<li>101</li>
<li>102</li>
</ul>]
'''
print(soup.findAll("li")) #print [<li>A</li>, <li>B</li>, <li>1</li>, <li>2</li>, <li>101</li>, <li>102</li>]
print(soup.findAll("div", {"id": "numbers"}))
'''
[<div class="second" id="numbers">
<ul>
<li>1</li>
<li>2</li>
</ul>
</div>, <div class="third end" id="numbers">
<ul>
<li>101</li>
<li>102</li>
</ul>
</div>]
'''
alllitags = soup.findAll("li")
print(alllitags[2]) #print <li>1</li>
for eachalllitags in alllitags:
    print(eachalllitags)
    print(eachalllitags.text)
    '''
    <li>A</li>
	A
	<li>B</li>
	B
	<li>1</li>
	1
	<li>2</li>
	2
	<li>101</li>
	101
	<li>102</li>
	102
	'''
# Juan S Vasquez Web Scraping with BeautifulSoup - Yelp-s API PyData LA 2019
import requests as r
from bs4 import BeautifulSoup
legal = "https://www.yellowpages.com/los-angeles-ca/legal?page="
pages = range(1, 3)  #RM:  There are 102 pages.
businesslist = []
for page in pages:
    legalurl = f"{legal}{page}"
    businesslist.append(legalurl)
name = []
phone = []
address = []
localitycityzip = []
categories = []
for page in businesslist:
    print(page)
    url = r.get(page)
    htmldoc = url.text
    soup = BeautifulSoup(htmldoc, "html.parser")
    organiclistings = soup.findAll("div", {"class": "info"})
    for i in organiclistings:
        if i.find("h2", {"class": "n"}):
            name.append(i.find("h2", {"class": "n"}).text)
        else:
            name.append("No name")
        if i.find("div", {"class": "phones phone primary"}):
            phone.append(i.find("div", {"class": "phones phone primary"}).text)
        else:
            phone.append("No phone")
        if i.find("div", {"class": "street-address"}):
            address.append(i.find("div", {"class": "street-address"}).text)
        else:
            address.append("No address")
        if i.find("div", {"class": "localitycityzip"}):
            localitycityzip.append(i.find("div", {"class": "localitycityzip"}).text)
        else:
            localitycityzip.append("No localitycityzip")
        if i.find("div", {"class": "categories"}):
            categories.append(i.find("div", {"class": "categories"}).text)
        else:
            categories.append("No categories")
print(name, phone, address, localitycityzip, categories)
'''
['1. Legal', '2. Law Office Of Michael Rose', '3. Community Driving & Traffic', '4. Your Way Out Bail Bonds', '5. Bad Boys Bail Bonds', "6. Bull's Eye Financial Professionals", '7. Younessi Law', '8. C and M Injury Lawyers', '9. Mann Jeff Law Offices Of', '10. Law Office of Richard Cherry', '11. Ropers Majeski Kohn & Bentley', '12. Law Offices of Gerald L. Marcus', '13. Anderson  Bradshaw Tax Consultants', '14. Direct Legal Support Inc', '15. Schwartz Link K A Law Corporation', '16. National Family Solutions', '17. Law Office Of M Lynda Sheridan', '18. Smyth & Smyth Law Office', '19. Tax Relief Pros', '20. Law Offices of Drasin Yee & Santiago', '21. Lewis B. Sternfels', '22. Gray Humberto R', '23. Citywide Law Group', '24. Skinner III Lemoine', '25. Financial Counseling Center', '26. Jones Eric L Law Offices', '27. The Dominguez Firm', '28. Law Offices of Paul R. Hammons', '29. Doreen A Emenike Los Angeles Immigration Lawyer', '30. Los Angeles Bail Bonds', 'AdLegal Aid Legal Services Corp', 'AdKids Zone Visitation Services', '31. Anyanwu Chima Law Offices', '32. Law Offices of Richard Fleg', '33. Law Offices Of James T. Hudson', '34. Discovery Economics', '35. Davis Wright Tremaine LLP', '36. Child Support Survival Services', '37. BET Tzedek Legal Services', '38. Sidley Austin LLP', '39. Alliance Solution Network', '40. Greenberg Glusker, LLP.', '41. Palma Javier', '42. First Legal Service', '43. Home Owner Assoc', '44. Gallo LLP', '45. Decision Analysis', '46. F F and R Attorney', '47. Dui attorney Los Angeles', '48. Justicia Hispana', '49. Centro De Dolucion Legal', "50. Silva's Legal Service", '51. Centro De Dolucion Legal', '52. Ayuda Legal En General', '53. International College-English', '54. Tech Of US', '55. Wise Law Clinic', '56. First Legal Support Service', '57. Legal Aid Bankruptcy Clinic', '58. Angel De La Comunidad', '59. Proteccion Legal Femenina', '60. Hermandad Mexicana Legal Centers'] ['(424) 298-8420', '(310) 337-1600', '(323) 222-3333', '(626) 291-2002', '(213) 262-1503', '(213) 660-3164', '(424) 325-6681', '(310) 880-4555', '(213) 480-1902', '(323) 873-2779', '(213) 262-6826', '(323) 872-0041', '(844) 446-9432', '(213) 454-0747', '(310) 553-5465', '(833) 489-6958', '(310) 286-7211', '(323) 847-2951', '(424) 388-1144', '(424) 389-0822', '(424) 835-5189', '(310) 447-6577', '(424) 248-2700', '(310) 208-8282', '(323) 954-4330', '(213) 738-7838', '(213) 388-7788', '(310) 348-4900', '(626) 256-8500', '(818) 512-1203', 'No phone', 'No phone', '(213) 385-8288', '(310) 572-6250', '(213) 224-9448', '(213) 621-7780', '(213) 633-6800', '(310) 472-0666', '(213) 384-3243', '(310) 284-6618', '(213) 387-2120', '(310) 553-3610', '(213) 427-0273', '(323) 937-0380', '(310) 472-7372', '(213) 516-8050', '(310) 979-0999', '(310) 439-1082', '(310) 889-0945', '(213) 674-8848', '(213) 382-3085', '(213) 483-0165', '(213) 382-3085', '(213) 382-8282', '(800) 433-3243', '(310) 878-7972', '(310) 734-7129', '(424) 201-4747', '(424) 270-3026', '(213) 381-5939', '(323) 721-9882', '(213) 745-5222'] ['2476 Overland Ave', '8929 S Sepulveda Blvd', '726 S Atlantic Blvd', '1547 W Martin Luther King Jr Blvd', '412 Bauchet St', '355 S Grand Ave Ste 2450', '3435 Wilshire Blvd', '12121 Wilshire Blvd Ste 103', '3600 Wilshire Blvd', '3055 Wilshire Blvd Ste 820', '445 S Figueroa St Ste 3000', '11500 W Olympic Blvd Ste 400', '7080 Hollywood Blvd', '1541 Wilshire Blvd Ste 550', '1801 Century Park E Ste E', '1999 Ave of the Stars', '1801 Century Park E', '4929 Wilshire Blvd', '1605 W Olympic Blvd', '3415 S Sepulveda Blvd Ste 440', '3100 Inglewood Blvd', '11726 San Vicente Blvd', '12424 Wilshire Blvd Ste 705', '10940 Wilshire Blvd', '4311 Wilshire Blvd Ste 602', '3580 Wilshire Blvd Ste 1798a', '3250 Wilshire Boulevard, Suite 2200', '8616 La Tijera Blvd Ste 505', '5055 Wilshire Blvd Ste 740', '108 S Spring St', 'No address', 'No address', '3540 Wilshire Blvd Ste 1200', '11600 Washington Pl', '3550 Wilshire Boulevard Suite 2000', '350 S Grand Ave Ste 2200', '865 S Figueroa St Ste 2400', '11901 Santa Monica Blvd Ste #323', '3435 Wilshire Blvd Ste 470', '1999 Avenue Of The Stars', '3540 Wilshire Blvd Ste 824', '2049 Century Park E Ste 2600', '1605 W Olympic Blvd Ste 9045', '5157 W Adams Blvd', '420 S Barrington Ave', '801 S Figueroa St Ste 2170', '10951 W Pico Blvd Ste 203', '12209 Culver Blvd', '333 S Hope St', '2033 W 7th St', '1113 Venice Blvd', '2502 W Sunset Blvd', '2253 W Pico Blvd', '3156 Wilshire Blvd', '3345 Wilshire Blvd Ste 1106', '603 S Cochran Ave', '1801 Century Park E', '511 N Beverly Glen Blvd', '3315 Glendale Blvd Ste 5', '3055 Wilshire Blvd Ste 1100', '5300 E Beverly Blvd Ste A', '210 W Adams Blvd'] ['No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip', 'No localitycityzip'] ['No categories', 'Legal ClinicsAttorneysFamily Law Attorneys', 'Internet Marketing & AdvertisingTraffic SchoolsDriving Instruction', 'Financial ServicesBail Bond Referral ServiceBail Bonds', 'Bail Bond Referral ServiceBail Bonds', 'Tax AttorneysAdministrative & Governmental Law AttorneysAttorneys', 'AttorneysConstruction Law AttorneysEmployment Discrimination Attorneys', 'AttorneysPersonal Injury Law Attorneys', 'Business Law AttorneysConstruction Law AttorneysAttorneys', 'Family Law AttorneysDivorce AttorneysPersonal Injury Law Attorneys', 'Corporation & Partnership Law AttorneysConstruction Law AttorneysAttorneys', 'Transportation Law AttorneysAttorneysPersonal Injury Law Attorneys', 'Administrative & Governmental Law AttorneysAttorneysAccounting Services', 'Printing ServicesLegal Service PlansCopying & Duplicating Service', 'Attorneys', 'AttorneysChild Custody AttorneysFamily Law Attorneys', 'Child Custody AttorneysAttorneysFamily Law Attorneys', 'General Practice AttorneysAttorneysEstate Planning, Probate, & Living Trusts', 'AttorneysAdministrative & Governmental Law AttorneysTax Attorneys', 'AttorneysLabor & Employment Law AttorneysEmployee Benefits & Worker Compensation Attorneys', 'AttorneysTrademark Agents & ConsultantsPersonal Property Law Attorneys', 'AttorneysImmigration Law AttorneysImmigration & Naturalization Consultants', 'Real Estate AttorneysAttorneysAutomobile Accident Attorneys', 'Attorneys', 'Credit & Debt CounselingBankruptcy ServicesCredit Repair Service', 'General Practice AttorneysAttorneysCorporation & Partnership Law Attorneys', 'Legal Service PlansTransportation Law AttorneysAttorneys', 'AttorneysFinancial ServicesAccounting Services', 'Immigration Law AttorneysAttorneysImmigration & Naturalization Consultants', 'Bail BondsBail Bond Referral Service', 'Legal ClinicsParalegalsDivorce AttorneysChild Custody Attorneys', 'Legal ClinicsChild Custody AttorneysFamily Law AttorneysAttorneys', 'AttorneysBankruptcy Law AttorneysCriminal Law Attorneys', 'Transportation Law AttorneysAttorneysProduct Liability Law Attorneys', 'AttorneysGeneral Practice Attorneys', 'Legal ClinicsAttorneysGeneral Practice Attorneys', 'Legal ClinicsAttorneys', 'Legal Clinics', 'Legal ClinicsAttorneysGeneral Practice Attorneys', 'Legal ClinicsAttorneysLegal Service Plans', 'Legal ClinicsAttorneysGeneral Practice Attorneys', 'Legal ClinicsGeneral Practice AttorneysAttorneys', 'Legal ClinicsLegal Service PlansBankruptcy Law Attorneys', 'Legal ClinicsLegal Service Plans', 'Legal ClinicsLegal Service PlansSocial Service Organizations', 'Legal ClinicsAttorneys', 'Legal ClinicsAttorneys', 'Legal ClinicsAttorneys', 'Legal Clinics', 'Legal Clinics', 'Legal Clinics', 'Legal Clinics', 'Legal Clinics', 'Legal Clinics', 'Legal Clinics', 'Legal Clinics', 'Legal ClinicsAttorneys Referral & Information Service', 'Legal Clinics', 'Legal Clinics', 'Legal Clinics', 'Legal ClinicsAttorneysLegal Service Plans', 'Legal ClinicsAttorneysAttorneys Referral & Information Service']
'''

#Web Scraping with requests- Beautiful Soup - Yelp-s API （01252020)
import yelpcredentials as yc
import requests as r
import pandas as pd
getyelp = "https://api.yelp.com/v3/businesses/search"
keyyelp = yc.key
headeryelp = {"Authorization": "Bearer %s" % keyyelp}
#https://www.yelp.com/developers/documentation/v3/business_search website search parameters documentation
limitnumber = 50
parameters = {"location": "1200 West 7th Street, Los Angeles Ca 90017", "limit": limitnumber, "term": "free wifi", "radius": 805}
response = r.get(getyelp, headers=headeryelp, params=parameters)
data = response.json()
#print(data)
'''
{'businesses': [{'id': 'hERxbudMM_AjSfrDiaMowA', 'alias': 'fairgrounds-coffee-and-tea-los-angeles-4', 'name': 'Fairgrounds Coffee and Tea', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/ZkUehuQR9xSIVEev4NuOlA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/fairgrounds-coffee-and-tea-los-angeles-4?adjust_creative=4tJ3rKmvMI-m3JN0U29LHQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=4tJ3rKmvMI-m3JN0U29LHQ', 'review_count': 71, 'categories': [{'alias': 'coffee', 'title': 'Coffee & Tea'}], 'rating': 4.0, 'coordinates': {'latitude': 34.05181, 'longitude': -118.26785}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '1256 W 7th St', 'address2': None, 'address3': '', 'city': 'Los Angeles', 'zip_code': '90017', 'country': 'US', 'state': 'CA', 'display_address': ['1256 W 7th St', 'Los Angeles, CA 90017']}, 'phone': '+12133780382', 'display_phone': '(213) 378-0382', 'distance': 186.90388849037126}, {'id': 'Aohc9uWSAxILFev2TwiMVQ', 'alias': 'philz-coffee-los-angeles-15', 'name': 'Philz Coffee', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/WRXaHT4T2tjp3QaO2kjtlA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/philz-coffee-los-angeles-15?adjust_creative=4tJ3rKmvMI-m3JN0U29LHQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=4tJ3rKmvMI-m3JN0U29LHQ', 'review_count': 936, 'categories': [{'alias': 'coffee', 'title': 'Coffee & Tea'}, {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'}], 'rating': 4.5, 'coordinates': {'latitude': 34.0465343, 'longitude': -118.2592814}, 'transactions': [], 'price': '$', 'location': {'address1': '801 S Hope St', 'address2': 'Unit A', 'address3': '', 'city': 'Los Angeles', 'zip_code': '90017', 'country': 'US', 'state': 'CA', 'display_address': ['801 S Hope St', 'Unit A', 'Los Angeles, CA 90017']}, 'phone': '+12132132616', 'display_phone': '(213) 213-2616', 'distance': 781.6319481961642}, {'id': 'ABr1g2u9p-H-coNgwpHkUg', 'alias': 'brasil-kiss-coffeebar-los-angeles-3', 'name': 'Brasil Kiss Coffeebar', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/PGq_K4CA1pBHNf6Vmo8C8A/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/brasil-kiss-coffeebar-los-angeles-3?adjust_creative=4tJ3rKmvMI-m3JN0U29LHQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=4tJ3rKmvMI-m3JN0U29LHQ', 'review_count': 252, 'categories': [{'alias': 'coffee', 'title': 'Coffee & Tea'}, {'alias': 'brazilian', 'title': 'Brazilian'}, {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'}], 'rating': 4.0, 'coordinates': {'latitude': 34.0519690715975, 'longitude': -118.262663157451}, 'transactions': ['deliverey', 'pickup'], 'price': '$$', 'location': {'address1': '1010 Wilshire Blvd', 'address2': None, 'address3': '', 'city': 'Los Angeles', 'zip_code': '90017', 'country': 'US', 'state': 'CA', 'display_address': ['1010 Wilshire Blvd', 'Los Angeles, CA 90017']}, 'phone': '+12137855131', 'display_phone': '(213) 785-5131', 'distance': 297.22449992187734}], 'total': 38, 'region': {'center': {'longitude': -118.26576232910156, 'latitude': 34.051226417953856}}}
RM:  38 is the total results if there's no limit.
'''
print(type(data)) #print <class 'dict'>
print(data["businesses"][0]["location"]) #print {'address1': '1256 W 7th St', 'address2': None, 'address3': '', 'city': 'Los Angeles', 'zip_code': '90017', 'country': 'US', 'state': 'CA', 'display_address': ['1256 W 7th St', 'Los Angeles, CA 90017']}
print(data["businesses"][0]["location"]["display_address"]) #print ['1256 W 7th St', 'Los Angeles, CA 90017']
#RM:  I don't understand the offset which used Numpy.
print(data["total"]) #print 38
resultsnumber = data["total"]
listingslist = []
for n in range(0, resultsnumber):
    name = data["businesses"][n]["name"]
    reviews = data["businesses"][n]["review_count"]
    rating = data["businesses"][n]["rating"]
    address = data["businesses"][n]["location"]["display_address"]
    location = " ".join(address)
    phone = data["businesses"][n]["display_phone"]
    listingslist.append([name, reviews, rating, location, phone])
print(listingslist) #print [['Fairgrounds Coffee and Tea', 71, 4.0, '1256 W 7th St Los Angeles, CA 90017', '(213) 378-0382'], ['Brasil Kiss Coffeebar', 252, 4.0, '1010 Wilshire Blvd Los Angeles, CA 90017', '(213) 785-5131'], ['Philz Coffee', 938, 4.5, '801 S Hope St Unit A Los Angeles, CA 90017', '(213) 213-2616'], ['Café WG', 31, 3.5, '900 Wilshire Blvd Ste 130 Los Angeles, CA 90017', '(213) 439-9025'], ['Kachi Deli Cafe & Grill', 280, 4.0, '1055 Wilshire Blvd Los Angeles, CA 90017', '(213) 482-4553'], ...]
columnheader = ["Name", "Reviews", "Rating", "Address", "Phone"]
pandadataframe = pd.DataFrame.from_records(listingslist, index="Name", columns=columnheader)
print(f"Total Records: {len(pandadataframe)}") #print Total Records: 38
print(pandadataframe.head())
'''
                            Reviews  ...           Phone
Name                                 ...                
Fairgrounds Coffee and Tea       71  ...  (213) 378-0382
Brasil Kiss Coffeebar           252  ...  (213) 785-5131
Philz Coffee                    938  ...  (213) 213-2616
Café WG                          31  ...  (213) 439-9025
Kachi Deli Cafe & Grill         280  ...  (213) 482-4553

[5 rows x 4 columns]
'''
print(pandadataframe.info())
'''
<class 'pandas.core.frame.DataFrame'>
Index: 38 entries, Fairgrounds Coffee and Tea to Locala
Data columns (total 4 columns):
Reviews    38 non-null int64
Rating     38 non-null float64
Address    38 non-null object
Phone      38 non-null object
dtypes: float64(1), int64(1), object(2)
memory usage: 1.5+ KB
None
'''
print(pandadataframe.describe())
'''
           Reviews     Rating
count    38.000000  38.000000
mean    242.710526   3.618421
std     504.096725   0.720681
min      12.000000   2.000000
25%      46.250000   3.125000
50%     111.000000   3.500000
75%     244.750000   4.375000
max    3042.000000   5.000000
'''
mostreviews = pandadataframe.sort_values(by="Reviews", ascending=False)
print(mostreviews.head())
'''
                      Reviews  ...           Phone
Name                           ...                
Original Pantry Cafe     3042  ...  (213) 972-9279
Philz Coffee              938  ...  (213) 213-2616
Mendocino Farms           783  ...  (213) 430-9040
Mad Men Burger            335  ...                
Bodhi Bowl                305  ...  (213) 622-6560

[5 rows x 4 columns]
'''
highestratings = pandadataframe.sort_values(by="Rating", ascending=False)
print(highestratings.head())
'''
               Reviews  ...           Phone
Name                    ...                
The Burrow         272  ...  (213) 784-3050
Locala              88  ...  (213) 632-1210
SD Coffee           12  ...  (213) 263-2614
Philz Coffee       938  ...  (213) 213-2616
Cafe Teragram      285  ...  (213) 689-9103

[5 rows x 4 columns]
'''
print(pandadataframe["Rating"].hist()) #print AxesSubplot(0.125,0.11;0.775x0.77)
pandadataframe["Rating"].hist()
pandadataframe["Reviews"].hist()

#BeautifulSoup 4 Python Web Scaping to CSV Excel File
#https://stackoverflow.com/questions/47029280/python-3-add-custom-headers-to-urllib-request-request
import urllib.request
import csv
from bs4 import BeautifulSoup
url = "https://socialblade.com/youtube/top/50/mostviewed"
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response.read(), "html.parser")
#print(soup)
rows = soup.find("div", attrs={"style": "float: right; width: 900px;"}).find_all("div", recursive=False)[4:]
#print(rows)
'''
[<div style="width: 860px; background: #fafafa; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;">
<div style="float: left; width: 50px; color:#888;">1st</div>
<div style="float: left; width: 70px; font-size: 1.1em;">
<span style="font-weight: bold; color:#00bee7;">A++</span> </div>
<div style="float: left; width: 350px; line-height: 25px;">
<img src="https://yt3.ggpht.com/a/AATXAJzOcyc2UwB0vlV7SyfzwgU_La1FOFZmObW3HCH0VzM=s88-c-k-c0xffffffff-no-rj-mo" style="height: 40px; width: 40px; vertical-align: middle; margin-right: 10px;"/>
<a href="/youtube/c/tseriesmusic">T-Series</a>
<sup><i aria-hidden="false" class="fa fa-music" style="color:#aaa; padding-left: 5px;" title="Category: music"></i></sup>
</div>
<div style="float: left; width: 80px;"><span style="color:#555;">14,534</span></div>
<div style="float: left; width: 150px;">
                146M            </div>
<div style="float: left; width: 150px;">
<span style="color:#555;">116,330,142,642</span> </div>
<div style="clear: both;"></div></div>, <div style="width: 860px; background: #f8f8f8;; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;">
<div style="float: left; width: 50px; color:#888;">2nd</div>
<div style="float: left; width: 70px; font-size: 1.1em;">
<span style="font-weight: bold; color:#00bee7;">A++</span> </div>
<div style="float: left; width: 350px; line-height: 25px;">
<img src="https://yt3.ggpht.com/a/AATXAJyQ9bFPnnofMf58cJZPfFHaHZXqLfFm-RW7eC6JXQ=s88-c-k-c0xffffffff-no-rj-mo" style="height: 40px; width: 40px; vertical-align: middle; margin-right: 10px;"/>
<a href="/youtube/c/cocomelon">Cocomelon - Nursery Rhymes</a>
<sup><i aria-hidden="false" class="fa fa-graduation-cap" style="color:#aaa; padding-left: 5px;" title="Category: education"></i></sup>
</div>
<div style="float: left; width: 80px;"><span style="color:#555;">546</span></div>
<div style="float: left; width: 150px;">
                88.4M            </div>
<div style="float: left; width: 150px;">
<span style="color:#555;">70,142,668,168</span> </div>
<div style="clear: both;"></div></div>, <div style="width: 860px; background: #fafafa; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;">
<div style="float: left; width: 50px; color:#888;">3rd</div>
<div style="float: left; width: 70px; font-size: 1.1em;">
<span style="font-weight: bold; color:#00bee7;">A++</span> </div>
<div style="float: left; width: 350px; line-height: 25px;">
<img src="https://yt3.ggpht.com/a/AATXAJxfoPS0uPI-1MQrz0QxcgcPJVtnGcemE8N6NtF7gA=s88-c-k-c0xffffffff-no-rj-mo" style="height: 40px; width: 40px; vertical-align: middle; margin-right: 10px;"/>
<a href="/youtube/c/set-india">SET India</a>
...
'''
file = open("topyoutubers.csv", "w")
writer = csv.writer(file)
writer.writerow(["Username", "Uploads", "Views"])
for eachrow in rows:
    username = eachrow.find("a").text.strip()
    numbers = eachrow.findAll("span", attrs={"style": "color:#555;"})
    uploads = numbers[0].text.strip()
    views = numbers[1].text.strip()
    print(username + " " + uploads + " " + views) #print T-Series 14,534 116,330,142,642
    writer.writerow([username.encode("utf-8"), uploads.encode("utf-8"), views.encode("utf-8")])
file.close()

#Python Tutorial Web Scraping with BeautifulSoup and Requests
from bs4 import BeautifulSoup
import requests
import csv
#Pass HTML webpage as a file
with open("filename.html", "r") as htmlfile:
    soup = BeautifulSoup(htmlfile, "lxml")  #lxml is the parser
#print(soup) #print html in filename.html
#print(soup.prettify()) #print html in filename.html with indentation
title = soup.title
print(title) #print <title>Test - A Sample Website</title>
print(title.text) #print Test - A Sample Website
firstdivtag = soup.div
print(firstdivtag)
'''
<div class="article">
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>
'''
finddivtag = soup.find("div")
print(finddivtag)
'''
<div class="article">
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>
'''
finddivtagclassfooter = soup.find("div", {"class": "footer"}) #or , class_:"footer"
print(finddivtagclassfooter)
'''
<div class="footer">
<p>Footer Information</p>
</div>
'''
finddivtagarticle = soup.find("div", class_="article")
print(finddivtagarticle)
'''
<div class="article">
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>
'''
headline = finddivtagarticle.h2.a
print(headline) #print <a href="article_1.html">Article 1 Headline</a>
print(headline.text) #print Article 1 Headline
headlinemultiplefind = soup.find("div", class_="article").find("h2").find("a")
print(headlinemultiplefind) #print <a href="article_1.html">Article 1 Headline</a>
headlinemultiplefindtext = soup.find("div", class_="article").find("h2").find("a").text
print(headlinemultiplefindtext) #print Article 1 Headline
summary = soup.find("div", class_="article").find("p")
print(summary) #print <p>This is a summary of article 1</p>
findalldivtagarticle = soup.findAll("div", class_="article")
print(findalldivtagarticle) #print [<div class="article"> <h2><a href="article_1.html">Article 1 Headline</a></h2> <p>This is a summary of article 1</p> </div>, <div class="article"> <h2><a href="article_2.html">Article 2 Headline</a></h2> <p>This is a summary of article 2</p> </div>]
for eacharticle in findalldivtagarticle:
    headline = eacharticle.h2.a.text
    print(headline) #print Article 1 Headline
    summary = eacharticle.find("p").text
    print(summary) #print This is a summary of article 1
#Pass HTML webpage as an object
source = requests.get("https://coreyms.com/").text
soup = BeautifulSoup(source, "lxml")
#print(soup.prettify()) #prints webpage
article = soup.find("article")
#print(article.prettify())
headlinecorey = article.h2.a.text
print(headlinecorey) #print Python Tutorial: Zip Files – Creating and Extracting Zip Archives
summarycorey = article.find("div", class_="entry-content")
print(summarycorey)
'''
<div class="entry-content" itemprop="text">
<p>In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let’s get started…<br/></p>
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" width="640"></iframe></span>
</div>
'''
print(summarycorey.p.text) #print In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let’s get started…
print(summarycorey.text) #print In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let’s get started…
videosource = article.find("span", class_="embed-youtube")
print(videosource)
'''
  <span class="embed-youtube" style="text-align:center; display: block;">
   <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" width="640">
   </iframe>
  </span>
'''
videosource = article.find("iframe", class_="youtube-player")
print(videosource)
'''
<iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" width="640"></iframe>
'''
print(type(videosource)) #print <class 'bs4.element.Tag'>
print(videosource["src"]) #print https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent
print(type(videosource["src"])) #print <class 'str'>
print(videosource["src"].find("?")) #print 41
videosourceurl = videosource["src"]
videosourceurl = videosourceurl.replace("embed", "watch")
print(videosourceurl[0:videosource["src"].find("?")]) #print https://www.youtube.com/embed/z0gguhEmWiY
print("\n")
allarticles = soup.findAll("article")
csvfile = open("coreymsscrape.csv", "w")
csvwriter = csv.writer(csvfile)
csvwriter.writerow(["headline", "summary", "video link"]) #csv headers
for eachallarticles in allarticles:
    headlinecorey = eachallarticles.h2.a.text
    print(headlinecorey) #print Python Tutorial: Zip Files – Creating and Extracting Zip Archives
    summarycorey = eachallarticles.find("div", class_="entry-content")
    summarycorey = summarycorey.p.text
    print(summarycorey) #print In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let’s get started…
    videosource = eachallarticles.find("iframe", class_="youtube-player")
    try:
        print(videosource["src"].find("?")) #print 41
        videosourceurl = videosource["src"]
        videosourceurl = videosourceurl.replace("embed", "watch")
        videosourceurl = videosourceurl[0:videosource["src"].find("?")]
        print(videosourceurl)
        #print(videosourceurl[0:videosource["src"].find("?")]) #print https://www.youtube.com/embed/z0gguhEmWiY
    except TypeError:
        videosourceurl = None
    csvwriter.writerow([headlinecorey, summarycorey, videosourceurl])
csvfile.close()
