import datetime
from copy import deepcopy

class ToJsonMixIn(object):
    def json(self):
        dict_attrs=deepcopy(self.__dict__)
        from douyin_spider.models.video import Video
        for k,v in dict_attrs.items():
            if not v:
                dict_attrs[k]="None"
            if isinstance(v,(Video,)):
                dict_attrs[k]=v.json()
            if isinstance(v,datetime.datetime):
                dict_attrs[k]=str(v)
            if isinstance(v,str):
                dict_attrs[k]=v

        return dict_attrs

class Test(ToJsonMixIn):
    def __init__(self,a,b):
        from douyin_spider.models.video import Video
        self.a=10
        self.b=20
        self.data=datetime.datetime.now()
        self.video=Video()

if __name__ == '__main__':
    import datetime
    test=Test(exec("a=2"),exec("b=20"))
    result=test.json()
    print(result)