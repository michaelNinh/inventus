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
    channelId_list = keyword_search.run_keyword_search(client)

    # get list of videos related to channel ID
    for channelId in channelId_list:
        videoId_list = get_channel_videos.run_get_channel_videos(client, channelId)
        for videoId in videoId_list:
            video_statistics.run_video_statistics(client,videoId)
        print('running channel stats')
        get_channel_stats.runStats(channelId)








