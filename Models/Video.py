class Video:
    def __init__(self, creatorId: object, videoId: object, publishedAt: object, title: object, videoTags: object, viewCount: object, likeCount: object, dislikeCount: object,
                 favoriteCount: object, commentCount: object,categoryId:object ) -> object:
        self.videoId = videoId
        self.creatorId = creatorId
        self.publishedAt = publishedAt
        self.title = title
        self.videoTags = videoTags
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.favoriteCount = favoriteCount
        self.commentCount = commentCount
        self.categoryId = categoryId

    def __repr__(self):
        return "Video('creatorId {}',' " \
               "videoId {}',' " \
               "publishedAt {}'," \
               "'title ""{}'," \
               "'videoTags {}', " \
               "'viewCount {}', " \
               "'likeCount {}', " \
               "'dislikeCount {}'," \
               "'favoriteCount {}'," \
               "'commentCount {}'" \
               "'categoryId {}',)" \
            .format(self.creatorId, self.videoId, self.publishedAt, self.title, self.videoTags, self.viewCount,
                    self.likeCount, self.dislikeCount, self.favoriteCount, self.commentCount, self.categoryId)



