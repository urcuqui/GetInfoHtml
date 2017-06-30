#Python 2.7
# this class gets the information through parameters of html tags and the information will save in sqlite database


import urllib
from bs4 import BeautifulSoup
import sqlite3





def save_db(id, ffi, fff, other, id_service):
    conn = sqlite3.connect('sms4dc_colombia.db')
    c = conn.cursor()
    # Insert a row of data
    query = "INSERT INTO INFO_SERVICE VALUES (" + str(id) + ", " + str(ffi) + "," + str(fff) + ",'" + other + "', '',"+str(id_service)+")"
    print(query)
    c.execute(query)
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    print("save")

def read_html():

    r = urllib.urlopen("url").read()
    soup = BeautifulSoup(r)
    letters = soup.find_all("td")
    i=1
    c=0
    id=606
    while (i < len(letters)):


        a_array = letters[i].find_all("a")
        a_length = len(a_array)
        ffi = 0
        fff = 0
        other = ""
        while(c < a_length):
            if(c==0):
                frequencies = a_array[c].get_text().split(" - ")
                ffi = frequencies[0]
                fff = frequencies[1]

            else:
                other += a_array[c].get_text()+";"
            c = c+1

        c = 0
        i=3+i
        save_db(id, ffi, fff, other, 16)
        id =1+id


read_html()

