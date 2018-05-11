import base_youtube_code
import keyword_search
import get_channel_videos
import video_statistics
import get_channel_stats
import sqlite3

# run file to start function flow



kw = keywords = [

'bloodborne pro guide',
'bloodborne pro tutorial',
'bloodborne pro strategy',
'bloodborne pro methods',
'bloodborne pro lessons',
'bloodborne pro techniques',
'bloodborne pro videos',
'bloodborne pro lessons',
'bloodborne pro tactics',
'bloodborne pro overview',
'bloodborne pro tips and trick',
'bloodborne pro gameplay',
'bloodborne pro common mistakes',
'bloodborne pro builds',
'bloodborne pro players',
'bloodborne pro noobs',
'bloodborne pro news',
'bloodborne pro tutorial',
'GTA 5 beginner guide',
'GTA 5 beginner tutorial',
'GTA 5 beginner strategy',
'GTA 5 beginner methods',
'GTA 5 beginner lessons',
'GTA 5 beginner techniques',
'GTA 5 beginner videos',
'GTA 5 beginner lessons',
'GTA 5 beginner tactics',
'GTA 5 beginner overview',
'GTA 5 beginner tips and trick',
'GTA 5 beginner gameplay',
'GTA 5 beginner common mistakes',
'GTA 5 beginner builds',
'GTA 5 beginner players',
'GTA 5 beginner noobs',
'GTA 5 beginner news',
'GTA 5 tutorial',
'GTA 5 intermediate guide',
'GTA 5 intermediate tutorial',
'GTA 5 intermediate strategy',
'GTA 5 intermediate methods',
'GTA 5 intermediate lessons',
'GTA 5 intermediate techniques',
'GTA 5 intermediate videos',
'GTA 5 intermediate lessons',
'GTA 5 intermediate tactics',
'GTA 5 intermediate overview',
'GTA 5 intermediate tips and trick',
'GTA 5 intermediate gameplay',
'GTA 5 intermediate common mistakes',
'GTA 5 intermediate builds',
'GTA 5 intermediate players',
'GTA 5 intermediate noobs',
'GTA 5 intermediate news',
'GTA 5 intermediate tutorial',
'GTA 5 expert guide',
'GTA 5 expert tutorial',
'GTA 5 expert strategy',
'GTA 5 expert methods',
'GTA 5 expert lessons',
'GTA 5 expert techniques',
'GTA 5 expert videos',
'GTA 5 expert lessons',
'GTA 5 expert tactics',
'GTA 5 expert overview',
'GTA 5 expert tips and trick',
'GTA 5 expert gameplay',
'GTA 5 expert common mistakes',
'GTA 5 expert builds',
'GTA 5 expert players',
'GTA 5 expert noobs',
'GTA 5 expert news',
'GTA 5 expert tutorial',
'GTA 5 pro guide',
'GTA 5 pro tutorial',
'GTA 5 pro strategy',
'GTA 5 pro methods',
'GTA 5 pro lessons',
'GTA 5 pro techniques',
'GTA 5 pro videos',
'GTA 5 pro lessons',
'GTA 5 pro tactics',
'GTA 5 pro overview',
'GTA 5 pro tips and trick',
'GTA 5 pro gameplay',
'GTA 5 pro common mistakes',
'GTA 5 pro builds',
'GTA 5 pro players',
'GTA 5 pro noobs',
'GTA 5 pro news',
'GTA 5 pro tutorial',


    ]

if __name__ == '__main__':
    base_youtube_code.os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = base_youtube_code.get_authenticated_service()
    # NEED TO PASS IN CLIENT INTO FUNCTIONS!

    # get a list of channel IDs related to keywork

    for keyword in kw:
        print('keyword is: '+ keyword)
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




