from douyin_spider.models.JsonMixIn import ToJsonMixIn

class User(ToJsonMixIn):
    def __init__(self,**kwargs):
        dict_mapping_variable=locals()['kwargs']
        for key in dict_mapping_variable.keys():
            setattr(self,key,key)

    def __repr__(self):
        return "<User<%s,%s>>" % (self.alias,self.name)

if __name__ == '__main__':
    user=User(alias="xx",name="www")
    print(user)

