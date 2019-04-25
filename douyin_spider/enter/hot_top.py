from douyin_spider.utils.get import get
from douyin_spider.utils.common import parse_datetime
from douyin_spider.models.collection_model import HotTopVideo
from douyin_spider.utils.parse import parse_to_video

headers={'User-Agent':'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}
hot_top_url="https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/?version_code=5.5.0&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&os_version=11.3.1&device_platform=iphone&device_type=iPhone7,2"

def hot_top20():
    result=get(hot_top_url,headers=headers)
    active_time=parse_datetime(result.get('active_time'))
    video_lists=result.get('aweme_list',[])
    videos=[]
    for item in video_lists:
        video =parse_to_video(item.get('aweme_info'))
        video.hot_value_count=item.get('hot_value')
        videos.append(video)

    return HotTopVideo(data=videos,datetime=active_time)

if __name__ == '__main__':
    result=hot_top20()
    print(result)

