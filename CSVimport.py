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
    #the following converts readData into pythonData
    for row in csv_f:
        if firstline:
            firstline = False
            continue
        # create an object from row

        channelId = row[-1]
        notes = row[7]
        reachOut = row[8]

        connection = sqlite3.connect('core.db')
        c = connection.cursor()

        c.execute("""
        UPDATE creator
        SET reachOut = ?, notes = ?
        WHERE creatorId = ?
        """, (reachOut, notes, channelId))

        connection.commit()
        connection.close()

    print('UPDATED storage')


def testWork():
    connection = sqlite3.connect('core.db')
    c = connection.cursor()
    c.execute("""
    SELECT *
    FROM creator
    WHERE creatorId = 'UCmY3dSr-0TOkJqy0btd2AJg'
    """)

    print(c.fetchall())





readConvertCsvData('/Users/michaelninh/Desktop/inventus/csvRaws/test.csv - First Round Emails.csv')
testWork()