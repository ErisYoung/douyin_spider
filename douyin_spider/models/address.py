from douyin_spider.models.JsonMixIn import ToJsonMixIn


class Address(ToJsonMixIn):
    def __init__(self, **kwargs):
        dict_mapping_variable = locals()['kwargs']
        for key in dict_mapping_variable.keys():
            setattr(self, key, key)

    def __repr__(self):
        return "<Address<%s,%s>>" % (self.id, self.simple_addr)


if __name__ == '__main__':
    address = Address(id="2", simple_addr="in my house")
    print(address)
    print(address.json())
