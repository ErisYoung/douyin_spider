import douyin
from douyin.structures import Topic, Music

# define file handler and specify folder
video_file_handler = douyin.handlers.VideoFileHandler(folder='./videos')
music_file_handler = douyin.handlers.MusicFileHandler(folder='./musics')
# define mongodb handler
mongo_handler = douyin.handlers.MongoHandler()
# define downloader
downloader = douyin.downloaders.VideoDownloader([mongo_handler, video_file_handler, music_file_handler])

for result in douyin.hot.trend():
    for item in result.data:
        # download videos of topic/music for 100 max per
        downloader.download(item.videos(max=10))