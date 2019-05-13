from douyin_spider.utils.get import get
from douyin_spider.utils.common import parse_datetime
from douyin_spider.utils.parse import parse_to_video
from douyin_spider.models.collection_model import HotPETopVideo
from douyin_spider.config import headers, hot_positive_energy_url


def hot_pe_top20():
    """
    get 20 of the most popular positive energy videos in billboard
    :return:HotPETopVideo
    """
    result = get(hot_positive_energy_url, headers=headers)
    active_time = parse_datetime(result.get('active_time'))
    video_lists = result.get('aweme_list', [])
    videos = []
    for item in video_lists:
        video = parse_to_video(item.get('aweme_info'))
        video.hot_value_count = item.get('hot_value')
        videos.append(video)

    return HotPETopVideo(data=videos, datetime=active_time)


if __name__ == '__main__':
    result = hot_pe_top20()
    print(result)
