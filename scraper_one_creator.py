import base_youtube_code
import keyword_search
import video_statistics
import get_channel_stats
import get_channel_videos
from Models.Creator import Creator, Video
import json
import sqlite3

# run file to start function flow
if __name__ == '__main__':
    base_youtube_code.os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = base_youtube_code.get_authenticated_service()
    # NEED TO PASS IN CLIENT INTO FUNCTIONS!

    # get a list of channel IDs related to keywork

    # there is no channel being created

    # if does not exist, needs to enter into DB
    channelId = 'UCPzw9Ttu0nFbB_0l1QFRBtA'

    # obtain a list of video IDs here
    recent_video_ids = get_channel_videos.run_get_channel_videos(client, channelId)


    channelData = keyword_search.channels_list_by_id(client,
                                       part='snippet,contentDetails,statistics',
                                       id=channelId)



    # print(channelData)


    print(json.dumps(channelData, indent=2))

    # check if country data exists in snipppet
    if 'country' in channelData["snippet"]:
        countryInput = channelData["snippet"]['country']
    else:
        # print('dislike count hidden')
        countryInput = 'country not detected'

    create_creatorObject = Creator(channelTitle=channelData['snippet']['title'],
                                   creatorId=channelId,
                                   totalSubscribers=channelData['statistics']['subscriberCount'],
                                   totalViews=channelData['statistics']['viewCount'],
                                   availableVideoIds=recent_video_ids[0],
                                   email='testEmail',
                                   totalComments=channelData['statistics']['commentCount'],
                                   videoCount=channelData['statistics']['videoCount'],
                                   discoveryKeyword='custom id input',
                                   reachOut='gtoofast',
                                   country=countryInput,
                                   notes='no notes'
                                   )
    print(create_creatorObject)

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
                  'notes': create_creatorObject.notes,
                  'approval': 0

              })

    connection.commit()
    connection.close()

    for videoId in recent_video_ids:
        video_statistics.run_video_statistics(client,videoId)

    get_channel_stats.runStats(channelId)


