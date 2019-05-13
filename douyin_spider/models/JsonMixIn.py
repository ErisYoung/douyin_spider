import datetime
from copy import deepcopy


class ToJsonMixIn(object):
    """
    serialize to json MixIn
    """

    def json(self):
        """
        serialize item to json
        :return: json
        """
        dict_attrs = deepcopy(self.__dict__)
        from douyin_spider.models.video import Video
        from douyin_spider.models.music import Music
        from douyin_spider.models.address import Address
        from douyin_spider.models.user import User
        from douyin_spider.models.challenge import Challenge
        for k, v in dict_attrs.items():
            if not v:
                dict_attrs[k] = "None"
            if isinstance(v, (Video, Music, Address, User, Challenge)):
                dict_attrs[k] = v.json()
            elif isinstance(v, datetime.datetime):
                dict_attrs[k] = str(v)
            elif isinstance(v, str):
                dict_attrs[k] = v
            else:
                dict_attrs[k] = v

        return dict_attrs


if __name__ == '__main__':
    from douyin_spider.models.video import Video
    from douyin_spider.models.music import Music

    video = Video(id='11', play_url='cc.com')
    music = Music(id='22', play_url='dd.com')
    video.music = music
    print(video.json())
