from douyin_spider.models.video import Video
from douyin_spider.downloaders.parent import Downloader
from douyin_spider.handler.handler import Handler

class VideoDownloader(Downloader):

    async def handle_one_item(self, item):
        if isinstance(item,Video):
            print("Processing video",item)
            for handler in self.handlers:
                if isinstance(handler,Handler):
                    handler.handle(item)
