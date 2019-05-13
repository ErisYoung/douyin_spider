from douyin_spider.utils.get import get
from douyin_spider.utils.common import parse_datetime
from douyin_spider.utils.parse import parse_to_music
from douyin_spider.models.collection_model import HotTopMusic
from douyin_spider.config import headers, hot_music_url


def hot_music():
    """
    get 20 of the most popular musics in billboard
    :return:HotTopMusic
    """
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
