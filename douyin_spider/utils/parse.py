from douyin_spider.utils.common import parse_datetime,get_array_first
from douyin_spider.models.video import Video
from douyin_spider.models.music import Music

def get_video_url(video_list):
    if video_list and isinstance(video_list,list) and len(video_list)>1:
        return video_list[-1]
    return None

def get_music_url(music_list):
    if music_list and isinstance(music_list,list) and len(music_list)>1:
        return music_list[-1]
    return None

def download_video_test(url):
    import requests
    headers={'User-Agent':'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}
    res=requests.get(url,headers=headers)
    with open('test.mp4','wb+') as f:
        f.write(res.content)

def parse_to_video(data):
    statistics=data.get('statistics',{})
    id=statistics.get('aweme_id')
    like_count=statistics.get('digg_count')
    comment_count=statistics.get('comment_count')
    share_count=statistics.get('share_count')

    share_url=data.get('share_url')
    desc=data.get('desc')
    group_id=data.get('group_id')
    author_user_id=data.get('author_user_id')
    create_time=parse_datetime(data.get('create_time'))
    is_ads = data.get('is_ads')
    region = data.get('region')

    video=data.get('video',{})
    ratio=video.get('ratio')
    cover_url=get_array_first(video.get('origin_cover').get('url_list',[]))
    play_url=get_video_url(video.get('play_addr',{}).get('url_list',[]))
    duration=data.get('duration')

    music = parse_to_music(data.get('music', {}))
    author = parse_to_user(data.get('author', {}))
    address=parse_to_address(data.get('poi_info',{}))

    if id:
        return Video(
            id=id,
            like_count=like_count,
            comment_count=comment_count,
            share_count=share_count,
            share_url=share_url,
            desc=desc,
            group_id=group_id,
            author_user_id=author_user_id,
            create_time=create_time,
            is_ads=is_ads,
            region=region,
            ratio=ratio,
            cover_url=cover_url,
            play_url=play_url,
            duration=duration,
            music=music,
            author=author,
            address=address
        )
    else:
        return None

def parse_to_user(author_json):
    pass

def parse_to_music(music_json):
    id=music_json.get('mid')
    title=music_json.get('title')
    play_url=get_music_url(music_json.get('play_url',{}).get('url_list',[]))
    owner_name=music_json.get('owner_nickname')
    alunm = music_json.get('album')
    owner_id=music_json.get('owner_id')
    duration=music_json.get('duration')
    cover_url=get_array_first(music_json.get('cover_large',{}).get('url_list'))

    if id:
        return Music(
            id=id,
            title=title,
            play_url=play_url,
            owner_name=owner_name,
            alunm=alunm,
            owner_id=owner_id,
            duration=duration,
            cover_url=cover_url
        )
    else:
        return None

def parse_to_address(poi_info_json):
    pass


if __name__ == '__main__':
    url='https://api.amemv.com/aweme/v1/play/?video_id=v0200f940000bis3ort1mik7192tss6g&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0'
    download_video_test(url)