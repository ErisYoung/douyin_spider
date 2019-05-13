from douyin_spider.handler.media import MediaHandler
from douyin_spider.models.video import Video


class VideoHandler(MediaHandler):
    """
    video handler,handle video item
    """
    async def handle(self, item, **kwargs):
        """
        handle item use VideoHandler
        :param item:
        :param kwargs:
        :return:
        """
        if isinstance(item, Video):
            return await self.process(item, **kwargs)
