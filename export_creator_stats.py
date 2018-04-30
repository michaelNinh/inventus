import csv
import sqlite3
import json

"""
Flow of logic
- pull all available creator_stats data from database -> data structure of stats
- create csv 
- write all data into csv  
"""


"""
CSV headers
Discovery keyword 0 
Channel name  1
Full channel youtube URL / youtube.com/[channelId] 2
email 3
subscribers 4  
average views 5
average engagement 6 
date recorded 7
"""

def pull_creator_stats_data():
    """returns an array of arrays"""
    connection = sqlite3.connect('core.db')
    c = connection.cursor()
    c.execute("""
    SELECT keywords, channelTitle, creatorId, email, totalSubs, viewsAverage, engagementRate, dataRecorded
    FROM creator
    JOIN creator_stats on creator.channelId = creator_stats.creatorId
    """)

    return c.fetchall()

    # print(json.dumps(c.fetchall(), indent=2))


def writeCSV(csvPath, masterStatsArray):
    with open(csvPath, 'w') as csvfile:
        fieldnames = ['discovery keyword', 'channel name', 'URL', 'emails', 'total subs', 'AVG views','AVG engagement', 'date recorded']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for channelEntry in masterStatsArray:
            # transform testDict into correct writable formate here

            #dumboFormat is the format needed to correctly write into csv
            dumboFormat = {
                'discovery keyword': channelEntry[0],
                'channel name': channelEntry[1],
                'URL': channelEntry[2],
                'emails': channelEntry[3],
                'total subs': channelEntry[4],
                'AVG views': channelEntry[5],
                'AVG engagement': channelEntry[6],
                'date recorded': channelEntry[7],
            }

            print(dumboFormat)

            writer.writerow(dumboFormat)
    print('SAVED TO MEMORY')



dataArray = pull_creator_stats_data()


writeCSV('/Users/michaelninh/PycharmProjects/inventus/inventusCoreData.csv',dataArray)



