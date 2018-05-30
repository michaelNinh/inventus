import sqlite3
import json
import numpy
from Models.Video import Video
from Models.Creator_statistics import Channel_statistics
import datetime

"""
Logic flow

For each creatorId, get all saved videos
Calculate Q1, Q3, IQR
Find views, comments, likes, adjusted for outliers
save channel statistics as another object?


get_saved videos -> array of videos
get_statistics(array of videos) -> array of stats
create video_stats object(array of stats + creatorId)
save into database  

"""


def get_saved_videos(creatorId):
    """returns an array of Video Objects related to CreatorID"""
    connection = sqlite3.connect('core.db')
    c = connection.cursor()
    # SQLITE needs tuples for some reason?
    creatorIdTuple = (creatorId,)

    c.execute("""
    SELECT * FROM video
    WHERE creatorID = ?
    """, creatorIdTuple)

    rawVideoJson = c.fetchall()

    connection.commit()
    connection.close()

    videoArray = []

    for raw in rawVideoJson:
        newVideo = Video(
            videoId=raw[0],
            creatorId=raw[1],
            publishedAt=raw[2],
            title=raw[3],
            videoTags=raw[4],
            viewCount=raw[5],
            likeCount=raw[6],
            dislikeCount=raw[7],
            favoriteCount=raw[8],
            commentCount=raw[9],
            categoryId=raw[10]
        )

        videoArray.append(newVideo)

    return videoArray


def removeOutliers(dataArray):
    elements = numpy.array(dataArray)
    mean = numpy.mean(elements, axis=0)
    std = numpy.std(elements, axis=0)

    # boundry dictating when outliers start. 2 stds is the typical normal distribution
    stdthreshold = 2

    # remove upper bound
    final_list = [x for x in dataArray if (x > mean - stdthreshold * std)]
    # remove lower bounds
    final_list = [x for x in final_list if (x < mean + stdthreshold * std)]

    return final_list


def get_statistics(videoArray):
    # there must be a more elegant way to do this....
    viewCountArray = []
    likeCountArray = []
    dislikeCountArray = []
    favoriteCountArray = []
    commentCountArray = []
    categoryIdArray = []

    # get all resulting numbers
    for video in videoArray:
        viewCountArray.append(video.viewCount)
        likeCountArray.append(video.likeCount)
        dislikeCountArray.append(video.dislikeCount)
        favoriteCountArray.append(video.favoriteCount)
        commentCountArray.append(video.commentCount)
        categoryIdArray.append(video.categoryId)

    viewCountArray = removeOutliers(viewCountArray)
    likeCountArray = removeOutliers(likeCountArray)
    dislikeCountArray = removeOutliers(dislikeCountArray)
    favoriteCountArray = removeOutliers(favoriteCountArray)
    commentCountArray = removeOutliers(commentCountArray)

    # notes - looking at average only does not account for variance...i should account for it at some point
    viewsAverage = numpy.average(viewCountArray)
    likesAverage = numpy.average(likeCountArray)
    dislikeAverage = numpy.average(dislikeCountArray)

    favoriteAverage = numpy.average(favoriteCountArray)
    if str(favoriteAverage) == 'nan':
        favoriteAverage = 0
        # print('nanChange')
    else:
        print('no change')

    commentAverage = numpy.average(commentCountArray)
    engagementAverage = (likesAverage + dislikeAverage + commentAverage + favoriteAverage) / viewsAverage

    # check if there are values inside mostCommonCategoryId
    if len(categoryIdArray) > 0:
        mostCommonCategoryId = max(categoryIdArray, key=categoryIdArray.count)
    else:
        mostCommonCategoryId = 000



    return [viewsAverage, likesAverage, dislikeAverage, favoriteAverage, commentAverage, engagementAverage, mostCommonCategoryId]



def runStats(creatorId):
    videoArray = get_saved_videos(creatorId)
    stats_array = get_statistics(videoArray)

    creator_stats = Channel_statistics(
        creatorId=creatorId,
        viewsAverage=stats_array[0],
        likesAverage=stats_array[1],
        dislikeAverage=stats_array[2],
        favoritesAverage=stats_array[3],
        commentsAverage=stats_array[4],
        engagementRate=stats_array[5],
        sampleSize=len(videoArray),
        dateRecorded=datetime.datetime.now(),
        categoryId=stats_array[6]
    )

    # this is clogging up the terminal
    # print(creator_stats)

    connection = sqlite3.connect('core.db')
    c = connection.cursor()

    valueList = [
        creator_stats.creatorId,
        creator_stats.viewAverage,
        creator_stats.likesAverage,
        creator_stats.dislikeAverage,
        creator_stats.favoritesAverage,
        creator_stats.commentsAverage,
        creator_stats.engagementRate,
        creator_stats.sampleSize,
        creator_stats.dateRecorded,
        creator_stats.categoryId
    ]

    # THIS IS AN OVERRIDE, updates channel statistics
    c.execute("INSERT OR REPLACE INTO creator_stats VALUES (?,?,?,?,?,?,?,?,?,?)", valueList)

    connection.commit()
    connection.close()


# runStats('UCvLT8V6syfFU5AETDM4CtpA')

# videos = get_saved_videos('UCvLT8V6syfFU5AETDM4CtpA')
# get_statistics(videos)


"""

note, json returns an ARRAY OF ARRAYS 

    "nbxhvz_VCFE", 0 videoId
    "UCvLT8V6syfFU5AETDM4CtpA", 1 CreatorId 
    "2018-04-19T04:15:57.000Z", 2 published date
    "Kai Sallas | Kaniela Stewart | Queens Surf Break, Waikiki Beach", 3 title
    "blankForNow", 4 videoTags
    7350, 5 viewCount
    158, 6 likeCount
    4, 7 dislikeCount
    0, 8 favoriteCount
    20 9 commentCount

"""
