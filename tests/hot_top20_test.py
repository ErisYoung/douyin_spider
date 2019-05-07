from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.handler.video import VideoHandler
from douyin_spider.handler.music import MusicHandler
from douyin_spider.handler.mongodb import MongoHandler
from douyin_spider.enter.hot_top import hot_top20

video_handler = VideoHandler(folder='./videos')
music_handler = MusicHandler(folder='./musics')
mongo_handler = MongoHandler()
downloader = VideoDownloader([video_handler])

result = hot_top20()

for item in result.data[0:2]:
    downloader.download(item)

print("success")
