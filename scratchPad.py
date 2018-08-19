"""

How does the flow of logic work? 

Run "keyword search" 
-> Get a list of channels associated with keywords 
-> save these channel IDs into the database
 
run "get channel videos"
-> Return list of Video IDs associated with a channel
-> save these video IDs and associate them with a channel ID

run "video_statistics"
-> for each video ID available in the database 
-> if there are no available statistics, run function
-> get relevant information about video ID


On running statistics....
-> At the moment I am cutting out any outlier video performances...at some point it would be valuable to go back
and save outlier videos...look for trends on what works and doesn't
-> need to account for variance i.e. start saving standard deviations in DB
-> need to account for 'video favorites' for channel stats



TO DO:
- retroactively update all existing data to conform to new data types
    - grab geographic data
    - grab category Id
    - approximate most common category Id
- need way for spreadsheet to talk to database


REFERENCE CODES:
MODIFY reachOut codes in KEYWORDSEARCH.PY
reachOut ==
3 == initial scrape
4 == additional game scrape
5 == men's fashion tags
8 == duncan scrapes
cycling == cycling communities thing
7 == finding more gaming content creators, long tail
10 == seige content
11 == pub g content
"""

# t = [1,1,1,1,1,1,1,1,5,6,89,6,6354,354,987,]
# print(max(t,key=t.count))

import sqlite3
import json
import numpy
from Models.Video import Video
from Models.Creator_statistics import Channel_statistics
import datetime
import video_statistics
import get_channel_videos
import get_channel_stats
import base_youtube_code


def test():
    client = base_youtube_code.get_authenticated_service()

    channelId_list = ['UCGK9n7svoIjuaQfRIBJXkqQ']
    for channelId in channelId_list:
        connection = sqlite3.connect('core.db')
        c = connection.cursor()
        creatorIdTuple = (channelId,)

        c.execute("""
            SELECT * FROM video
            WHERE creatorID = ?
            """, creatorIdTuple)

        existing_videoCount = c.fetchall()

        connection.commit()
        connection.close()

        # if there is a result in DB, have videos from creator saved
        if len(existing_videoCount) > 0:
            print('already discovered')
        # if results == 0, no videos saved from creator, just discovered a new creator
        else:
            # videoId_list = get_channel_videos.run_get_channel_videos(client, channelId)
            # for videoId in videoId_list:
            #     video_statistics.run_video_statistics(client, videoId)
            print('getting channel stats')
            # get_channel_stats.runStats(channelId)


# test()


def test2():
    array = [0, 1]
    try:
        print(array[2])
    except IndexError:
        print('no response')


# test2()


def keywordGen(game_names):
    for game in game_names:
        print("'" + "rainbow six seige "  + game + ' beginner guide' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' intermediate guide' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' advanced guide' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' for noobs' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' newbies' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' for scrubs' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' for starters' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' for new players' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' grandmaster tips' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' from grandmasters' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' sick gameplayer 2018' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' new season tips' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' the best of' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' insane' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' season 10' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' all legendary skins' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' tricks and tips' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' advanced skills' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' season 9 guide' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' season' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' coaching' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' gone wrong' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' secrets' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' get better' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' improve' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' drills' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' practice tips' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' pro moments' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' grandmaster' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' vs matchup' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' how to play' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' advanced guide' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' breakdown' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' movement' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' positioning' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' 5 top tier' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' how to play console' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' console' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' pro' + "'" + ",")
        print("'" + "rainbow six seige " + game + ' aggressive' + "'" + ",")









game_names = [

'maestro',
    'Alibi',
'Lion',
'Finka',
'Vigil',
'Dokkaebi','Zofia',
'Ela',
'ying',
'lesion',
'mira',
    'jackal',
'hibana',
'echo',
'caveira','capitao',
'blackbeard',
'valkerie',
'buck',
'frost',
'mute'





]

keywordGen(game_names)

#
# def testFuc():
#     someDict = {'snippet': {'country': None}}
#     # print(someDict['snippet']['country'])
#     if someDict['snippet']['country'] == None:
#         print('WHOLE LOTTA GANG')
#     else:
#         print('not none')
#
# testFuc()



#
# from datetime import datetime
# s = '2018-06-01T21:32:27.000Z'
# print(s.split('T'))
"""
# [pairing[0] (UTM), 0 
# pairing[1] (URL), 1
# creator_title, 2
# creator_sub_count, 3
# create_video.publishedAt, 4
# create_video.title, 5 
# create_video.viewCount, 6
# create_video.likeCount, 7
# create_video.commentCount, 8
# create_video.dislikeCount 9

"""





