#Open a web brower on terminal
#python3.8 -m webbrowser -t "http://www.python.org"
import webbrowser

url = "https://innovateinfinitely.com"
webbrowser.open(url, new=0, autoraise=True) #open in same browser window if possible, browser window raised if possible
urlnewone = "https://innovateinfinitely.com/blog.html"
webbrowser.open(urlnewone, new=1, autoraise=True) #open in new browser window if possible, browser window raised if possible
webbrowser.open(url, new=2, autoraise=True) #open in new browser page or tab, browser window raised if possible
urlnewwindow = "https://innovateinfinitely.com/favoritequotes.html"
webbrowser.open_new(urlnewwindow)
urlregister = "https://innovateinfinitely.com/contact.html"
webbrowser.register("firefox", Mozilla("Mozilla"), instance=None)

url = "https://innovateinfinitely.com"
webbrowser.get("firefox").open(url, new=0, autoraise=True)

url = "https://innovateinfinitely.com"
firefoxpath = "/usr/bin/firefox"
webbrowser.get(firefoxpath).open(url, new=0, autoraise=True)

#Opens google.com in new browser window, seconds pass, opens espn.com in same browser window new tab
webbrowser.get("firefox").open("google.com")
webbrowser.get("firefox").open("espn.com")

mywebpagelist = ["https://innovateinfinitely.com/favoritequotes.html", "https://innovateinfinitely.com/cooking101.html", "https://innovateinfinitely.com/blog.html"]
for eachmywebpagelist in mywebpagelist:
    webbrowser.open(eachmywebpagelist, new=2)

browservariable = webbrowser.open("https://www.innovateinfinitely.com")
browservariable #opens browser window to innovateinfinitely.com
