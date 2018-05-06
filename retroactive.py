import base_youtube_code
import keyword_search
import get_channel_videos
import video_statistics
import get_channel_stats
import sqlite3
import json
import retro_video_statistics

"""
flow of logic
Get all country codes
    - get all videoIds from database
    - API connection to get country code
    - update database item with country code
    
    
Get categoryIds
    - get all creators
    - Get all video ids from database related to creator 
    - API connection to get countrycode
    - update videos with categoryIDS
    - run channel statistics 
"""


def get_existing_channnel():
    connection = sqlite3.connect('core.db')
    c = connection.cursor()
    c.execute(
        """
        SELECT creatorId FROM video
        WHERE LENGTH(categoryIId) > 3
        
        """
    )

    channelIdTuple = c.fetchall()

    connection.commit()
    connection.close()
    return channelIdTuple


# test channel ID UC-3Oc4KY7pElZMbsWtm3X6A


def channels_list_by_id(client, **kwargs):
    # See full sample for function
    kwargs = base_youtube_code.remove_empty_kwargs(**kwargs)

    response = client.channels().list(
        **kwargs
    ).execute()

    return response['items'][0]


def getCountryCode(channelIdTuple):
    client = base_youtube_code.get_authenticated_service()

    # for each channelId, connect to youtube API and get the countryCode
    for channelId in channelIdTuple:

        print(channelId)
        countryApiConnect = channels_list_by_id(client, part='snippet,contentDetails,statistics',
                                                id=channelId[0])

        # check if country data exists in snipppet
        if 'country' in countryApiConnect["snippet"]:
            countryInput = countryApiConnect["snippet"]['country']
            print(countryInput)
        else:
            print('no country detected')
            countryInput = 'n/a'

        print('UPDATING ' + channelId[0])

        connection = sqlite3.connect('core.db')
        c = connection.cursor()
        c.execute("UPDATE creator SET country=? WHERE creator.creatorId=?", (countryInput, channelId[0]))

        connection.commit()
        connection.close()


def updateCountry():
    channelIdArray = get_existing_channnel()
    getCountryCode(channelIdArray)


def updateCategory(creatorTuple):
    for creatorTuple in creatorTuple:
        print('updateing' + creatorTuple[0])
        get_channel_stats.runStats(creatorTuple[0])


def updateAllVideos(creatorIdTuple):
    client = base_youtube_code.get_authenticated_service()

    # given a list of creatorId, for each creator

    for creator in creatorIdTuple:
        print('updating creator' + creator[0])
        # get all videos related to creator
        connection = sqlite3.connect('core.db')
        c = connection.cursor()
        # SQLITE needs tuples for some reason?
        creatorIdTuple = (creator[0],)

        c.execute("""
            SELECT videoId FROM video
            WHERE creatorID = ?
            """, creatorIdTuple)

        # get list of all videoIds that need updating
        rawVideoTuple = c.fetchall()

        connection.commit()
        connection.close()

        for videoId in rawVideoTuple:
            print("updating video " + videoId[0])
            retro_video_statistics.run_video_statistics(client, videoId[0])




# this should update the category Id
# updateCategory(get_existing_channnel())

# should re-scrape all the videos and update category Id
updateAllVideos(get_existing_channnel())

# now need to update all the videos using get_channel_stats