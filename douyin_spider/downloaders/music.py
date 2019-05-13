from douyin_spider.models.music import Music
from douyin_spider.downloaders.parent import Downloader
from douyin_spider.handler.handler import Handler


class MusicDownloader(Downloader):
    """
    Music downloader for items
    """

    async def handle_one_item(self, item):
        """
        handle one item by traversing all handlers
        :param item:item
        :return:
        """
        if isinstance(item, Music):
            print("Processing music", item)
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    await handler.handle(item)
