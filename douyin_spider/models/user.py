from douyin_spider.models.JsonMixIn import ToJsonMixIn
from douyin_spider.utils.decryption.signture import generate_signature
from douyin_spider.utils.common import get_user_dytk_by_id
from douyin_spider.utils.get import get

share_user_base_url = "https://www.iesdouyin.com/web/api/v2/aweme/post/"
HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}


class BasicUser(object):
    def __init__(self, **kwargs):
        self.id = None

    def videos(self, max=None):
        if not isinstance(max, int):
            raise RuntimeError("`max` param must be int")
        if max <= 0:
            raise RuntimeError("`max` param must >=1")
        from douyin_spider.utils.parse import parse_to_video

        user_video_params = {
            'user_id': str(self.id),
            'count': '21',
            'max_cursor': '0',
            'aid': '1128',
            '_signature': generate_signature(str(self.id)),
            'dytk': get_user_dytk_by_id(str(self.id)),
        }
        count, cursor = 0, None
        while True:
            if cursor:
                user_video_params['max_cursor'] = str(cursor)
            result = get(share_user_base_url, params=user_video_params, headers=HEADERS)
            aweme_list = result.get('aweme_list', [])
            for item in aweme_list:
                count += 1
                video = parse_to_video(item)
                yield video
                if max and count >= max:
                    return

            if result.get('has_more'):
                cursor = result.get('max_cursor')
            else:
                break
        if count == 0:
            print(f"There is no video in the user {self.id}")
        print(f"video count:{count}")


class User(BasicUser, ToJsonMixIn):
    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs.get('id')
        self.avatar_url = kwargs.get('avatar_url')
        self.is_verified = kwargs.get('is_verified')
        self.verify_info = kwargs.get('verify_info')
        self.is_hide_search = kwargs.get('is_hide_search')
        self.nickname = kwargs.get('nickname')
        self.region = kwargs.get('region')
        self.signature = kwargs.get('signature')
        self.gender = kwargs.get('gender')
        self.alias = kwargs.get('alias')

    def __repr__(self):
        return "<User<%s,%s>>" % (self.alias, self.nickname)


class Star(BasicUser, ToJsonMixIn):
    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs.get('id')
        self.nickname = kwargs.get('nickname')
        self.signature = kwargs.get('signature')
        self.avatar_url = kwargs.get('avatar_url')
        self.factor_hot_value = kwargs.get('factor_hot_value')
        self.hot_value = kwargs.get('hot_value')

    def __repr__(self):
        return "<Star<%s,%s>>" % (self.nickname, self.id)


if __name__ == '__main__':
    user = User(alias="xx", nickname="www")
    print(user)

    star = Star(id='1231', nickname='jerry')
    star.videos()
