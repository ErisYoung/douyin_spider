from douyin_spider.models.JsonMixIn import ToJsonMixIn


class User(ToJsonMixIn):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.avatar_url = kwargs.get('avatar_url')
        self.is_verified = kwargs.get('is_verified')
        self.verify_info = kwargs.get('verify_info')
        self.is_hide_search = kwargs.get('is_hide_search')
        self.nikename = kwargs.get('nikename')
        self.region = kwargs.get('region')
        self.signature = kwargs.get('signature')
        self.gender = kwargs.get('gender')
        self.alias = kwargs.get('alias')

    def __repr__(self):
        return "<User<%s,%s>>" % (self.alias, self.nikename)


if __name__ == '__main__':
    user = User(alias="xx", nikename="www")
    print(user)
