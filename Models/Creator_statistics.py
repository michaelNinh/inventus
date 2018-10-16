class Channel_statistics:
    """ after getting a series of videos, get averages of channel attributes """

    def __init__(self, creatorId ,viewsAverage, likesAverage, dislikeAverage,favoritesAverage,commentsAverage, engagementRate, sampleSize, dateRecorded, categoryId,date_last_video):
        self.creatorId = creatorId
        self.viewAverage = viewsAverage
        self.likesAverage = likesAverage
        self.dislikeAverage = dislikeAverage
        self.favoritesAverage = favoritesAverage
        self.commentsAverage = commentsAverage
        self.engagementRate = engagementRate
        self.sampleSize = sampleSize
        self.dateRecorded = dateRecorded
        self.categoryId = categoryId
        self.date_last_video = date_last_video



    def __repr__(self):
        return "Channel_statistics('creatorId {}',' " \
               "viewAverage {}',' " \
               "likesAverage {}'," \
               "'dislikeAverage ""{}'," \
               "'favoritesAverage {}', " \
               "'commentsAverage {}', " \
               "'engagementRateAverage {}', " \
               "'sampleSize {}'," \
               "'dateRecorded {}', " \
               "'date_last_video {}', " \
               "''categoryId {}'" \
            .format(self.creatorId, self.viewAverage, self.likesAverage,self.dislikeAverage,
                    self.favoritesAverage,self.commentsAverage, self.engagementRate,self.sampleSize,self.dateRecorded, self.date_last_video ,self.categoryId)