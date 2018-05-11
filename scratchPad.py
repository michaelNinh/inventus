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
    array = [0,1]
    try:
        print(array[2])
    except IndexError:
        print('no response')


# test2()


def keywordGen(game_names):
    for game in game_names:
        print("'" + game + ' beginner guide' + "'" + ",")
        print("'" + game + ' beginner tutorial' + "'" + ",")
        print("'" + game + ' beginner strategy' + "'" + ",")
        print("'" + game + ' beginner methods' + "'" + ",")
        print("'" + game + ' beginner lessons' + "'" + ",")
        print("'" + game + ' beginner techniques' + "'" + ",")
        print("'" + game + ' beginner videos' + "'" + ",")
        print("'" + game + ' beginner lessons' + "'" + ",")
        print("'" + game + ' beginner tactics' + "'" + ",")
        print("'" + game + ' beginner overview' + "'" + ",")
        print("'" + game + ' beginner tips and trick' + "'" + ",")
        print("'" + game + ' beginner gameplay' + "'" + ",")
        print("'" + game + ' beginner common mistakes' + "'" + ",")
        print("'" + game + ' beginner builds' + "'" + ",")
        print("'" + game + ' beginner players' + "'" + ",")
        print("'" + game + ' beginner noobs' + "'" + ",")
        print("'" + game + ' beginner news' + "'" + ",")
        print("'" + game + ' tutorial' + "'" + ",")

        print("'" + game + ' intermediate guide' + "'" + ",")
        print("'" + game + ' intermediate tutorial' + "'" + ",")
        print("'" + game + ' intermediate strategy' + "'" + ",")
        print("'" + game + ' intermediate methods' + "'" + ",")
        print("'" + game + ' intermediate lessons' + "'" + ",")
        print("'" + game + ' intermediate techniques' + "'" + ",")
        print("'" + game + ' intermediate videos' + "'" + ",")
        print("'" + game + ' intermediate lessons' + "'" + ",")
        print("'" + game + ' intermediate tactics' + "'" + ",")
        print("'" + game + ' intermediate overview' + "'" + ",")
        print("'" + game + ' intermediate tips and trick' + "'" + ",")
        print("'" + game + ' intermediate gameplay' + "'" + ",")
        print("'" + game + ' intermediate common mistakes' + "'" + ",")
        print("'" + game + ' intermediate builds' + "'" + ",")
        print("'" + game + ' intermediate players' + "'" + ",")
        print("'" + game + ' intermediate noobs' + "'" + ",")
        print("'" + game + ' intermediate news' + "'" + ",")
        print("'" + game + ' intermediate tutorial' + "'" + ",")

        print("'" + game + ' expert guide' + "'" + ",")
        print("'" + game + ' expert tutorial' + "'" + ",")
        print("'" + game + ' expert strategy' + "'" + ",")
        print("'" + game + ' expert methods' + "'" + ",")
        print("'" + game + ' expert lessons' + "'" + ",")
        print("'" + game + ' expert techniques' + "'" + ",")
        print("'" + game + ' expert videos' + "'" + ",")
        print("'" + game + ' expert lessons' + "'" + ",")
        print("'" + game + ' expert tactics' + "'" + ",")
        print("'" + game + ' expert overview' + "'" + ",")
        print("'" + game + ' expert tips and trick' + "'" + ",")
        print("'" + game + ' expert gameplay' + "'" + ",")
        print("'" + game + ' expert common mistakes' + "'" + ",")
        print("'" + game + ' expert builds' + "'" + ",")
        print("'" + game + ' expert players' + "'" + ",")
        print("'" + game + ' expert noobs' + "'" + ",")
        print("'" + game + ' expert news' + "'" + ",")
        print("'" + game + ' expert tutorial' + "'" + ",")

        print("'" + game + ' pro guide' + "'" + ",")
        print("'" + game + ' pro tutorial' + "'" + ",")
        print("'" + game + ' pro strategy' + "'" + ",")
        print("'" + game + ' pro methods' + "'" + ",")
        print("'" + game + ' pro lessons' + "'" + ",")
        print("'" + game + ' pro techniques' + "'" + ",")
        print("'" + game + ' pro videos' + "'" + ",")
        print("'" + game + ' pro lessons' + "'" + ",")
        print("'" + game + ' pro tactics' + "'" + ",")
        print("'" + game + ' pro overview' + "'" + ",")
        print("'" + game + ' pro tips and trick' + "'" + ",")
        print("'" + game + ' pro gameplay' + "'" + ",")
        print("'" + game + ' pro common mistakes' + "'" + ",")
        print("'" + game + ' pro builds' + "'" + ",")
        print("'" + game + ' pro players' + "'" + ",")
        print("'" + game + ' pro noobs' + "'" + ",")
        print("'" + game + ' pro news' + "'" + ",")
        print("'" + game + ' pro tutorial' + "'" + ",")




game_names = ['smite', 'escape from tarkov', 'runscape', 'world of tanks', 'bloodborne', 'GTA 5']

keywordGen(game_names)




