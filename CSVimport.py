import csv
import sqlite3
import json

"""
flow of logic 
Meant to take modified objects in CSV and update them in database

read CSV
where creatorId = creatorId from CSV 
update object attribute inside DB 


on the creator BD object, might need to add 
"approve" attribute 
0 - disapprove
1 - approve 
null - not reviewed 

when exporting, i could select all objects with null approvals

this function needs to import from CSV to database
"channel name" [1]
"reachOut" [7]
"notes" [8]

"""


def readConvertCsvData(csvPath):
    f = open(csvPath)

    csv_f = csv.reader(f)

    firstline = True
    # the following converts readData into pythonData
    for row in csv_f:
        if firstline:
            firstline = False
            continue
        # create an object from row


        channelName = str(row[1])
        # channelId = row[12]
        email = row[2]
        notes = row[7]
        reachOut = row[8]

        # print(channelId)
        print(channelName)
        # print(notes)
        # print(reachOut)

        connection = sqlite3.connect('core.db')
        c = connection.cursor()

        c.execute("""
        UPDATE creator
        SET reachOut = ?, notes = ?, email = ?
        WHERE channelTitle = ?
        """, (reachOut, notes, email,channelName))


        connection.commit()
        connection.close()

    print('UPDATED storage')


def testWork():
    connection = sqlite3.connect('core.db')
    c = connection.cursor()
    c.execute("""    
    SELECT reachOut, notes
    FROM creator
    WHERE creator.reachOut = 1
    """)
    print(c.fetchall())


def getcolm():
    connection = sqlite3.connect('core.db')
    cursor = connection.execute('select * from creator')
    names = list(map(lambda x: x[0], cursor.description))
    print(names)


# testWork()
readConvertCsvData('/Users/michaelninh/PycharmProjects/inventus/csvRaws/seige check - Sheet1.csv')
# getcolm()




"""
['channelTitle', 'creatorId', 'totalSubs', 'totalViews', 'vidIds', 'email', 'totalComments', 'videoCount', 'keywords', 'reachOut', 'country', 'notes', 'approval']
"""

"""
What is the main problem? 
- I do not have a clear way to understand who I've scraped for email.
- I need to link emails found or unavailables into the database 
- I also need to add a new database row for the last video made


"""