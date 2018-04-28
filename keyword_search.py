import base_youtube_code
from Models.Creator import Creator, Video
import sqlite3


def search_list_by_keyword(client, **kwargs):
    kwargs = base_youtube_code.remove_empty_kwargs(**kwargs)

    response = client.search().list(
        **kwargs
    ).execute()

    # response is type DICT, results are nested under 'items'
    # return print(json.dumps(response, indent=2))

    # this returns the LIST of just video results
    # return print(json.dumps(response['items'], indent=2))

    return response['items']


def channels_list_by_id(client, **kwargs):
    # See full sample for function
    kwargs = base_youtube_code.remove_empty_kwargs(**kwargs)

    response = client.channels().list(
        **kwargs
    ).execute()

    return response['items'][0]['statistics']


def run_keyword_search(client):
    """ returns an array of STR channel Ids"""
    keywordSearch = input('enter keyword search: ')

    # find all videos by keyword
    video_results_array = search_list_by_keyword(client,
                                                 part='snippet',
                                                 maxResults=5,
                                                 q=keywordSearch,
                                                 type=''
                                                 )

    channelIdArray = []

    for video in video_results_array:
        # for each video, find the channel statistics
        videoChannelStatisticsQuery = channels_list_by_id(client,
                                                          part='snippet,contentDetails,statistics',
                                                          id=video['snippet']['channelId'])

        # create the whole channel object
        create_creatorObject = Creator(channelTitle=video['snippet']['channelTitle'],
                                       creatorId=video['snippet']['channelId'],
                                       totalSubscribers=videoChannelStatisticsQuery['subscriberCount'],
                                       totalViews=videoChannelStatisticsQuery['viewCount'],
                                       availableVideoIds=video['id']['videoId'],
                                       email='testEmail',
                                       totalComments=videoChannelStatisticsQuery['commentCount'],
                                       videoCount=videoChannelStatisticsQuery['videoCount'],
                                       discoveryKeyword=keywordSearch
                                       )

        channelIdArray.append(create_creatorObject.creatorId)

        connection = sqlite3.connect('core.db')
        c = connection.cursor()

        # save into DB
        c.execute("INSERT OR IGNORE INTO creator VALUES ("
                  ":channelTitle, "
                  ":creatorId, "
                  ":totalSubs, "
                  ":totalViews, "
                  ":vidIds, "
                  ":email, "
                  ":totalComments, "
                  ":videoCount, "
                  ":keywords)",
                  {
                      'channelTitle': create_creatorObject.channelTitle,
                      'creatorId': create_creatorObject.creatorId,
                      'totalSubs': create_creatorObject.totalSubscribers,
                      'totalViews': create_creatorObject.totalViews,
                      'vidIds': create_creatorObject.availableVideosIds,
                      'email': create_creatorObject.email,
                      'totalComments': create_creatorObject.totalComments,
                      'videoCount': create_creatorObject.videoCount,
                      'keywords': create_creatorObject.discoveryKeyword})

        connection.commit()
        connection.close()

    return channelIdArray

#########
#     additional notes


# alternative way to insert multiple values
# testList = [('videoId', 'creatorId')]
# c.executemany("INSERT INTO video VALUES (?,?)", testList)

# test_video = {
#             "kind": "youtube#searchResult",
#             "etag": "\"RmznBCICv9YtgWaaa_nWDIH1_GM/o7awYc7gIpr1NLZ1l9Y7GcTGuMQ\"",
#             "id": {
#                 "kind": "youtube#video",
#                 "videoId": "vk0F8dHo3wU"
#             },
#             "snippet": {
#                 "publishedAt": "2015-10-14T13:45:47.000Z",
#                 "channelId": "UC-Zt7GPzlrPPQexkG9-shPg",
#                 "title": "\"Pacific Dreams\" A California Surfing Film",
#                 "description": "\"Pacific Dreams\" is a surfing movie featuring my 2015 footage shot around the beautiful state of California. Filmed & Edited by Jeff Chavolla ( http://www.JeffChavolla.com) Camera Gear: Tripod:...",
#                 "thumbnails": {
#                     "default": {
#                         "url": "https://i.ytimg.com/vi/vk0F8dHo3wU/default.jpg",
#                         "width": 120,
#                         "height": 90
#                     },
#                     "medium": {
#                         "url": "https://i.ytimg.com/vi/vk0F8dHo3wU/mqdefault.jpg",
#                         "width": 320,
#                         "height": 180
#                     },
#                     "high": {
#                         "url": "https://i.ytimg.com/vi/vk0F8dHo3wU/hqdefault.jpg",
#                         "width": 480,
#                         "height": 360
#                     }
#                 },
#                 "channelTitle": "Jeff Chavolla",
#                 "liveBroadcastContent": "none"
#             }
#         }

# test_channel_statistics = {
#   "viewCount": "131149433",
#   "commentCount": "393",
#   "subscriberCount": "1384453",
#   "hiddenSubscriberCount": false,
#   "videoCount": "4614"
# }
