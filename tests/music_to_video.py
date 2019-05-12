""" In this module ,you can download videos from music

You can choose how many you want,and what media you want download and store.

"""

from douyin_spider.enter.hot_music import hot_music
from douyin_spider.handler.video import VideoHandler
from douyin_spider.handler.music import MusicHandler
from douyin_spider.downloaders.video import VideoDownloader

video_handler = VideoHandler(folder='./videos')
music_handler = MusicHandler(folder='./musics')
downloader = VideoDownloader([video_handler])

results = hot_music()

for music in results.data:
    downloader.download(music.videos(max=10))
    break
