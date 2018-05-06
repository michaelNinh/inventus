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
    SELECT keywords, channelTitle, creator.creatorId, email, country,totalSubs, viewsAverage, engagementRate, dataRecorded, sampleSize, notes 
    
    FROM creator
    
    JOIN creator_stats ON creator.creatorId = creator_stats.creatorId
    
    limit 1
    
    """)

    return c.fetchall()

    # print(json.dumps(c.fetchall(), indent=2))


def writeCSV(csvPath, masterStatsArray):
    with open(csvPath, 'w') as csvfile:
        fieldnames = ['discovery keyword', 'channel name', 'URL', 'emails','country', 'total subs', 'AVG views','AVG engagement', 'date recorded', 'sampleSize', 'notes', 'id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for channelEntry in masterStatsArray:
            # transform testDict into correct writable formate here

            # concate channelId into youtubeURL pattern
            fullUrl = 'https://www.youtube.com/channel/' + channelEntry[2] + '/about'

            #dumboFormat is the format needed to correctly write into csv
            dumboFormat = {
                'discovery keyword': channelEntry[0],
                'channel name': channelEntry[1],
                'URL': fullUrl,
                'emails': channelEntry[3],
                'country': channelEntry[4],
                'total subs': channelEntry[5],
                'AVG views': channelEntry[6],
                'AVG engagement': channelEntry[7],
                'date recorded': channelEntry[8],
                'sampleSize': channelEntry[9],
                'notes': channelEntry[10],
                'id': channelEntry[2]
            }

            print(dumboFormat)

            writer.writerow(dumboFormat)
    print('SAVED TO MEMORY')



dataArray = pull_creator_stats_data()
# print(dataArray)


writeCSV('/Users/michaelninh/PycharmProjects/inventus/inventusCoreData3.csv',dataArray)




"""
[('mechanical keyboard review', 0 
'Linus Tech Tips', 1
'UCXuqSBlHAE6Xw-yeJA0Tunw', 2 
'testEmail', 3
'n/a', 4
5724356, 5 
691304.0, 6
0.035287418173963025, 7
'2018-04-30 10:08:19.525312', 8 
 13.0 9)]



"""



