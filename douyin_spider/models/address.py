from douyin_spider.models.JsonMixIn import ToJsonMixIn


class Address(ToJsonMixIn):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.longitude = kwargs.get('longitude')
        self.latitude = kwargs.get('latitude')
        self.name = kwargs.get('name')
        self.province = kwargs.get('province')
        self.city = kwargs.get('city')
        self.simple_addr = kwargs.get('simple_addr')
        self.district = kwargs.get('district')
        self.city_code = kwargs.get('city_code')
        self.sub_address = kwargs.get('sub_address')

    def __repr__(self):
        return "<Address<%s,%s>>" % (self.id, self.simple_addr)


if __name__ == '__main__':
    address = Address(id="2", simple_addr="in my house")
    print(address)
    print(address.json())
