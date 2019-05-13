from motor.motor_asyncio import AsyncIOMotorClient
from douyin_spider.handler.handler import Handler
from douyin_spider.models.video import Video
from douyin_spider.models.music import Music


class MongoHandler(Handler):
    """
    mongodb handler,save data to local mongodb with asyncIO mongodb
    """

    def __init__(self, con_uri=None, db_name="douyin"):
        """
        init function,you can also enter one mongodb connect_uri
        :param con_uri:
        :param db_name: default name "douyin"
        """
        super().__init__()
        self.con_uri = con_uri or 'localhost'
        self.client = AsyncIOMotorClient(self.con_uri)
        self.db = self.client[db_name]

    async def handle(self, item, **kwargs):
        """
        save item  to mongodb,insert if item not exists,otherwise update
        :param item:
        :param kwargs:
        :return:
        """
        collection_name = "default"
        if isinstance(item, Video):
            collection_name = "videos"
        elif isinstance(item, Music):
            collection_name = "musics"

        collection = self.db[collection_name]
        print("Saving", item, 'to mongodb...')
        if await collection.update_one({'id': item.id}, {'$set': item.json()}, upsert=True):
            print("Save success", item, 'to mongodb...')
        else:
            print("error save", item, 'to mongodb...')
