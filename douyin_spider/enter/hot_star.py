from douyin_spider.utils.parse import parse_to_star
from douyin_spider.utils.get import get
from douyin_spider.models.collection_model import HotStar
from douyin_spider.utils.common import parse_datetime

headers = {'User-Agent': 'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}
hot_star_url = "https://api.amemv.com/aweme/v1/hotsearch/star/billboard/?version_code=5.5.0&pass-region=1&pass-route=1&js_sdk_version=1.12.0.2&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=de1ae3452f4c0d33795e12fe4d4224fcf4f52160&os_api=18&ac=WIFI&os_version=11.3.1&device_platform=iphone&build_number=55011&device_type=iPhone7,2&iid=67030863950&idfa=A5198308-FD4E-40A4-9630-9900B20E38D7&type=0&mas=0154d1c244712b7a4cb317bdb0482cc5c3c640c3df778b22d554e1&as=a2b5dd7dd9d43c74639759&ts=1557386313"


def hot_stars():
    result = get(url=hot_star_url, headers=headers)
    date_time = parse_datetime(result.get('active_time'))
    star_list = result.get('user_list', [])
    stars = []
    for item in star_list:
        star = parse_to_star(item)
        stars.append(star)

    return HotStar(data=stars, datetime=date_time)


if __name__ == '__main__':
    result = hot_stars()
    print(result)
