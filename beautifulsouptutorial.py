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