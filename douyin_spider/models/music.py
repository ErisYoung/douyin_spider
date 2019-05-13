from douyin_spider.models.JsonMixIn import ToJsonMixIn
from douyin_spider.utils.get import get
from douyin_spider.utils.decryption.signture import generate_signature
from douyin_spider.config import share_music_base_url, HEADERS


class Music(ToJsonMixIn):
    """
    Music model

    Main public attributes:
    - id: address id,unique
    - play_url: music url
    - cover_url: cover url
    - ...
    """

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

    def videos(self, max=None):
        """
        videos belongs to challenge
        :param max:videos number need
        :return:videos generator
        """
        if not isinstance(max, int):
            raise RuntimeError("`max` param must be int")
        if max <= 0:
            raise RuntimeError("`max` param must >=1")
        from douyin_spider.utils.parse import parse_to_video

        music_video_params = {
            'music_id': str(self.id),
            'count': '9',
            'cursor': '0',
            'aid': '1128',
            'screen_limit': '3',
            'download_click_limit': '0',
            '_signature': generate_signature(str(self.id)),
        }
        count, cursor = 0, None
        while True:
            if cursor:
                music_video_params['cursor'] = str(cursor)
                # music_video_params['_signature'] = generate_signature(
                #     str(self.id) + '9' + str(cursor))

            result = get(share_music_base_url, params=music_video_params, headers=HEADERS)
            aweme_list = result.get('aweme_list', [])
            for item in aweme_list:
                count += 1
                video = parse_to_video(item)
                yield video
                if max and count >= max:
                    return

            if result.get('has_more'):
                cursor = result.get('cursor')
            else:
                break

        if count == 0:
            print(f"There is no video in this music {self.id}")
        print(f"video count:{count}")
