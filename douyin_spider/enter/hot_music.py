from douyin_spider.utils.get import get
from douyin_spider.utils.common import parse_datetime
from douyin_spider.utils.parse import parse_to_music
from douyin_spider.models.collection_model import HotTopMusic

headers = {'User-Agent': 'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}
hot_music_url = "https://aweme.snssdk.com/aweme/v1/hotsearch/music/billboard/?version_code=5.5.0&pass-region=1&pass-route=1&js_sdk_version=1.12.0.2&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=de1ae3452f4c0d33795e12fe4d4224fcf4f52160&os_api=18&ac=WIFI&os_version=11.3.1&device_platform=iphone&build_number=55011&device_type=iPhone7,2&iid=67030863950&idfa=A5198308-FD4E-40A4-9630-9900B20E38D7&type=0&mas=013ca1905d580de8826c40058f7ff140e876bcfd0fada8a0d228d8&as=a275c45cd77bdce5dd1867&ts=1556956599"


def hot_music():
    result = get(url=hot_music_url, headers=headers)
    date_time = parse_datetime(result.get('active_time'))
    music_list = result.get('music_list', [])
    musics = []
    for item in music_list:
        music = parse_to_music(item.get('music_info'))
        music.hot_value = item.get('hot_value')
        musics.append(music)

    return HotTopMusic(data=musics, datetime=date_time)


if __name__ == '__main__':
    result = hot_music()
    print(result)
