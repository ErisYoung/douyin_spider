import aiohttp
from pathlib import Path
from douyin_spider.handler.handler import Handler
from douyin_spider.utils.extension import type_to_extension

GET_DICT_PARAMS = {'ssl': False, 'timeout': 10}


class MediaHandler(Handler):

    def __init__(self, folder):
        super().__init__()
        self.folder = folder
        self.create_folder(self.folder)

    @staticmethod
    def create_folder(folder_path):
        if not Path(folder_path).exists():
            Path(folder_path).mkdir()

    async def process(self, item, **kwargs):
        print("Downloading", item, '...')
        kwargs.update(GET_DICT_PARAMS)
        async with aiohttp.ClientSession() as session:
            async with session.get(item.play_url,**kwargs) as res:
                if res.status == 200:
                    extension = type_to_extension(res.headers.get('Content-Type'))
                    media_save_path = Path(self.folder).joinpath(f"{item.id}.{extension}")
                    with open(media_save_path, 'wb') as f:
                        f.write(await res.content.read())
                        print('success!',"Download media to", media_save_path)
                else:
                    print(f"Cannot download {item.id},response status {res.status} ")

    async def handle(self, item, **kwargs):

        return await self.process(item, **kwargs)


if __name__ == '__main__':
    from os.path import join

    path = './videos'
    str1 = Path(path).joinpath("111.jpg")
    str2 = join(path, '112.jpg')
    str3 = Path(path) / "111.jpg"
    print(str1)
    print(str2)
    print(str3)
