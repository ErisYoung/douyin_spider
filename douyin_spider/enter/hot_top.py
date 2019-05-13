from douyin_spider.utils.get import get
from douyin_spider.utils.common import parse_datetime
from douyin_spider.models.collection_model import HotTopVideo
from douyin_spider.utils.parse import parse_to_video
from douyin_spider.config import headers, hot_top_url


def hot_top20():
    """
    get 20 of the most popular videos in billboard
    :return:HotTopVideo
    """
    result = get(hot_top_url, headers=headers)
    active_time = parse_datetime(result.get('active_time'))
    video_lists = result.get('aweme_list', [])
    videos = []
    for item in video_lists:
        video = parse_to_video(item.get('aweme_info'))
        video.hot_value_count = item.get('hot_value')
        videos.append(video)

    return HotTopVideo(data=videos, datetime=active_time)


if __name__ == '__main__':
    result = hot_top20()
    print(result)
