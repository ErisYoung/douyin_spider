"""In the module,you can download videos with your own entering share url

You can enter user share_url,music share_url,challenge share_url to download
specified videos.

You can use like: 'python assign_share_url --help'  to know command line arguments

"""
import re
import argparse
import pathlib
import sys

root_path = pathlib.Path().cwd().parent
sys.path.append(str(root_path))

from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.handler.video import VideoHandler
from douyin_spider.models.user import User
from douyin_spider.models.music import Music
from douyin_spider.models.challenge import Challenge
from douyin_spider.utils.common import get_real_address_from_short

INIT_VIDEO_COUNT = 10
HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}
SHORT_BASE_URL = "v.douyin.com"


def init_args_parse():
    """
    init arg_parser
    :return: args
    """
    parser = argparse.ArgumentParser(usage="assign douYin share-url download", description="assign share-url")
    parser.add_argument("-u", "--url", help="share url",type=str)
    parser.add_argument("-c", "--count", help="video count you download", default=INIT_VIDEO_COUNT, type=int)
    args = parser.parse_args()
    return args


def init_downloader():
    """
    init downloader,default add video_handler
    :return: downloader
    """
    video_handler = VideoHandler(folder="./videos")
    downloader = VideoDownloader([video_handler])
    return downloader


def parse_url_for_type(share_url):
    """
    parse share_url to type what it's
    :param share_url: str
    :return: type:str
    """
    music_pattern = r".*/share/music/"
    user_pattern = r".*/share/user/"
    challenge_pattern = r".*/share/challenge/"
    if re.match(music_pattern, share_url):
        print("Parse share-url to music share url...")
        return "music"
    elif re.match(user_pattern, share_url):
        print("Parse share-url to user share url...")
        return "user"
    elif re.match(challenge_pattern, share_url):
        print("Parse share-url to challenge share url...")
        return "challenge"


def parse_for_id(url_str):
    """
    parse id from url_str
    :param url_str: url
    :return: id:str
    """
    if isinstance(url_str, str):
        id = re.search(r"/(\d+)\?", url_str).group(1)
        return id
    else:
        return None


def download_videos_from_challenge(share_url, count):
    """
    download videos in challenge
    :param share_url:
    :param count: videos number
    :return:
    """
    challenge_id = parse_for_id(share_url)
    challenge = Challenge(id=challenge_id, name="default")
    downloader = init_downloader()
    print(f"Downloading videos from challenge, count:{count}...")
    downloader.download(challenge.videos(max=count))


def download_videos_from_music(share_url, count):
    """
    download videos in music
    :param share_url:
    :param count: videos number
    :return:
    """
    music_id = parse_for_id(share_url)
    user = Music(id=music_id)
    downloader = init_downloader()
    print(f"Downloading videos from music, count:{count}...")
    downloader.download(user.videos(max=count))


def download_videos_from_user(share_url, count):
    """
    download videos in user
    :param share_url:
    :param count: videos number
    :return:
    """
    user_id = parse_for_id(share_url)
    user = User(id=user_id, nickname="default")
    downloader = init_downloader()
    print(f"Downloading videos from user, count:{count}...")
    downloader.download(user.videos(max=count))


def parse_for_url(share_url):
    """
    parse normal url or short url to real url
    :param share_url:
    :return:real share_url
    """
    if share_url.find(SHORT_BASE_URL) != -1:
        return get_real_address_from_short(share_url)
    return share_url


def run():
    """
    run
    :return:
    """
    pattern_func_mapping = {'user': download_videos_from_user, 'music': download_videos_from_music,
                            'challenge': download_videos_from_challenge}
    args = init_args_parse()
    share_url, count = args.url, args.count
    real_url = parse_for_url(share_url)
    print(real_url)
    pattern = parse_url_for_type(real_url)
    process_func = pattern_func_mapping[pattern]
    process_func(real_url, count)


if __name__ == '__main__':
    run()