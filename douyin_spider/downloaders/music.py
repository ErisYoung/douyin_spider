from douyin_spider.models.music import Music
from douyin_spider.downloaders.parent import Downloader
from douyin_spider.handler.handler import Handler


class MusicDownloader(Downloader):

    async def handle_one_item(self, item):
        if isinstance(item, Music):
            print("Processing music", item)
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    await handler.handle(item)
