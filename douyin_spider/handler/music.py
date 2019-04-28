from douyin_spider.handler.media import MediaHandler
from douyin_spider.models.music import Music

class MusicHandler(MediaHandler):
    async def handle(self, item, **kwargs):
        """
        handler item use MusicHandler
        :param item:
        :param kwargs:
        :return:
        """
        if isinstance(item,Music):
            return await self.process(item,**kwargs)