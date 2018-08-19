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


# given a video ID, get the channel associated with it
def channels_list_by_id(client, **kwargs):
    # See full sample for function
    kwargs = base_youtube_code.remove_empty_kwargs(**kwargs)

    response = client.channels().list(
        **kwargs
    ).execute()

    # print(response['items'])
    # sometimes response will be []

    if len(response['items']) == 0:
        pass
    else:
        return response['items'][0]


def run_keyword_search(client, keyword):
    """ returns an array of STR channel Ids"""

    # keywordSearch = input('enter keyword search: ')

    # find all videos by keyword
    video_results_array = search_list_by_keyword(client,
                                                 part='snippet',
                                                 maxResults=50,
                                                 q=keyword,
                                                 type=''
                                                 )

    channelIdArray = []

    for video in video_results_array:

        if 'videoId' in video["id"]:
            availableVideoId = video['id']['videoId']
            # print(availableVideoId)
        else:
            # print('missing video ID')
            availableVideoId = 'notavailable'


        # for each video, find the channel statistics
        videoChannelStatisticsQuery = channels_list_by_id(client,
                                                          part='snippet,contentDetails,statistics',
                                                          id=video['snippet']['channelId'])

        # print(videoChannelStatisticsQuery)


        # print(videoChannelStatisticsQuery['snippet'])
        # there is a huge error going on here...None Type?
        if 'country' in videoChannelStatisticsQuery['snippet']:
                countryInput = videoChannelStatisticsQuery['snippet']['country']
        else:
                # print('dislike count hidden')
                countryInput = 'country not detected'



        # IMPORTANT #############################
        ########################################## MODIFY REACH OUT CODES HERE
        # this is the creation of a WHOLE NEW CREATOR OBJECT
        # IMPORTANT #############################
        # IMPORTANT #############################
        # IMPORTANT #############################
        # IMPORTANT #############################
        # IMPORTANT #############################
        # IMPORTANT #############################

        '''IMPORTANT  '''

        # IMPORTANT #############################
        # IMPORTANT #############################
        # IMPORTANT #############################
        # IMPORTANT #############################
        create_creatorObject = Creator(channelTitle=video['snippet']['channelTitle'],
                                       creatorId=video['snippet']['channelId'],
                                       totalSubscribers=videoChannelStatisticsQuery['statistics']['subscriberCount'],
                                       totalViews=videoChannelStatisticsQuery['statistics']['viewCount'],
                                       availableVideoIds=availableVideoId,
                                       email='testEmail',
                                       totalComments=videoChannelStatisticsQuery['statistics']['commentCount'],
                                       videoCount=videoChannelStatisticsQuery['statistics']['videoCount'],
                                       discoveryKeyword=keyword,

                                       reachOut='11',

                                       country=countryInput,
                                       notes='no notes'
                                       )


        channelIdArray.append(create_creatorObject.creatorId)

        connection = sqlite3.connect('core.db')
        c = connection.cursor()

        # save into DB
        # this does NOT UPDATE EXISTING CREATOR STATS - THIS NEEDS TO BE FIXED!
        c.execute("INSERT OR IGNORE INTO creator VALUES ("
                  ":channelTitle, "
                  ":creatorId, "
                  ":totalSubs, "
                  ":totalViews, "
                  ":vidIds, "
                  ":email, "
                  ":totalComments, "
                  ":videoCount, "
                  ":keywords,"
                  ":reachOut,"
                  ":country,"
                  ":notes,"
                  ":approval)",
                  {
                      'channelTitle': create_creatorObject.channelTitle,
                      'creatorId': create_creatorObject.creatorId,
                      'totalSubs': create_creatorObject.totalSubscribers,
                      'totalViews': create_creatorObject.totalViews,
                      'vidIds': create_creatorObject.availableVideosIds,
                      'email': create_creatorObject.email,
                      'totalComments': create_creatorObject.totalComments,
                      'videoCount': create_creatorObject.videoCount,
                      'keywords': create_creatorObject.discoveryKeyword,
                      'reachOut': create_creatorObject.reachOut,
                      'country': create_creatorObject.country,
                      'notes':create_creatorObject.notes,
                      'approval':0

                  })

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



testData =  {
        "title": "Jeff Chavolla",
        "description": "I want to inspire and be inspired\nCinematographer \nPhotographer\nEditor\n\nWebsite: http://www.JeffChavolla.com\nEmail: JeffChavolla@gmail.com\nDonate: https://paypal.me/JeffChavolla\n\nSubscribe!",
        "customUrl": "jeffchavolla",
        "publishedAt": "2014-10-21T00:19:52.000Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/-jmaP8NuzjqQ/AAAAAAAAAAI/AAAAAAAAAAA/O0YmloF15KU/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/-jmaP8NuzjqQ/AAAAAAAAAAI/AAAAAAAAAAA/O0YmloF15KU/s240-c-k-no-mo-rj-c0xffffff/photo.jpg",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/-jmaP8NuzjqQ/AAAAAAAAAAI/AAAAAAAAAAA/O0YmloF15KU/s800-c-k-no-mo-rj-c0xffffff/photo.jpg",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "Jeff Chavolla",
          "description": "I want to inspire and be inspired\nCinematographer \nPhotographer\nEditor\n\nWebsite: http://www.JeffChavolla.com\nEmail: JeffChavolla@gmail.com\nDonate: https://paypal.me/JeffChavolla\n\nSubscribe!"
        },
        "country": "US"
      }


# test channel ID = UC-Zt7GPzlrPPQexkG9-shPg

# def test():
#         # for each video, find the channel statistics
#         client = base_youtube_code.get_authenticated_service()
#         videoChannelStatisticsQuery = channels_list_by_id(client,
#                                                           part='snippet,contentDetails,statistics',
#                                                           id='UC-Zt7GPzlrPPQexkG9-shPg')
#
#         # check if country data exists in snipppet
#         if 'country' in videoChannelStatisticsQuery["snippet"]:
#             countryInput = videoChannelStatisticsQuery["snippet"]['country']
#         else:
#             print('dislike count hidden')
#             countryInput = 'country not detected'
#
#         # this is the creation of a WHOLE NEW CREATOR OBJECT
#         create_creatorObject = Creator(channelTitle='test',
#                                        creatorId='test',
#                                        totalSubscribers=videoChannelStatisticsQuery['statistics']['subscriberCount'],
#                                        totalViews=videoChannelStatisticsQuery['statistics']['viewCount'],
#                                        availableVideoIds='test',
#                                        email='testEmail',
#                                        totalComments=videoChannelStatisticsQuery['statistics']['commentCount'],
#                                        videoCount=videoChannelStatisticsQuery['statistics']['videoCount'],
#                                        discoveryKeyword='test',
#                                        reachOut=0,
#                                        country=countryInput,
#                                        notes='no notes'
#                                        )
#
#
#         print(create_creatorObject)
#
#
# test()