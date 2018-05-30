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
        SET reachOut = ?, notes = ?
        WHERE channelTitle = ?
        """, (reachOut, notes, channelName))


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


readConvertCsvData('/Users/michaelninh/PycharmProjects/inventus/csvRaws/4batch.csv - 2nd filter.csv')
# testWork()
# getcolm()




"""
['channelTitle', 'creatorId', 'totalSubs', 'totalViews', 'vidIds', 'email', 'totalComments', 'videoCount', 'keywords', 'reachOut', 'country', 'notes', 'approval']
"""
