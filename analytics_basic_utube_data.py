import csv
import base_youtube_code
import video_statistics
import keyword_search
from Models.Video import Video
import helpers
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



CLIENT_SECRETS_FILE = "client_secret.json"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def print_response(response):
    print(response)


# remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():  # iteritems should be .items?
            if value:
                good_kwargs[key] = value
    return good_kwargs





"""
- intake CSV
- read CSV data
- get landing_referer data
- split on watch?v

- run the individual video statistics 
- run the channel level statistics 

"""








def get_vid_stats_without_db(client, utm_url_pairings):
    """utm_url_parings is formed as [UTM, videoID]"""

    full_data = []

    for pairing in utm_url_pairings:

        videoURL = utm_url_pairings[1]
        splitter = videoURL.split('watch?v=')
        dirtyPossibleVidId = splitter[1]
        cleanerVidId = dirtyPossibleVidId.split('&')
        videoId = cleanerVidId[0]

        raw_video_data = video_statistics.videos_list_by_id(client,
                                                            part='snippet,contentDetails,statistics',
                                                            id=videoId)

        #check for invalid data
        if 'viewCount' in raw_video_data["statistics"]:
            viewCount = raw_video_data["statistics"]['viewCount']
        else:
            viewCount = 0

        if 'likeCount' in raw_video_data["statistics"]:
            likeCount = raw_video_data["statistics"]['likeCount']
        else:
            likeCount = 0

        if 'dislikeCount' in raw_video_data["statistics"]:
            dislikeCount = raw_video_data["statistics"]['dislikeCount']
        else:
            dislikeCount = 0

        if 'commentCount' in raw_video_data["statistics"]:
            commentCount = raw_video_data["statistics"]['commentCount']
        else:
            commentCount = 0


        # convert this into JSON
        create_video = Video(videoId=raw_video_data['id'],
                             creatorId=raw_video_data['snippet']['channelId'],
                             publishedAt=raw_video_data['snippet']['publishedAt'],
                             title=raw_video_data['snippet']['title'],
                             videoTags=raw_video_data['snippet']['tags'],
                             viewCount=viewCount,
                             likeCount=likeCount,
                             dislikeCount=dislikeCount,
                             favoriteCount=raw_video_data["statistics"]['favoriteCount'],
                             commentCount=commentCount,
                             categoryId=raw_video_data['snippet']['categoryId'])

        # getting some information about the creator channel
        videoChannelStatisticsQuery = keyword_search.channels_list_by_id(client,
                                                          part='snippet,contentDetails,statistics',
                                                          id=create_video.creatorId)

        creator_sub_count = videoChannelStatisticsQuery['statistics']['subscriberCount']
        creator_title = videoChannelStatisticsQuery['snippet']['title']

        print([pairing[0],pairing[1],creator_title,creator_sub_count,create_video.publishedAt,create_video.title,create_video.viewCount, create_video.likeCount,create_video.commentCount,create_video.dislikeCount])

        full_data.append([pairing[0],pairing[1],creator_title,creator_sub_count,create_video.publishedAt,create_video.title,create_video.viewCount, create_video.likeCount,create_video.commentCount,create_video.dislikeCount])

    return full_data




client = base_youtube_code.get_authenticated_service()
















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


