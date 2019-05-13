from douyin_spider.models.collection_model import HotSearch
from douyin_spider.utils.get import get
from douyin_spider.utils.common import parse_datetime
from douyin_spider.config import headers, hot_search_url


def hot_search():
    """
    get 20 of the most popular searching videos in billboard
    :return:HotSearch
    """
    result = get(hot_search_url, headers=headers)
    data = result.get('data', {})
    date_time = parse_datetime(data.get('active_time'))
    word_list = data.get('word_list', [])
    data_lists = [{'hot_value': item.get('hot_value'), 'word': item.get('word')} for item in word_list]
    return HotSearch(data=data_lists, datetime=date_time)


if __name__ == '__main__':
    result = hot_search()
    print(result)
