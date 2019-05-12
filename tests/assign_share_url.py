import re
import argparse
from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.handler.video import VideoHandler
from douyin_spider.models.user import User
from douyin_spider.models.music import Music

INIT_VIDEO_COUNT = 10


def init_args_parse():
    parser = argparse.ArgumentParser(usage="assign douYin share-url download", description="assign share-url")
    parser.add_argument("-u", "--url", help="share url")
    parser.add_argument("-c", "--count", help="video count you download")
    args = parser.parse_args()
    return args


def init_downloader():
    video_handler = VideoHandler(folder="./videos")
    downloader = VideoDownloader([video_handler])
    return downloader


def parse_url_for_type(share_url):
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
    if isinstance(url_str, str):
        id = re.search(r"/(\d+)\?", url_str).group(1)
        return id
    else:
        return None


def download_videos_from_challenge(share_url, count=INIT_VIDEO_COUNT):
    pass


def download_videos_from_music(share_url, count=INIT_VIDEO_COUNT):
    music_id = parse_for_id(share_url)
    user = Music(id=music_id)
    downloader = init_downloader()
    print(f"Downloading videos from music, count:{count}...")
    downloader.download(user.videos(max=count))


def download_videos_from_user(share_url, count=INIT_VIDEO_COUNT):
    user_id = parse_for_id(share_url)
    user = User(id=user_id, nickname="default")
    downloader = init_downloader()
    print(f"Downloading videos from user, count:{count}...")
    downloader.download(user.videos(max=count))


def run():
    pattern_func_mapping = {'user': download_videos_from_user, 'music': download_videos_from_music,
                            'challenge': download_videos_from_challenge}
    args = init_args_parse()
    share_url, count = args.url, args.count
    pattern = parse_url_for_type(share_url)
    process_func = pattern_func_mapping[pattern]
    process_func(share_url,count)


if __name__ == '__main__':
    url_lists = [
        "https://www.douyin.com/share/user/85860189461?share_type=link&tt_from=weixin&utm_source=weixin&utm_medium=aweme_ios&utm_campaign=client_share&uid=97193379950&did=30337873848",
        "https://www.iesdouyin.com/share/challenge/1593608573838339?utm_campaign=clien",
        "https://www.iesdouyin.com/share/music/6536362398318922509?utm_campaign=client_share&app=aweme&utm_medium=ios&iid=30337873848&utm_source=copy"]
    for url in url_lists:
        print(parse_for_id(url))

    args = init_args_parse()
    print(args.url,args.count)
