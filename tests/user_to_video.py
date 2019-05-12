""" In this module ,you can download videos from stars

You can choose how many you want,and what media you want download and store.

"""

from douyin_spider.enter.hot_star import hot_stars
from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.handler.video import VideoHandler
from douyin_spider.handler.mongodb import MongoHandler

video_handler = VideoHandler(folder='./videos')
mongo_handler = MongoHandler()
downloader = VideoDownloader([video_handler])

results = hot_stars()

for user in results.data:
    downloader.download(user.videos(max=5))
    break
