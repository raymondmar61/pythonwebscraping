#dates 08/04/2005-12/31/2024.  I have times starting 12/01/2024 to present.  Copy Blogs From Innovating Common Knowledge To WordPress Blog.xlsx file I have times 08/04/2005-07/18/2006.  URL template https://ininblog.blogspot.com/yyyy/mm/.  https://ininblog.blogspot.com/2019/10/.  https://ininblog.blogspot.com/2008/11/ has two blogs.  https://ininblog.blogspot.com/2005/08/my-first-blog.html
import csv
import urllib
import urllib.request
from bs4 import BeautifulSoup
with open("blogdatetime.csv", "w", newline="") as fileobject:
    csvwriter = csv.writer(fileobject, delimiter="\t")
    csvwriter.writerow(["Title", "URL", "Date", "Time", "Timeampm"])
url = "https://ininblog.blogspot.com/"
for year in range(2006, 2025):
    year = str(year)
    for month in range(1, 13):
        if month < 10:
            month = "0" + str(month)
        else:
            month = str(month)
        blogurl = url + year + "/" + month + "/"
        print(blogurl)
        # '''
        # https://ininblog.blogspot.com/2006/01/
        # https://ininblog.blogspot.com/2006/02/
        # https://ininblog.blogspot.com/2006/03/
        # ...
        # '''
        # # blogurl = "https://ininblog.blogspot.com/2008/11/"
        page = urllib.request.urlopen(blogurl)
        soup = BeautifulSoup(page, "html.parser")
        # print(soup)
        # print(soup.find("div",{"class":"descriptionwrapper"}))
        # print(soup.find("div", {"class": "post hentry uncustomized-post-template"}))
        # print("\n")
        # print(soup.find_all("div", {"class": "post hentry uncustomized-post-template"}))
        for allinfo in soup.find_all("div", {"class": "post hentry uncustomized-post-template"}):
            # print(allinfo.find("h3", {"class": "post-title entry-title"}))
            '''
            <h3 class="post-title entry-title" itemprop="name">
            <a href="http://ininblog.blogspot.com/2008/11/daylight-standard-time-08.html">Daylight Standard Time '08</a>
            </h3>
            '''
            # print(allinfo.find("h3", {"class": "post-title entry-title"}).find("a")) #print <a href="http://ininblog.blogspot.com/2008/11/wed-nov-5-2008.html">Wed Nov 5, 2008</a>
            # print(allinfo.find("h3", {"class": "post-title entry-title"}).find("a").get_text()) #print Daylight Standard Time '08
            # print(allinfo.find("a", class_="timestamp-link").get("href")) #print https://ininblog.blogspot.com/2008/11/daylight-standard-time-08.html
            # print(allinfo.find("abbr", class_="published").get("title")[0:10]) #print 2008-11-02
            # print(allinfo.find("abbr", class_="published").get("title")[11:16]) #print 01:07
            # print(allinfo.find("abbr", class_="published").get_text()) #print 1:07 AM
            try:
                title = allinfo.find("h3", {"class": "post-title entry-title"}).find("a").get_text()
            except:
                title = "No Title" #RM:  Sat Oct 31, 2009 no title in blog.  It's a test message.  Also, small amount blogs no title.
            urlblogspecific = allinfo.find("a", class_="timestamp-link").get("href")
            date = allinfo.find("abbr", class_="published").get("title")[0:10]
            time = allinfo.find("abbr", class_="published").get("title")[11:16]
            timeampm = allinfo.find("abbr", class_="published").get_text()
            with open("blogdatetime.csv", "a", newline="") as fileobject:
                csvwriter = csv.writer(fileobject, delimiter="\t")
                csvwriter.writerow([title, urlblogspecific, date, time, timeampm])
