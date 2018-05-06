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
        continue


test2()



