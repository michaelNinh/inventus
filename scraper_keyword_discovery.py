import base_youtube_code
import keyword_search
import get_channel_videos
import video_statistics
import get_channel_stats
import sqlite3

# run file to start function flow



kw = keywords = ['overwatch tips',
'overwatch',
'overwatch league',
'overwatch gameplay',
'overwatch new hero',
'overwatch tips and tricks',
'overwatch tips for beginners',
'overwatch tips for competitive',
'overwatch tips and trick advanced',
'overwatch tips for genji',
'overwatch tip for every hero',
'overwatch tips for tracer',
'overwatch tips for mccree',
'overwatch tips for solder 76',
'pro overwatch tips',
'pro overwatch',
'pro overwatch players',
'pro overwatch highlights',
'pro overwatch match',
'pro overwatch plays',
'pro overwatch settings',
'pro overwatch vods',
'Ryzen 2',
'ultra wide display',
'home audio',
'home audio set',
'home cinema set',
'home audiophile',
'budget audiophile',
'MSi monitor',
'steel series review',
'GPU review',
'corsair keyboard review',
'pubG gameplay',
                 'pubg tips',
'pubg tips and tricks',
'pubg xbox',
'pubg tips and tricks xbox',
'pubg tips for beginners',
'pubg tips advanced',
'pubg xbox 1',
'pubg tips pc',
'pubg tips mobile',
'pubg tips and tricks pc ',
'fortnite strategy',
'fortnite strategies and tips',
'fortnite strats',
'fortnite strategy solo',
'fortnite strategy duo',
'fortnite strategy ps4 ',
'fortnite strategy squad',
'fortnite strategy xbox',



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




