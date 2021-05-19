import sqlite3

#sudo find -type d -name "firefox"
'''
./usr/share/doc/firefox
./usr/lib/firefox
find: ‘./run/user/1000/doc’: Permission denied
find: ‘./run/user/1000/gvfs’: Permission denied
./home/mar/.cache/mozilla/firefox
./home/mar/.mozilla/firefox
./home/mar/.local/lib/python3.8/site-packages/selenium/webdriver/firefox
./etc/firefox
'''

#https://support.mozilla.org/en-US/questions/1132706
#It is in the Firefox profile, it uses a database file called places.sqlite, that also includes your bookmarks.
#RM:  Complete path:  /home/mar/.mozilla/firefox/bvb4b9nt.default-release/places.sqlite.  That's why find -type d -name "History" and  find -type d -name "history" didn't work.  Firefox doesn't have the Chrome's History directory.

path = "/home/mar/.mozilla/firefox/bvb4b9nt.default-release/places.sqlite"
#RM:  Firefox browser must be closed.
connection = sqlite3.connect(path)
print(connection) #print <sqlite3.Connection object at 0x7f0dea90a3f0>
c = connection.cursor()
print(c) #print <sqlite3.Cursor object at 0x7f5f9b432960>
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
listalltables = c.fetchall()  #source https://www.kite.com/python/answers/how-to-list-tables-using-sqlite3-in-python
print(listalltables) #print [('moz_origins',), ('moz_places',), ('moz_historyvisits',), ('moz_inputhistory',), ('moz_bookmarks',), ('moz_bookmarks_deleted',), ('moz_keywords',), ('sqlite_sequence',), ('moz_anno_attributes',), ('moz_annos',), ('moz_items_annos',), ('moz_meta',), ('sqlite_stat1',)]
c.execute("select * from moz_historyvisits;")
printhistory = c.fetchall()
print(printhistory)
'''
[(1, 0, 134, 1621385194956145, 2, 0), (2, 1, 135, 1621385195123893, 5, 0), (3, 0, 136, 1621385214992617, 2, 0), (4, 3, 137, 1621385215117900, 5, 0), (5, 4, 138, 1621385220026637, 5, 0), (6, 0, 139, 1621385255325284, 2, 0), (7, 6, 140, 1621385255482021, 5, 0), (8, 7, 141, 1621385255583621, 5, 0), (9, 8, 142, 1621385279031702, 1, 0), (10, 0, 143, 1621385443274767, 2, 0), (11, 10, 144, 1621385443537551, 5, 0), (12, 0, 145, 1621385449457295, 2, 0), (13, 12, 146, 1621385449660803, 5, 0), (14, 0, 147, 1621385472743576, 2, 0), (15, 14, 148, 1621385472981504, 6, 0), (16, 0, 149, 1621385482280876, 2, 0), (17, 16, 150, 1621385482508046, 6, 0), (18, 0, 151, 1621385969920211, 2, 0), (19, 18, 152, 1621385970495730, 5, 0)]
'''
