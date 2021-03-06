import csv
# import unicodecsv as csv
import sqlite3
import json
import helpers

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
    
    
    SELECT keywords, channelTitle, creator.creatorId, email, country,
    totalSubs, viewsAverage, engagementRate, dataRecorded, 
    sampleSize, notes, reachOut, categoryId, date_last_video
    FROM creator
    JOIN creator_stats ON creator.creatorId = creator_stats.creatorId
    
    LIMIT 1 
    """)

    return c.fetchall()

    # print(json.dumps(c.fetchall(), indent=2))



"""
keywords, 0 
channelTitle, 1 
creator.creatorId, 2 
email, 3
country, 4
totalSubs, 5
viewsAverage, 6 
engagementRate,  7
dataRecorded, 8
sampleSize, 9
notes, 10
reachOut 11
categoryIId 12
"""



def writeCSV(csvPath, masterStatsArray):
    with open(csvPath, 'w', encoding='utf-8') as csvfile:
        fieldnames = ['discovery keyword', 'channel name', 'email', 'country','URL', 'AVG views', 'AVG engagement','notes', 'reachOut', 'total subs', 'date recorded', 'sampleSize','id','categoryId','last video']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for channelEntry in masterStatsArray:
            # transform testDict into correct writable formate here

            # concate channelId into youtubeURL pattern
            fullUrl = 'https://www.youtube.com/channel/' + channelEntry[2] + '/about'

            categoryId = helpers.youtubeChannelDict.get(channelEntry[12], 'N/A')

            date_recorded_edit = channelEntry[8].split(" ")[0]


            #dumboFormat is the format needed to correctly write into csv
            dumboFormat = {
                'discovery keyword': channelEntry[0],
                'channel name': channelEntry[1],
                'email': channelEntry[3],
                'country': channelEntry[4],
                'URL': fullUrl,
                'AVG views': channelEntry[6],
                'AVG engagement': channelEntry[7],
                'notes': channelEntry[10],
                'reachOut': channelEntry[11],
                'total subs': channelEntry[5],
                'date recorded': date_recorded_edit,
                'sampleSize': channelEntry[9],
                'id': channelEntry[2],
                'categoryId': categoryId,
                'last video': channelEntry[13]
                # connection = sqlite3.connect('core.db')
            # c = connection.cursor()
            #
            # creatorIdTuple = (channelEntry[2],)
            #
            # c.execute("""
            #     SELECT * FROM video
            #     WHERE creatorID = ?
            #     """, creatorIdTuple)
            #
            # # This code breaks stuff.
            # # print(c.fetchall())
            # # getDate = c.fetchall()[0]
            # # lastVideoDate = getDate[2].split('T')[0]
            #
            # # THIS CODE GETS THE MOST RECENT RECORDED VIDEO
            # try:
            #     getDate = c.fetchall()[0]
            #     lastVideoDate = getDate[2].split('T')[0]
            #     print(lastVideoDate)
            # except IndexError:
            #     lastVideoDate = 'no date'
            #     print('no date')
            #
            #
            #
            # connection.commit()
            # connection.close()
            #
            # #     END GET DATE
            }


            writer.writerow(dumboFormat)
    print('SAVED TO MEMORY')



dataArray = pull_creator_stats_data()
writeCSV('/Users/michaelninh/PycharmProjects/inventus/exports/testAgain2.csv' ,dataArray)




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



