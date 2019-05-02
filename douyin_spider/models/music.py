from douyin_spider.models.JsonMixIn import ToJsonMixIn


class Music(ToJsonMixIn):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.play_url = kwargs.get('play_url')
        self.owner_name = kwargs.get('owner_name')
        self.album = kwargs.get('album')
        self.owner_id = kwargs.get('owner_id')
        self.duration = kwargs.get('duration')
        self.cover_url = kwargs.get('cover_url')

    def __repr__(self):
        return "<Music<%s,%s>>" % (self.id, self.title[:50].strip() if self.title else None)
