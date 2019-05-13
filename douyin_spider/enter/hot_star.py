from douyin_spider.utils.parse import parse_to_star
from douyin_spider.utils.get import get
from douyin_spider.models.collection_model import HotStar
from douyin_spider.utils.common import parse_datetime
from douyin_spider.config import headers, hot_star_url


def hot_stars():
    """
    get 20 of the most popular starts in billboard
    :return:HotStar
    """
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
