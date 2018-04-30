import base_youtube_code
from Models.Video import Video
import sqlite3


# youtube API function to get individual video statistics
def videos_list_by_id(client, **kwargs):
    kwargs = base_youtube_code.remove_empty_kwargs(**kwargs)

    response = client.videos().list(
        **kwargs
    ).execute()

    return response['items'][0]


# print_response(response['items'])

def run_video_statistics(client, videoId):
    raw_video_data = videos_list_by_id(client,
                                       part='snippet,contentDetails,statistics',
                                       id=videoId)

    # print(json.dumps(raw_video_data,indent=2))

    # testObject = raw_video_data["snippet"]["tags"]
    # print(testObject)

    # need to create the correct video object here
    print('creating video object for ' + videoId)

    # sometimes creators hide certain stats. need to check if certain stat is pullable

    if 'likeCount' in raw_video_data["statistics"]:
        likeCount = raw_video_data["statistics"]['likeCount']
    else:
        print('like count hidden')
        likeCount = 0

    if 'dislikeCount' in raw_video_data["statistics"]:
        dislikeCount = raw_video_data["statistics"]['dislikeCount']
    else:
        print('dislike count hidden')
        dislikeCount = 0


    if 'commentCount' in raw_video_data["statistics"]:
        commentCount = raw_video_data["statistics"]['commentCount']
    else:
        print('commentCount count hidden')
        commentCount = 0

    create_video = Video(videoId=raw_video_data['id'],
                         creatorId=raw_video_data['snippet']['channelId'],
                         publishedAt=raw_video_data['snippet']['publishedAt'],
                         title=raw_video_data['snippet']['title'],
                         videoTags='placeholder',
                         # videoTags=raw_video_data['snippet']['tags'],
                         viewCount=raw_video_data["statistics"]['viewCount'],

                         # need to perform check if likeCount exists
                         likeCount=likeCount,

                         dislikeCount=dislikeCount,
                         favoriteCount=raw_video_data["statistics"]['favoriteCount'],
                         commentCount=commentCount,
                         categoryId=raw_video_data['snippet']['title'])

    # # save data into DB
    # # OPEN CONNECTION TO VIDEO DB
    connection = sqlite3.connect('core.db')
    c = connection.cursor()

    # should this be insert or place? will the video have immutable stats past the initial scrape?
    c.execute("INSERT OR IGNORE INTO video VALUES (:videoId, :creatorId, :publishedAt, :title, :videoTags, "
              ":viewCount, :likeCount, :dislikeCount, :favoriteCount, :commentCount, :categoryId)",
              {'videoId': create_video.videoId,
               'creatorId': create_video.creatorId,
               'publishedAt': create_video.publishedAt,
               'title': create_video.title,
               'videoTags': 'blankForNow',
               'viewCount': create_video.viewCount,
               'likeCount': create_video.likeCount,
               'dislikeCount': create_video.dislikeCount,
               'favoriteCount': create_video.favoriteCount,
               'commentCount': create_video.commentCount,
               'categoryId': create_video.categoryId,
               })

    print("video saved")

    connection.commit()
    connection.close()


#########

# data structure
sampleData = {
    "kind": "youtube#video",
    "etag": "\"ZG3FIn5B5vcHjQiQ9nDOCWdxwWo/Y_zjFdN-eS8QWMRJIZM8hi52dng\"",
    "id": "Ks-_Mh1QhMc",
    "snippet": {
        "publishedAt": "2012-10-01T15:27:35.000Z",
        "channelId": "UCAuUUnT6oDeKwE6v1NGQxug",
        "title": "Your body language may shape who you are | Amy Cuddy",
        "description": "Body language affects how others see us, but it may also change how we see ourselves. Social psychologist Amy Cuddy argues that \"power posing\" -- standing in a posture of confidence, even when we don't feel confident -- can boost feelings of confidence, and might have an impact on our chances for success. (Note: Some of the findings presented in this talk have been referenced in an ongoing debate among social scientists about robustness and reproducibility. Read Amy Cuddy's response here: http://ideas.ted.com/inside-the-debate-about-power-posing-a-q-a-with-amy-cuddy/)\n\nThe TED Talks channel features the best talks and performances from the TED Conference, where the world's leading thinkers and doers give the talk of their lives in 18 minutes (or less). Look for talks on Technology, Entertainment and Design -- plus science, business, global issues, the arts and more.\n\nFollow TED on Twitter: http://www.twitter.com/TEDTalks\nLike TED on Facebook: https://www.facebook.com/TED\n\nSubscribe to our channel: https://www.youtube.com/TED",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/Ks-_Mh1QhMc/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/Ks-_Mh1QhMc/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/Ks-_Mh1QhMc/hqdefault.jpg",
                "width": 480,
                "height": 360
            },
            "standard": {
                "url": "https://i.ytimg.com/vi/Ks-_Mh1QhMc/sddefault.jpg",
                "width": 640,
                "height": 480
            },
            "maxres": {
                "url": "https://i.ytimg.com/vi/Ks-_Mh1QhMc/maxresdefault.jpg",
                "width": 1280,
                "height": 720
            }
        },
        "channelTitle": "TED",
        "tags": [
            "Amy Cuddy",
            "TED",
            "TEDTalk",
            "TEDTalks",
            "TED Talk",
            "TED Talks",
            "TEDGlobal",
            "brain",
            "business",
            "psychology",
            "self",
            "success"
        ],
        "categoryId": "22",
        "liveBroadcastContent": "none",
        "defaultLanguage": "en",
        "localized": {
            "title": "Your body language may shape who you are | Amy Cuddy",
            "description": "Body language affects how others see us, but it may also change how we see ourselves. Social psychologist Amy Cuddy argues that \"power posing\" -- standing in a posture of confidence, even when we don't feel confident -- can boost feelings of confidence, and might have an impact on our chances for success. (Note: Some of the findings presented in this talk have been referenced in an ongoing debate among social scientists about robustness and reproducibility. Read Amy Cuddy's response here: http://ideas.ted.com/inside-the-debate-about-power-posing-a-q-a-with-amy-cuddy/)\n\nThe TED Talks channel features the best talks and performances from the TED Conference, where the world's leading thinkers and doers give the talk of their lives in 18 minutes (or less). Look for talks on Technology, Entertainment and Design -- plus science, business, global issues, the arts and more.\n\nFollow TED on Twitter: http://www.twitter.com/TEDTalks\nLike TED on Facebook: https://www.facebook.com/TED\n\nSubscribe to our channel: https://www.youtube.com/TED"
        },
        "defaultAudioLanguage": "en"
    },
    "contentDetails": {
        "duration": "PT21M3S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "true",
        "licensedContent": "true",
        "projection": "rectangular"
    },
    "statistics": {
        "viewCount": "14155455",
        "likeCount": "184249",
        "dislikeCount": "3521",
        "favoriteCount": "0",
        "commentCount": "6925"
    }
}


def test():
    # print(sampleData['snippet']['categoryId'])
    print(sampleData['snippet']['tags'])

# test()


#     additional notes


# alternative way to insert multiple values
# testList = [('videoId', 'creatorId')]
# c.executemany("INSERT INTO video VALUES (?,?)", testList)
