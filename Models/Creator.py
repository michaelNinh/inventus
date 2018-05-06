from Models.Video import Video


class Creator:
    """Class data model for youtube creator"""

    def __init__(self, channelTitle, creatorId, totalSubscribers, totalViews, availableVideoIds, email, totalComments, videoCount, discoveryKeyword, reachOut, country, notes):
        self.channelTitle = channelTitle
        self.creatorId = creatorId
        self.totalSubscribers = totalSubscribers
        self.totalViews = totalViews
        self.availableVideosIds = availableVideoIds
        self.email = email
        self.totalComments = totalComments
        self.videoCount = videoCount
        self.discoveryKeyword = discoveryKeyword
        self.reachOut = reachOut
        self.country = country
        self.notes = notes



    # do i actually need the video ID attribute?
    def __repr__(self):
        return "Creator('channel title {}'," \
               "'creatorID {}',' " \
               "total subs {}',' " \
               "total views {}'," \
               "'vid Ids ""{}'," \
               "'email {}', " \
               "'totalComments {}', " \
               "'videoCount {}', " \
               "'keyword {}'," \
               "'reachOut {}'" \
               "'country {}," \
               "'notes{})" \
            .format(self.channelTitle, self.creatorId, self.totalSubscribers, self.totalViews, self.availableVideosIds, self.email, self.totalComments, self.videoCount, self.discoveryKeyword,self.reachOut, self.country, self.notes)


