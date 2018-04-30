import base_youtube_code
import keyword_search
import get_channel_videos
import video_statistics
import get_channel_stats
import sqlite3

# run file to start function flow



kw = keywords = [
    'liquid cooling vs air cooling',
    'liquid cool pc build',
'easy computer build',
'gaming mouse vs normal mouse',
'gaming mouse review',
'gaming mouse and keyboard',
'gaming mouse for fortnite',
'gaming mouse with number pad',
'logitech gaming mouse review',
'evga review',
'gaming monitor  review',
'gaming monitor under 100',
'gaming monitor setup',
'best gaming monitor',
'4k gaming monitor review',
'top gaming monitors',
'',






]

if __name__ == '__main__':
    base_youtube_code.os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = base_youtube_code.get_authenticated_service()
    # NEED TO PASS IN CLIENT INTO FUNCTIONS!

    # get a list of channel IDs related to keywork

    for keyword in kw:
        channelId_list = keyword_search.run_keyword_search(client,keyword)

        # if channelId exist in database:
        # do not run

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
                videoId_list = get_channel_videos.run_get_channel_videos(client, channelId)
                for videoId in videoId_list:
                    video_statistics.run_video_statistics(client, videoId)
                get_channel_stats.runStats(channelId)





        # else:
        # run

        # get list of videos related to channel ID
        # for channelId in channelId_list:
        #     videoId_list = get_channel_videos.run_get_channel_videos(client, channelId)
        #     for videoId in videoId_list:
        #         video_statistics.run_video_statistics(client, videoId)
        #     get_channel_stats.runStats(channelId)







