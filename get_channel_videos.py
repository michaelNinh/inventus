import base_youtube_code

# youtube API function to most recent activities. check for most recent uploads
def activities_list(client, **kwargs):
  # See full sample for function
  kwargs = base_youtube_code.remove_empty_kwargs(**kwargs)

  response = client.activities().list(
    **kwargs
  ).execute()

  return response['items']

# this need a list of channel IDs to work
def run_get_channel_videos(client, channelId):
    results = activities_list(client,
                              part='snippet,contentDetails',
                              channelId=channelId,
                              maxResults=25)
    # results are returned as an array of Dicts
    # print(json.dumps(results,indent=2))


    # iterate over results array
    # if contentType = upload
    # grab video Id, put into array
    # apply video_statistics to each videoId in array
    # create video objects and add to DB

    recent_videoIds = []

    for activity in results:
        if activity['snippet']['type'] == 'upload':
            recent_videoIds.append(activity['contentDetails']['upload']['videoId'])
        else:
            continue
            # print('not video upload')


    # print(recent_videoIds)

    return recent_videoIds






#########

# data structure

# testData = {
#         "kind": "youtube#activity",
#         "etag": "\"ZG3FIn5B5vcHjQiQ9nDOCWdxwWo/lHfeYV2XghiIjHZRqR2GyTIk1p4\"",
#         "id": "VTE1MjQyNTA5MTc5NDYxMDUwNzg0NjYwOA==",
#         "snippet": {
#             "publishedAt": "2018-04-20T19:01:57.000Z",
#             "channelId": "UCPXhP-T9ROJ8luLezbGvvhQ",
#             "title": "TOP APRIL FAVORITES 2018 | BABSBEAUTY",
#             "description": "Native Deodorant - https://tinyurl.com/y8p4wz75\nCode SPRING20 to save 20%\n\nFOLLOW ME:\nInstagram: https://www.instagram.com/babsbeauty_/\nSnapchat: Babsbeauty2014\n\n\ud83d\udcb0** EBATES How I Get Money back when I Shop Online\ud83d\udcb0\n---In order to get Cash Back, you have to shop through Ebates website\nhttp://tinyurl.com/nbxwhg2\n\n-------------------------------------------------------------------------------\n\nAFFILIATE COUPON CODES:\n\nMORPHE BRUSHES: https://www.morphebrushes.com\nBABSBEAUTY for 10% off\n\nGERARD COSMETICS: https://www.gerardcosmetics.com\nBABSBEAUTY for 30% off\n\nBombay Hair: https://www.bombayhair.com\nSTEPH30 for 30% off hot tools\n\nOFRA COSMETICS: https://www.ofracosmetics.com\nBABSBEAUTY for 30% off\n\nJUVIAS PLACE: https://www.juviasplace.com\nBABSBEAUTY for 10% off\n\nLILLY LASHES: https://www.lillylashes.com\nBABSBEAUTY to save 10%\n________________________________________\u00ad\u00ad\u00ad\u00ad\u00ad\u00ad\u00ad\u00ad\u00ad\u00ad\u00ad________________\n\nPRODUCTS MENTIONED:\n\nNative Deodorant - https://tinyurl.com/y8p4wz75\nSPRING20 to save 20%\n\nMaybelline Tattoo Studio Brow Gel - https://tinyurl.com/y97w38mz\n\nLilly Faux Mink Lashes 'Mykonos' 'Miami' & 'Roya' - https://tinyurl.com/y7f5l3qm\nBABSBEAUTY to save 10%\n\nKKW Loose Powder #2\n\nLemonhead LA Glitter Pastes - https://tinyurl.com/y9lfgpb2\n\nEsqido Lash Glue - https://tinyurl.com/goepq55\n\nMorphe Blush Trio 'Pop of Peach', 'Pop of Pink', & 'Pop of Blush' - https://tinyurl.com/ybb5gtha\nBABSBEAUTY to save 10%\n\nPurlisse Coconut Oil & Coffee Sugar Body Scrub - https://tinyurl.com/y8jmcuy7\n\nSmashbox Primer Water 'So Chill Coconut' - https://tinyurl.com/yaapjjmq\n\n\nDisclaimer: This video is Sponsored by Native Deodorant. Some links may be affiliate links which means I make a small commission from the clicks of those links. As always, I appreciate your support & love you guys!",
#             "thumbnails": {
#                 "default": {
#                     "url": "https://i.ytimg.com/vi/muWy99QbeWM/default.jpg",
#                     "width": 120,
#                     "height": 90
#                 },
#                 "medium": {
#                     "url": "https://i.ytimg.com/vi/muWy99QbeWM/mqdefault.jpg",
#                     "width": 320,
#                     "height": 180
#                 },
#                 "high": {
#                     "url": "https://i.ytimg.com/vi/muWy99QbeWM/hqdefault.jpg",
#                     "width": 480,
#                     "height": 360
#                 },
#                 "standard": {
#                     "url": "https://i.ytimg.com/vi/muWy99QbeWM/sddefault.jpg",
#                     "width": 640,
#                     "height": 480
#                 }
#             },
#             "channelTitle": "BabsBeauty",
#             "type": "upload"
#         },
#         "contentDetails": {
#             "upload": {
#                 "videoId": "muWy99QbeWM"
#             }
#         }
#     }


