from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.handler.video import VideoHandler
from douyin_spider.handler.music import MusicHandler
from douyin_spider.handler.mongodb import MongoHandler
from douyin_spider.enter.hot_positive_energy import hot_pe_top20
video_handler = VideoHandler(folder='./videos')
music_handler = MusicHandler(folder='./musics')
mongo_handler = MongoHandler()
downloader = VideoDownloader([video_handler])

result = hot_pe_top20()

downloader.download(result.data)

print("success")
