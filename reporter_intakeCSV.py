import csv
import base_youtube_code
import video_statistics
import keyword_search
from Models.Video import Video
import helpers




"""
- intake CSV
- read CSV data
- get landing_referer data
- split on watch?v

- run the individual video statistics 
- run the channel level statistics 

"""




def readYoutubeReferrals(csvPath):
    f = open(csvPath)

    csv_f = csv.reader(f)

    utm_url_pairings_array = []

    firstline = True
    # the following converts readData into pythonData
    for row in csv_f:
        if firstline:
            firstline = False
            continue
        # create an object from row

        utm_term = str(row[0])

        full_youtube_url = str(row[4])
        splitter = full_youtube_url.split('watch?v=')
        dirtyPossibleVidId = splitter[1]
        cleanerVidId = dirtyPossibleVidId.split('&')
        vidId = cleanerVidId[0]

        pairing = [utm_term, vidId]
        # print(pairing)
        utm_url_pairings_array.append(pairing)

    print('read csv')
    return utm_url_pairings_array

# [UTM , URL]


def get_vid_stats_without_db(client, utm_url_pairings):

    full_data = []

    for pairing in utm_url_pairings:
        videoId = pairing[1]

        raw_video_data = video_statistics.videos_list_by_id(client,
                                                            part='snippet,contentDetails,statistics',
                                                            id=videoId)

        # checks for invalid data, this would never happen though but i'm too lazy to take this out
        if 'viewCount' in raw_video_data["statistics"]:
            viewCount = raw_video_data["statistics"]['viewCount']
        else:
            # print('like count hidden')
            viewCount = 0

        if 'likeCount' in raw_video_data["statistics"]:
            likeCount = raw_video_data["statistics"]['likeCount']
        else:
            # print('like count hidden')
            likeCount = 0

        if 'dislikeCount' in raw_video_data["statistics"]:
            dislikeCount = raw_video_data["statistics"]['dislikeCount']
        else:
            # print('dislike count hidden')
            dislikeCount = 0

        if 'commentCount' in raw_video_data["statistics"]:
            commentCount = raw_video_data["statistics"]['commentCount']
        else:
            # print('commentCount count hidden')
            commentCount = 0

        create_video = Video(videoId=raw_video_data['id'],
                             creatorId=raw_video_data['snippet']['channelId'],
                             publishedAt=raw_video_data['snippet']['publishedAt'],
                             title=raw_video_data['snippet']['title'],
                             videoTags='placeholder',
                             # videoTags=raw_video_data['snippet']['tags'],
                             viewCount=viewCount,

                             # need to perform check if likeCount exists
                             likeCount=likeCount,

                             dislikeCount=dislikeCount,
                             favoriteCount=raw_video_data["statistics"]['favoriteCount'],
                             commentCount=commentCount,
                             categoryId=raw_video_data['snippet']['categoryId'])

        videoChannelStatisticsQuery = keyword_search.channels_list_by_id(client,
                                                          part='snippet,contentDetails,statistics',
                                                          id=create_video.creatorId)

        creator_sub_count = videoChannelStatisticsQuery['statistics']['subscriberCount']
        creator_title = videoChannelStatisticsQuery['snippet']['title']

        print([pairing[0],pairing[1],creator_title,creator_sub_count,create_video.publishedAt,create_video.title,create_video.viewCount, create_video.likeCount,create_video.commentCount,create_video.dislikeCount])


        full_data.append([pairing[0],pairing[1],creator_title,creator_sub_count,create_video.publishedAt,create_video.title,create_video.viewCount, create_video.likeCount,create_video.commentCount,create_video.dislikeCount])

    return full_data




def writeCSV(csvPath, masterDataArray):
    with open(csvPath, 'w', encoding='utf-8') as csvfile:
        fieldnames = ['channel name','sub count','UTM', 'video title', 'vid ID', 'date live','views', 'comments','likes','dislikes','total engagement','engagement rate', 'views/sub']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for campaign in masterDataArray:
            dumbo_format = {
                'channel name': campaign[2],
                'sub count': campaign[3],
                'UTM': campaign[0],
                'video title':campaign[5],
                'vid ID':campaign[1],
                'date live': campaign[4],
                'views': campaign[6],
                'comments':campaign[8],
                'likes':campaign[7],
                'dislikes':campaign[9],
                'total engagement': 'hodl',
                'engagement rate':'hodl',
                'views/sub':'hodl'
            }

            writer.writerow(dumbo_format)

        print('exported')














client = base_youtube_code.get_authenticated_service()
# input form
path = '/Users/michaelninh/PycharmProjects/inventus/csvRaws/8%2F6 - 8%2F12 - utms_utube.csv'
pairings = readYoutubeReferrals(path)
master_data = get_vid_stats_without_db(client, pairings)
writeCSV('/Users/michaelninh/PycharmProjects/inventus/exports/weeklyanalysis1.csv',master_data)




"""
# [pairing[0] (UTM), 0 
# pairing[1] (URL), 1
# creator_title, 2
# creator_sub_count, 3
# create_video.publishedAt, 4
# create_video.title, 5 
# create_video.viewCount, 6
# create_video.likeCount, 7
# create_video.commentCount, 8
# create_video.dislikeCount 9

"""


