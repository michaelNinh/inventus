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
"approval" 
"notes" 

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


        masterChannelDict[row[0]] = [{'subscribers': row[1]},
                                     {'total view': row[2]},
                                     {'possible emails': row[3].replace("[","").replace("]", "").replace("'", "")},
                                     {'search tag': row[4]},
                                     {'reach out': row[5]}]
    print('UPDATED MEMORY')