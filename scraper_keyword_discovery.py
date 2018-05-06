import base_youtube_code
import keyword_search
import get_channel_videos
import video_statistics
import get_channel_stats
import sqlite3

# run file to start function flow



kw = keywords = ['fountain pen review',
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
                print('new creator discovered')
                get_channel_stats.runStats(channelId)




