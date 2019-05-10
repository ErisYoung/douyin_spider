from douyin_spider.models.JsonMixIn import ToJsonMixIn
from douyin_spider.utils.get import get
from douyin_spider.utils.decryption.signture import generate_signature

share_music_base_url = "https://www.iesdouyin.com/web/api/v2/music/list/aweme/"

HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}


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

    def videos(self, max=None):
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
