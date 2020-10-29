#Introduction to Web Scraping (Python) - Lesson 01 (BeautifulSoup, Twitter)
import urllib
import urllib.request
from bs4 import BeautifulSoup
webpageurl = "https://twitter.com/realDonaldTrump"
page = urllib.request.urlopen(webpageurl)
soup = BeautifulSoup(page, "html.parser")
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
print(soup.find("p", {"class": "ProfileHeaderCard-bio u-dir"}).text) #print 45th President of the United States of America  #RM:  found the HTML code by writing the soup as a json string file and finding 45th President of the United States of America.
#RM found the HTML code by writing the soup as a HTML string file and finding 45th President of the United States of America.
#print(soup.find("div",{"class":"ProfileHeaderCard"})) #print <div class="ProfileHeaderCard">\n <h1 class="ProfileHeaderCard-name"> . . .
print(soup.find("div", {"class": "ProfileHeaderCard"}).find("p").text) #print 45th President of the United States of America
#print(soup.find("div",{"class":"ProfileHeaderCard"}).find("p",{"class":"ProfileHeaderCard-bio u-dir"})) #print <p class="ProfileHeaderCard-bio u-dir" dir="ltr">45th President of the United States of America<img alt="🇺🇸" aria-label="Emoji: Flag of United States" class="Emoji Emoji--forText" draggable="false" src="https://abs.twimg.com/emoji/v2/72x72/1f1fa-1f1f8.png" title="Flag of United States"/></p>
print(soup.find("div", {"class": "ProfileHeaderCard"}).find("p", {"class": "ProfileHeaderCard-bio u-dir"}).text) #print 45th President of the United States of America
for alltweets in soup.findAll("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
    print(alltweets.text, end="\n\n")
    '''
	Had a great call with Catholic Leaders and Educators earlier today. I will be online tomorrow at 10:15 A.M. (Eastern) for Sunday Mass celebrated by @CardinalDolan at St. Patrick’s Cathedral (@StPatsNYC) in New York City. Join me: https://saintpatrickscathedral.org/live pic.twitter.com/iQy5iH5Lk6

	I never said the pandemic was a Hoax! Who would say such a thing? I said that the Do Nothing Democrats, together with their Mainstream Media partners, are the Hoax. They have been called out & embarrassed on this, even admitting they were wrong, but continue to spread the lie!
	...
	'''

#Introduction to Web Scraping (Python) - Lesson 02 (Scrape Tables)
import urllib
import urllib.request
from bs4 import BeautifulSoup
def makesoup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    #print the html code in a tempdelete.html file to view the html code easier
    #filewrite = open("tempdelete.html","w")
    #filewrite.write(str(soupdata))
    #filewrite.close()
    return soupdata


soup = makesoup("https://www.basketball-reference.com/players/a/")
#instructor started tutorial
displayerplayer = ""
for trhtmltagrow in soup.findAll("tr"):
    #print(trhtmltagrow.text) #print Alaa Abdelnaby19911995F-C6-10240June 24, 1968Duke . . .
    for tdhtmltagdata in trhtmltagrow.findAll("td"):
        #print(tdhtmltagdata.text) #print 1991\n 1995\n F-C\n 6-10\n 240\n June 24, 1968\n Duke . . .
        displayerplayer = displayerplayer + "," + tdhtmltagdata.text
print(displayerplayer) #print ,1991,1995,F-C,6-10,240,June 24, 1968,Duke,1969,1978,C-F,6-9,235,April 7, 1946,Iowa State, . . .

#html code changed from video produced to today May 2, 2020.  I adjust the tutorial and the Python code.
'''
#html code of one player
<tr><th class="left" data-append-csv="abdelal01" data-stat="player" scope="row"><a href="/players/a/abdelal01.html">Alaa Abdelnaby</a></th><td class="right" data-stat="year_min">1991</td><td class="right" data-stat="year_max">1995</td><td class="center" data-stat="pos">F-C</td><td class="right" csk="82.0" data-stat="height">6-10</td><td class="right" data-stat="weight">240</td><td class="left" csk="19680624" data-stat="birth_date"><a href="/friv/birthdays.cgi?month=6&amp;day=24">June 24, 1968</a></td><td class="left" data-stat="colleges"><a href="/friv/colleges.fcgi?college=duke">Duke</a></td></tr>
'''
for trhtmltagbasektballplayer in soup.findAll("tr"):
    for thhtmltagplayername in trhtmltagbasektballplayer.findAll("th", {"data-stat": "player"}):
        #print(thhtmltagplayername.text) #print Alaa Abdelnaby
        displayplayerstatsoneline = ""
    for tdhtmltagplayerstats in trhtmltagbasektballplayer.findAll("td"):
        displayplayerstatsoneline = displayplayerstatsoneline + "," + tdhtmltagplayerstats.text
        #print(tdhtmltagplayerstats.text) #print 1991\n 1995\n F-C\n 6-10\n 240\n June 24, 1968\n Duke . . .
    print(thhtmltagplayername.text + "," + displayplayerstatsoneline[1:]) #print Alaa Abdelnaby,1991,1995,F-C,6-10,240,June 24, 1968,Duke
#RM:  the printed output is separated by a semicolon because the Birth Date contains the comma for the year.  I also found some players with multiple colleges separated by a comma.  Create a .csv file writing the output to a .csv file.  You may separate by a tab \t.
'''
#html code header
<th aria-label="Birth Date" class="poptip sort_default_asc center" data-stat="birth_date" scope="col">Birth Date</th>
<th aria-label="colleges" class="poptip center" data-stat="colleges" scope="col">Colleges</th>
'''
displayheader = ""
for thhtmltagheader in soup.findAll("th", {"class": "poptip sort_default_asc center"}):
    displayheader = displayheader + ";" + thhtmltagheader.text
print((displayheader + ";" + soup.find("th", {"class": "poptip center"}).text)[1:]) #print Player;From;To;Pos;Ht;Wt;Birth Date,Colleges
for trhtmltagbasektballplayer in soup.findAll("tr"):
    for thhtmltagplayername in trhtmltagbasektballplayer.findAll("th", {"data-stat": "player"}):
        #print(thhtmltagplayername.text) #print Alaa Abdelnaby
        displayplayerstatsoneline = ""
    for tdhtmltagplayerstats in trhtmltagbasektballplayer.findAll("td"):
        displayplayerstatsoneline = displayplayerstatsoneline + ";" + tdhtmltagplayerstats.text
        #print(tdhtmltagplayerstats.text) #print 1991\n 1995\n F-C\n 6-10\n 240\n June 24, 1968\n Duke . . .
    if thhtmltagplayername.text == "Player":
        pass
    else:
        print(thhtmltagplayername.text + ";" + displayplayerstatsoneline[1:])
'''
Player;From;To;Pos;Ht;Wt;Birth Date,Colleges
Alaa Abdelnaby;1991;1995;F-C;6-10;240;June 24, 1968;Duke
Zaid Abdul-Aziz;1969;1978;C-F;6-9;235;April 7, 1946;Iowa State
'''
#https://stackoverflow.com/questions/56906907/trying-to-print-a-single-line-of-a-table-using-beautifulsoup-but-the-line-locat
# for trhtmltagheader in soup.select("tr"):
# 	print(trhtmltagheader.text.replace("\n",",").strip())
# 	'''
# 	,Player,From,To,Pos,Ht,Wt,Birth Date,Colleges,
# 	Alaa Abdelnaby19911995F-C6-10240June 24, 1968Duke
# 	Zaid Abdul-Aziz19691978C-F6-9235April 7, 1946Iowa State
# 	'''

#Introduction to Web Scraping (Python) - Lesson 03 (Scrape Multiple Web Pages)
import urllib
import urllib.request
from bs4 import BeautifulSoup
from string import ascii_lowercase
import time
timer = time.time()
def makesoup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


csvfilewrite = open("allbasektballplayers.csv", "w")
for letter in ascii_lowercase:
    print(letter) #print a\n b\n . . . y\n z  #RM:  the link https://www.basketball-reference.com/players/ ends with a lower case letter.  Create a for loop to loop all basektball players by last name alphabetically
    soup = makesoup("https://www.basketball-reference.com/players/" + letter)
    displayheader = ""
    for thhtmltagheader in soup.findAll("th", {"class": "poptip sort_default_asc center"}):
        displayheader = displayheader + ";" + thhtmltagheader.text
    print((displayheader + ";" + soup.find("th", {"class": "poptip center"}).text)[1:]) #print Player;From;To;Pos;Ht;Wt;Birth Date,Colleges
    csvfilewrite.write((displayheader + ";" + soup.find("th", {"class": "poptip center"}).text)[1:] + "\n")
    for trhtmltagbasektballplayer in soup.findAll("tr"):
        for thhtmltagplayername in trhtmltagbasektballplayer.findAll("th", {"data-stat": "player"}):
            #print(thhtmltagplayername.text) #print Alaa Abdelnaby
            displayplayerstatsoneline = ""
        for tdhtmltagplayerstats in trhtmltagbasektballplayer.findAll("td"):
            displayplayerstatsoneline = displayplayerstatsoneline + ";" + tdhtmltagplayerstats.text
            #print(tdhtmltagplayerstats.text) #print 1991\n 1995\n F-C\n 6-10\n 240\n June 24, 1968\n Duke . . .
        if thhtmltagplayername.text == "Player":
            pass
        else:
            print(thhtmltagplayername.text + ";" + displayplayerstatsoneline[1:])
            csvfilewrite.write(thhtmltagplayername.text + ";" + displayplayerstatsoneline[1:] + "\n")
'''
Player;From;To;Pos;Ht;Wt;Birth Date,Colleges
Alaa Abdelnaby;1991;1995;F-C;6-10;240;June 24, 1968;Duke
Zaid Abdul-Aziz;1969;1978;C-F;6-9;235;April 7, 1946;Iowa State
'''
csvfilewrite.close()
delta = time.time() - timer
print(delta)
#Introduction to Web Scraping (Python) - Lesson 03 (Scrape Multiple Web Pages) Part 2 Extract reviews from a website with multiple pages of reviews Practice Trial And Errror
import urllib
import urllib.request
from bs4 import BeautifulSoup

def makesoup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


soup = makesoup("https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-Fairmont_San_Jose-San_Jose_California.html")
# https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-Fairmont_San_Jose-San_Jose_California.html
# https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-or1Fairmont_San_Jose-San_Jose_California.html#REVIEWS
# https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-or5-Fairmont_San_Jose-San_Jose_California.html#REVIEWS
link = soup.find(attrs={"class": "pageNum current cx_brand_refresh_phase2 disabled"})
#print(link) #print <span class="pageNum current cx_brand_refresh_phase2 disabled">1</span>
reviews = soup.findAll("div", {"class": "hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"})
#print(reviews)
'''
[<div class="hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H" data-test-target="HR_CC_CARD"><div class="social-member-event-MemberEventOnObjectBlock__member_event_block--1Kusx"><a class="styleguide-avatar-Avatar__avatar--2NStU ui_social_avatar inline" href="/Profile/catherineeK8809MA" target="_self"><img alt=""/></a><div class="social-member-event-MemberEventOnObjectBlock__event_wrap--1YkeG"><div class="social-member-event-MemberEventOnObjectBlock__member_actions--2uzIM"><div class="overflow"><span class="_3-zQ1eyd _3LR9XvrV"><span class="_35pfga6W _2HBN-k68"></span></span></div><span class="social-section-overflow-SectionOverflowMenu__float--3mJ5J"></span></div><div class="social-member-event-MemberEventOnObjectBlock__event_type--3njyv"><span><a class="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC" href="/Profile/catherineeK8809MA">Catherine E</a> wrote a review Mar 2020</span></div><div class="social-member-MemberHeaderStats__event_info--30wFs"><span class="social-member-MemberHeaderStats__stat_item--34E1r"> . . . 
'''
#print(type(reviews)) #print <class 'bs4.element.ResultSet'>

#for gettextfromhtmltags in reviews:
#print(gettextfromhtmltags.text)
'''
	Catherine E wrote a review Mar 20205 contributions2 helpful votesHockey night in San JoseHad a great stay at Fairmont hotel. Greeted by Perla, so pleasant and helpful. She upgraded our room. Lots of restaurants near by. Short walk to sap centre. We had a late flight departure and again Perla was able to extend our stay until one. Pedal suggested the pool, where we relaxed after ordering room service. Thank you Perla for a wonderful experience. Also, the supplies in the washroom were wonderful, nice conditioner and lovely scent body wash. Great view of city, thanks to Perla.Read moreDate of stay: March 2020Trip type: Traveled as a coupleHelpfulShare 
	GoHuskies_Olympia wrote a review Feb 2020Olympia, Washington19 contributions4 helpful votesFantastic customer serviceOn top of the absolutely perfect location, the best part of our visit was the outstanding customer service.  On the night we checked in, Elia was very helpful and on checkout, Susheel was fantastic.  However, above all, Ellana made our trip.  She was thoughtful, kind, and did everything possible to make our trip a special one.  When there are so many options in a city, customer service like the Fairmont staff provides puts it head an shoulders above other properties.Read moreDate of stay: February 2020ValueLocationServiceHelpfulShare 
	neyu wrote a review Feb 2020UK3 contributions7 helpful votesThis hotel needs a holidayThe good: The location is right in the middle of downtown San Jose. With the car park under the hotel I can get to/from my car without getting wet in inclement weather. The room service is prompt.  The so-so: The decor is tired: sad carpets, bashed furniture, drawer handles falling off, peeling wallpaper. The bathroom toiletries are "Rose 31" by Le Labo.  That's right - every morning I smell like an old lady.  Don't get me wrong, I am fond of rose in the right way (Penhaligan's Hamman Bouquet for example), but not this. The (lack of) signage in the corridors leaves some guests confused.  One morning I guided some aircrew to the elevators as they got lost. The saddest part was the little alarm clock - stuck in time, at twenty-past-twelve, much like the hotel.  The ugly: Parking is $26/day. Every item of food and drink in the room is booby-trapped: you move it, touch it, look at it in a funny way, and the sensor trips and your room is charged.  Badda bing badda boom. Perhaps as part of this policy there is no space in the booby-trapped fridge to put your own items (water bottle, etc).  I didn't even open the door in case I tripped one of the sensors.  Ka-ching!! The only internet option is wifi.  When it doesn't work there is an Ethernet jack in the front of the writing desk, which would be fine if it was actually connected to anything (it isn't - I checked).  Conclusion: This hotel needs a holiday to refresh itself for the modern business traveller.…Read moreDate of stay: September 2019LocationServiceSleep QualityTrip type: Traveled on business3 Helpful votesHelpfulShare 
'''
textreviews = soup.findAll("q", {"class": "location-review-review-list-parts-ExpandableReview__reviewText--gOmRC"})
#print(textreviews)
'''
[<q class="location-review-review-list-parts-ExpandableReview__reviewText--gOmRC"><span>Had a great stay at Fairmont hotel. Greeted by Perla, so pleasant and helpful. She upgraded our room. Lots of restaurants near by. Short walk to sap centre. We had a late flight departure and again Perla was able to extend our stay until one. Pedal suggested the pool, where we relaxed after ordering room service. Thank you Perla for a wonderful experience. Also, the supplies in the washroom were wonderful, nice conditioner and lovely scent body wash. Great view of city, thanks to Perla.</span></q>, <q class="location-review-review-list-parts-ExpandableReview__reviewText--gOmRC"><span>On top of the absolutely perfect location, the best part of our visit was the outstanding customer service.  On the night we checked in, Elia was very helpful
'''
#print(type(textreviews)) #print <class 'bs4.element.ResultSet'>
for eachtextreviews in textreviews:
    print(eachtextreviews.text) #print Had a great stay at Fairmont hotel. Greeted by Perla, so pleasant and helpful. She upgraded our room. Lots of restaurants near by. Short walk to sap centre. We had a late flight departure and again Perla was able to extend our stay until one. Pedal suggested the pool, where we relaxed after ordering room service. Thank you Perla for a wonderful experience. Also, the supplies in the washroom were wonderful, nice conditioner and lovely scent body wash. Great view of city, thanks to Perla. . . .
titlereviews = soup.findAll("a", {"class": "location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT"})
for eachtitlereviews in titlereviews:
    print(eachtitlereviews.text) #print Hockey night in San Jose\n Fantastic customer service\n . . .
userreview = soup.findAll("a", {"class": "ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"})
for eachuserreview in userreview:
    print(eachuserreview.text) #print Catherine E\n GoHuskies_Olympia\n . . .
starsreview = soup.findAll("div", {"class": "location-review-review-list-parts-RatingLine__bubbles--GcJvM"})
#print(starsreview)
'''
[<div class="location-review-review-list-parts-RatingLine__bubbles--GcJvM" data-test-target="review-rating"><span class="ui_bubble_rating bubble_50"></span></div>, <div class="location-review-review-list-parts-RatingLine__bubbles--GcJvM" data-test-target="review-rating"><span class="ui_bubble_rating bubble_50"></span></div>, <div class="location-review-review-list-parts-RatingLine__bubbles--GcJvM" data-test-target="review-rating"><span class="ui_bubble_rating bubble_30"></span>
'''
#print(type(starsreview)) #print <class 'bs4.element.ResultSet'>
for eachstarsreview in starsreview:
    #print(type(eachf.find("span"))) #print <class 'bs4.element.Tag'>
    starnumber = str(eachstarsreview.find("span"))
    print(starnumber[37:39]) #print 50\n 50\n 30\n . . .
datestayreview = soup.findAll("span", {"class": "location-review-review-list-parts-EventDate__event_date--1epHa"})
for eachdatestayreview in datestayreview:
    print(eachdatestayreview.text[14:]) #print March 2020\n February 2020\n September 2019\n . . .
datepostreview = soup.findAll("div", {"class": "social-member-event-MemberEventOnObjectBlock__event_type--3njyv"})
for eachdatepostreview in datepostreview:
    #print(type(eachh.find("span").text)) #print <class 'str'>
    monthyear = eachdatepostreview.find("span").text[-8:]
    print(monthyear) #print Mar 2020\n Feb 2020\n Feb 2020 . . .
#Introduction to Web Scraping (Python) - Lesson 03 (Scrape Multiple Web Pages) Part 2 Extract reviews from a website with multiple pages of reviews Completed
import urllib
import urllib.request
from bs4 import BeautifulSoup

def makesoup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


header = "tripadvisormember\tdatereview\trating\treviewtitle\treviewtext\tdatestay\n"
filewrite = open("tempdelete.txt", "w")
filewrite.write(header)
for number in range(0, 2689, 5):
    print(number)
    #https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-Fairmont_San_Jose-San_Jose_California.html
    #https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-or5-Fairmont_San_Jose-San_Jose_California.html#REVIEWS
    #https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-or2675-Fairmont_San_Jose-San_Jose_California.html#REVIEWS
    #soup = makesoup("https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-or1-Fairmont_San_Jose-San_Jose_California.html")
    soup = makesoup("https://www.tripadvisor.com/Hotel_Review-g33020-d81705-Reviews-or" + str(number) + "-Fairmont_San_Jose-San_Jose_California.html")
    reviews = soup.findAll("div", {"class": "hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"})
    # for gettextfromhtmltags in reviews:
    # 	print(gettextfromhtmltags.text)
    '''
		Catherine E wrote a review Mar 20205 contributions2 helpful votesHockey night in San JoseHad a great stay at Fairmont hotel. Greeted by Perla, so pleasant and helpful. She upgraded our room. Lots of restaurants near by. Short walk to sap centre. We had a late flight departure and again Perla was able to extend our stay until one. Pedal suggested the pool, where we relaxed after ordering room service. Thank you Perla for a wonderful experience. Also, the supplies in the washroom were wonderful, nice conditioner and lovely scent body wash. Great view of city, thanks to Perla.Read moreDate of stay: March 2020Trip type: Traveled as a coupleHelpfulShare 
		GoHuskies_Olympia wrote a review Feb 2020Olympia, Washington19 contributions4 helpful votesFantastic customer serviceOn top of the absolutely perfect location, the best part of our visit was the outstanding customer service.  On the night we checked in, Elia was very helpful and on checkout, Susheel was fantastic.  However, above all, Ellana made our trip.  She was thoughtful, kind, and did everything possible to make our trip a special one.  When there are so many options in a city, customer service like the Fairmont staff provides puts it head an shoulders above other properties.Read moreDate of stay: February 2020ValueLocationServiceHelpfulShare 
		neyu wrote a review Feb 2020UK3 contributions7 helpful votesThis hotel needs a holidayThe good: The location is right in the middle of downtown San Jose. With the car park under the hotel I can get to/from my car without getting wet in inclement weather. The room service is prompt.  The so-so: The decor is tired: sad carpets, bashed furniture, drawer handles falling off, peeling wallpaper. The bathroom toiletries are "Rose 31" by Le Labo.  That's right - every morning I smell like an old lady.  Don't get me wrong, I am fond of rose in the right way (Penhaligan's Hamman Bouquet for example), but not this. The (lack of) signage in the corridors leaves some guests confused.  One morning I guided some aircrew to the elevators as they got lost. The saddest part was the little alarm clock - stuck in time, at twenty-past-twelve, much like the hotel.  The ugly: Parking is $26/day. Every item of food and drink in the room is booby-trapped: you move it, touch it, look at it in a funny way, and the sensor trips and your room is charged.  Badda bing badda boom. Perhaps as part of this policy there is no space in the booby-trapped fridge to put your own items (water bottle, etc).  I didn't even open the door in case I tripped one of the sensors.  Ka-ching!! The only internet option is wifi.  When it doesn't work there is an Ethernet jack in the front of the writing desk, which would be fine if it was actually connected to anything (it isn't - I checked).  Conclusion: This hotel needs a holiday to refresh itself for the modern business traveller.…Read moreDate of stay: September 2019LocationServiceSleep QualityTrip type: Traveled on business3 Helpful votesHelpfulShare 
	'''
    #print(reviews)
    '''
	[<div class="hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H" data-test-target="HR_CC_CARD"><div class="social-member-event-MemberEventOnObjectBlock__member_event_block--1Kusx"><a class="styleguide-avatar-Avatar__avatar--2NStU ui_social_avatar inline" href="/Profile/catherineeK8809MA" target="_self"><img alt=""/></a><div class="social-member-event-MemberEventOnObjectBlock__event_wrap--1YkeG"><div class="social-member-event-MemberEventOnObjectBlock__member_actions--2uzIM"><div class="overflow"><span class="_3-zQ1eyd _3LR9XvrV"><span class="_35pfga6W _2HBN-k68"></span></span></div><span class="social-section-overflow-SectionOverflowMenu__float--3mJ5J"></span></div><div class="social-member-event-MemberEventOnObjectBlock__event_type--3njyv"><span><a class="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC" href="/Profile/catherineeK8809MA">Catherine E</a> wrote a review Mar 2020</span></div><div class="social-member-MemberHeaderStats__event_info--30wFs"><span class="social-member-MemberHeaderStats__stat_item--34E1r"> . . . 
	'''
    #print(type(reviews)) #print <class 'bs4.element.ResultSet'>
    for eachreviews in reviews:
        #print(eachreviews.text) #print Catherine E wrote a review Mar 20205 contributions2 helpful votes Hockey night in San JoseHad a great stay at Fairmont hotel. Greeted by Perla, so pleasant and helpful. She upgraded our room. Lots of restaurants near by. Short walk to sap centre. We had a late flight departure and again Perla was able to extend our stay until one. Pedal suggested the pool, where we relaxed after ordering room service. Thank you Perla for a wonderful experience. Also, the supplies in the washroom were wonderful, nice conditioner and lovely scent body wash. Great view of city, thanks to Perla.Read moreDate of stay: March 2020Trip type: Traveled as a coupleHelpfulShare
        textreviews = eachreviews.find("q", {"class": "location-review-review-list-parts-ExpandableReview__reviewText--gOmRC"})
        #print(textreviews  #print <span>Had a great stay at Fairmont hotel. Greeted by Perla, . . .
        textreviews = str(textreviews.find("span"))
        textreviews = textreviews[6:-7]
        #print(textreviews) #print Had a great stay at Fairmont hotel. Greeted by Perla,  . . .
        titlereviews = eachreviews.find("a", {"class": "location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT"}).text
        #print(titlereviews) #print Hockey night in San Jose
        userreview = eachreviews.find("a", {"class": "ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"}).text
        #print(userreview) #print Catherine E
        starsreview = eachreviews.find("div", {"class": "location-review-review-list-parts-RatingLine__bubbles--GcJvM"})
        #print(starsreview)
        '''
		[<div class="location-review-review-list-parts-RatingLine__bubbles--GcJvM" data-test-target="review-rating"><span class="ui_bubble_rating bubble_50"></span></div>, <div class="location-review-review-list-parts-RatingLine__bubbles--GcJvM" data-test-target="review-rating"><span class="ui_bubble_rating bubble_50"></span></div>, <div class="location-review-review-list-parts-RatingLine__bubbles--GcJvM" data-test-target="review-rating"><span class="ui_bubble_rating bubble_30"></span>
		'''
        #print(type(starsreview)) #print <class 'bs4.element.ResultSet'>
        starsreview = str(starsreview.find("span"))
        starsreview = starsreview[37:39]
        #print(starsreview) #print 50
        datestayreview = eachreviews.find("span", {"class": "location-review-review-list-parts-EventDate__event_date--1epHa"}).text[14:]
        #print(datestayreview) #print March 2020
        datepostreview = eachreviews.find("div", {"class": "social-member-event-MemberEventOnObjectBlock__event_type--3njyv"})
        datepostreview = datepostreview.find("span").text[-8:]
        #print(datepostreview) #print Mar 2020
        #tabdelimiter = userreview+"\t"+datepostreview+"\t"+starsreview+"\t"+titlereviews+"\t"+textreviews+"\t"+datestayreview
        tabdelimiter = userreview + "\t" + datepostreview + "\t" + starsreview + "\t" + titlereviews + "\t" + textreviews + "\t" + datestayreview + "\n"
        filewrite.write(tabdelimiter)
filewrite.close()

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
classcontainer = htmlparsed.findAll("div", {"class": "item-container"})
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
print(classcontainer[0].findAll("a", {"class": "item-title"}))
'''
[<a class="item-title" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards">
                            
                            G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 256...
                        </a>]
'''
print(classcontainer[0].findAll("a", {"class": "item-title"})[0].text) #print G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 256...
print(classcontainer.findAll("li", {"class": "price-ship"}))


classbranding = htmlparsed.findAll("div", {"class": "item-branding"}.text)
print(classbranding[0])
'''
<div class="item-branding">
<a class="item-rating" href="https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941?cm_sp=SearchSuccess-_-INFOCARD-_-graphics+cards-_-20-231-941-_-1&amp;Description=graphics+cards&amp;IsFeedbackTab=true#scrollFullInfo"><i class="rating rating-4"></i><span class="item-rating-num">(245)</span></a>
</div>
'''

for eachclasscontainer in classcontainer:
    #brand = eachclasscontainer.a.img["title"]
    titlecontainer = eachclasscontainer.findAll("a", {"class": "item-title"})[0].text

#Python Programming Tutorial - 22 - Download an Image from the Web YouTube thenewboston
import urllib.request
from random import randint
def downloadimage(url, filedirectory, filename):
    fullfilepath = filedirectory + filename + ".jpg"
    urllib.request.urlretrieve(url, fullfilepath)


randomfilename = str(randint(10000, 99999))
print(randomfilename)
downloadimage("https://innovateinfinitely.com/stevejobs.jpg", "/home/mar/python/", randomfilename)

#Python Programming Tutorial - 25 - How to Build a Web Crawler (1_3)
#Python Programming Tutorial - 26 - How to Build a Web Crawler (2_3)
#Python Programming Tutorial - 27 - How to Build a Web Crawler (3_3)
#RM:  thenewboston vidoes outdated.  I added and experimented the code.
import requests
from bs4 import BeautifulSoup
def labels(bloglink):
    sourcecode = requests.get(bloglink) #connect to url and store the (html code?) results in sourcecode
    plaintext = sourcecode.text #get the text from sourcecode
    soupobject = BeautifulSoup(plaintext, "html.parser") #BeautifulSoup converts plaintext to a BeautifulSoup object soupobject to format plaintext.  RM:  need "html.parser" inside BeautifulSoup
    for bloglabels in soupobject.findAll("span", {"class": "post-labels"}):
        #print(type(bloglabels)) #print <class 'bs4.element.Tag'>
        #print(bloglabels)
        '''
        <span class="post-labels">
        Labels:
        <a href="https://ininblog.blogspot.com/search/label/Consumer" rel="tag">Consumer</a>,
        <a href="https://ininblog.blogspot.com/search/label/Economy" rel="tag">Economy</a>,
        <a href="https://ininblog.blogspot.com/search/label/Information%20Age" rel="tag">Information Age</a>,
        <a href="https://ininblog.blogspot.com/search/label/Life" rel="tag">Life</a>,
        <a href="https://ininblog.blogspot.com/search/label/Money" rel="tag">Money</a>,
        <a href="https://ininblog.blogspot.com/search/label/Moving%20Forward" rel="tag">Moving Forward</a>,
        <a href="https://ininblog.blogspot.com/search/label/Responsibility" rel="tag">Responsibility</a>,
        <a href="https://ininblog.blogspot.com/search/label/Retail" rel="tag">Retail</a>,
        <a href="https://ininblog.blogspot.com/search/label/Throwback" rel="tag">Throwback</a>
        </span>
        '''
        #print(type(bloglabels.text)) #print <class 'str'>
        #print(bloglabels.text)
        print(bloglabels.text.replace(",", ""))
        '''
		Labels:
		Consumer
		Economy
		Information Age
		Life
		Money
		Moving Forward
		Responsibility
		Retail
		Throwback
		'''
def tradespider(maxpages):
    page = 1
    while page <= maxpages:
        url = "https://ininblog.blogspot.com/2020/0" + str(page) + "/"
        sourcecode = requests.get(url) #connect to url and store the (html code?) results in sourcecode
        plaintext = sourcecode.text #get the text from sourcecode
        soupobject = BeautifulSoup(plaintext, "html.parser") #BeautifulSoup converts plaintext to a BeautifulSoup object soupobject to format plaintext.  RM:  need "html.parser" inside BeautifulSoup
        #for link in soupobject.findAll("a",{"class":"post-title entry-title"}):
        for link in soupobject.findAll("h3", {"class": "post-title entry-title"}):
            #print(type(link)) #print <class 'bs4.element.Tag'>
            #print(link)
            '''
            <h3 class="post-title entry-title" itemprop="name">
            <a href="https://ininblog.blogspot.com/2020/01/throwback-blog-41-stamp.html">Throwback Blog:  $.41 Stamp</a>
            </h3>
            <h3 class="post-title entry-title" itemprop="name">
            <a href="https://ininblog.blogspot.com/2020/01/top-ten-blogs-stand-test-of-time.html">Top Ten Blogs Stand The Test Of Time</a>
            </h3>
            '''
            stringlink = str(link) #convert link to string
            hrefstringlinkend = stringlink.find(".html\">") #find the index for the end of the url link
            hrefstringlink = stringlink[61:hrefstringlinkend + 5] #slice the url or extract the url link
            print(link.text, end="")
            print(hrefstringlink)
            labels(hrefstringlink)
            '''
			Throwback Blog:  $.41 Stamp
			https://ininblog.blogspot.com/2020/01/throwback-blog-41-stamp.html
			Top Ten Blogs Stand The Test Of Time
			https://ininblog.blogspot.com/2020/01/top-ten-blogs-stand-test-of-time.html
			'''
        page += 1


print(tradespider(5))
'''
The Reader Takes Something Away With These Pics
https://ininblog.blogspot.com/2020/05/the-reader-takes-something-away-with.html

Labels:
Appreciation
Championship
Hidden Beast
Honesty
House
Leisure
Life
Little Things
Major League Baseball
Music
Old
Pictures
Responsibility
Retail
Sad
San Francisco Giants
'''

from urllib.parse import urlsplit
myurl = "http://www.innovateinfinitely.com"
print(type(myurl)) #print <class 'str'>
url1 = urlsplit(myurl)
print(type(url1)) #print <class 'urllib.parse.SplitResult'>
print(url1.geturl()) #print http://www.innovateinfinitely.com
print(type(url1.geturl())) #print <class 'str'>
url2 = urlsplit(url1.geturl())
print(url2.geturl()) #print http://www.innovateinfinitely.com

from urllib.parse import quote, quote_plus, quote_from_bytes, unquote, unquote_plus, unquote_to_bytes
myurl = "http://www.innovateinfinitely.com"
print(quote(myurl, safe="/", encoding=None, errors=None)) #print http%3A//www.innovateinfinitely.com
#safe="/" is default, encoding="utf-8" is default.  errors="strict" is default means unsupported characters raise a UnicodeEncodeError.
print(quote(myurl, safe="", encoding=None, errors=None)) #print http%3A%2F%2Fwww.innovateinfinitely.com
#quote_plus() replaces spaces by a plus sign
print(quote_plus(myurl)) #print http%3A%2F%2Fwww.innovateinfinitely.com
print(quote_plus(myurl, safe="", encoding=None, errors=None)) #print http%3A%2F%2Fwww.innovateinfinitely.com
myurlspace = "http://www.innovate infinitely.com"
print(quote_plus(myurlspace)) #print http%3A%2F%2Fwww.innovate+infinitely.com
#quote_from_bytes accepts bytes instead of string and no string-to-bytes encoding
mybytes = b'a&\xef'
print(quote_from_bytes(mybytes, safe="/")) #print a%26%EF
#unquote replaces escape characters by their single-character equivalent.  The optional encoding and errors parameters specify how to decode percent-encoded sequences into Unicode characters.  Defaults are noted in code.  errors="replace" means invalid sequences are replaced by a placeholder character.
quoteplusstring = "http%3A%2F%2Fwww.innovate+infinitely.com"
print(unquote(quoteplusstring, encoding="utf-8", errors="replace")) #print http://www.innovate+infinitely.com
#unquote_plus replace plus signs by spaces
print(unquote_plus(quoteplusstring)) #print http://www.innovate infinitely.com
#unquote_to_bytes replaces %xx escapes by their single-octet equivalent, and return a bytes object.
stringtobytes = "a%26%EF"
print(unquote_to_bytes(stringtobytes)) #print b'a&\xef'
