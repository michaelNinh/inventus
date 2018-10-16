import sqlite3
import json



connection = sqlite3.connect('core.db')
c = connection.cursor()

# c.execute("""
#
# UPDATE creator
# SET reachOut = 5
# WHERE creatorId = 'UC2jao3bBO9EV3-PF7r2CtQA'
#
# """)


c.execute(
    """
    SELECT date_last_video
    FROM creator_stats
    WHERE creatorId = 'UCXuqSBlHAE6Xw-yeJA0Tunw'
    
    """
)


test = c.fetchall()
print(test)

# need to modify, videoId should be an array

# c.execute("""DROP TABLE IF EXISTS creator""")

# command to create a table
# c.execute("""CREATE TABLE creator(
#             channelTitle TEXT,
#             creatorId TEXT PRIMARY KEY,
#             totalSubs INT,
#             totalViews INT,
#             vidIds TEXT,
#             email TEXT,
#             totalComments INT,
#             videoCount INT,
#             keywords TEXT,
#             reachOut INT
#             )""")
#
#
# c.execute("""CREATE TABLE video(
#             videoId TEXT PRIMARY KEY,
#             creatorId TEXT NOT NULL REFERENCES creator(channelId),
#             publishedAt TEXT,
#             title TEXT,
#             videoTags TEXT,
#             viewCount INT,
#             likeCount INT,
#             dislikeCount INT,
#             favoriteCount INT,
#             commentCount INT,
#             categoryIId INT
#             )""")

#
# c.execute("""
#
# CREATE TABLE creator_stats(
# creatorId TEXT PRIMARY KEY NOT NULL REFERENCES creator(channelId),
# viewsAverage REAL,
# likesAverage REAL,
# dislikeAverage REAL,
# favoritesAverage REAL,
# commentsAverage REAL,
# engagementRate REAL,
# sampleSize REAL,
# dataRecorded TEXT
# date_last_video TEXT)
#
# """)

#
# c.execute("""
#
# DROP TABLE creator_stats
#
#  """)

# c.execute("SELECT * FROM creator_stats")
# c.execute("SELECT * FROM video")
# c.execute("SELECT * FROM creator")


# test channelID UCvLT8V6syfFU5AETDM4CtpA


# pull all saved videos related to creator
# c.execute("""
# SELECT * FROM video
# where creatorID = 'UCvLT8V6syfFU5AETDM4CtpA'
# """)

# this will output all videos related to creatorId TOGETHER
# c.execute("""
# SELECT * FROM creator
# JOIN video on creator.channelId = video.creatorId
# """)

# build a customized creator_stats report with this template
# c.execute("""
# SELECT creatorId, channelTitle ,email, keywords, viewsAverage,engagementRate,dataRecorded
# FROM creator
# JOIN creator_stats on creator.channelId = creator_stats.creatorId
# """)



# print(json.dumps(c.fetchall(),indent=2))
#
# testCreatorId = 'UCvLT8V6syfFUzzzzz5AETDM4CtpA'
# # stringCommand = 'SELECT count(*) FROM creator WHERE creatorId = {}'.format(testCreatorId)
# # print(stringCommand)
# # c.execute(stringCommand)
#
# # c.execute("""
# #
# #         SELECT count(*)
# #         FROM creator
# #         WHERE creatorId = {}
# #
# #         """).__format__(testCreatorId)
#
#
# creatorIdTuple = (testCreatorId,)
#
# c.execute("""
#     SELECT * FROM video
#     WHERE creatorID = ?
#     """, creatorIdTuple)
#
# testResult =  c.fetchall()


connection.commit()
connection.close()



'''
find videos where related Creator.Video Tags == "kpop'

'''