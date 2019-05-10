from douyin_spider.enter.hot_music import hot_music
from douyin_spider.handler.video import VideoHandler
from douyin_spider.handler.music import MusicHandler
from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.enter.hot_top import hot_top20

video_handler = VideoHandler(folder='./videos')
music_handler = MusicHandler(folder='./musics')
downloader = VideoDownloader([video_handler])

results = hot_music()

for music in results.data:
    downloader.download(music.videos(max=10))
    break
