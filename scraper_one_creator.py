import base_youtube_code
import keyword_search
import get_channel_videos
import video_statistics
import get_channel_stats

# run file to start function flow
if __name__ == '__main__':
    base_youtube_code.os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = base_youtube_code.get_authenticated_service()
    # NEED TO PASS IN CLIENT INTO FUNCTIONS!

    # get a list of channel IDs related to keywork

    # if does not exist, needs to enter into DB
    channelId = 'UCnxQ8o9RpqxGF2oLHcCn9VQ'

    recent_video_ids = get_channel_videos.run_get_channel_videos(client, channelId)
    for videoId in recent_video_ids:
        video_statistics.run_video_statistics(client,videoId)

    get_channel_stats.runStats(channelId)



