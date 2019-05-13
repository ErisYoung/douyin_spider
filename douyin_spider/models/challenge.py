from douyin_spider.models.JsonMixIn import ToJsonMixIn
from douyin_spider.utils.decryption.signture import generate_signature
from douyin_spider.utils.get import get
from douyin_spider.utils.parse import parse_to_video

share_challenge_base_url = "https://www.iesdouyin.com/aweme/v1/challenge/aweme/"
HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}


class Challenge(ToJsonMixIn):
    """
    Challenge model

    Main public attributes:
    - id: address id,unique
    - name: challenge name
    - ...
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get("name")

    def __repr__(self):
        return "<Challenge<%s,%s>>" % (self.id, self.name)

    def videos(self, max=None):
        """
        videos belongs to challenge
        :param max:videos number need
        :return:videos generator
        """
        print(f"<{type(self).__name__}<{self.name},{self.id}>>")
        if not isinstance(max, int):
            raise RuntimeError("`max` param must be int")
        if max <= 0:
            raise RuntimeError("`max` param must >=1")
        from douyin_spider.utils.parse import parse_to_video

        challenge_video_params = {
            "ch_id": str(self.id),
            "count": "9",
            "cursor": "0",
            "aid": "1128",
            "screen_limit": "3",
            "download_click_limit": "0",
            "_signature": generate_signature(str(self.id) + '9' + '0'),
        }
        count, cursor = 0, None
        while True:
            if cursor:
                challenge_video_params['cursor'] = str(cursor)
            result = get(share_challenge_base_url, params=challenge_video_params, headers=HEADERS)

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
            print(f"There is no video in the challenge {self.id}")
        print(f"video count:{count}")
