import aiohttp
import requests as rq
from pathlib import Path
from douyin_spider.handler.handler import Handler
from douyin_spider.utils.extension import type_to_extension
from douyin_spider.utils.common import get_real_url

GET_DICT_PARAMS = { 'timeout': 50}
REDIRECT_URL_HEAD= "https://aweme.snssdk.com/aweme"
headers = {'User-Agent': 'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}


class MediaHandler(Handler):

    def __init__(self, folder):
        super().__init__()
        self.folder = folder
        self.create_folder(self.folder)

    @staticmethod
    def create_folder(folder_path):
        if not Path(folder_path).exists():
            Path(folder_path).mkdir()

    @staticmethod
    def is_redirect_url(url):
        if isinstance(url, str) and url.startswith(REDIRECT_URL_HEAD):
            return True
        return False

    async def process(self, item, **kwargs):
        print("Downloading", item, '...')
        kwargs.update(GET_DICT_PARAMS)
        if self.is_redirect_url(item.play_url):
            item.play_url=get_real_url(item.play_url)
        async with aiohttp.ClientSession() as session:
            async with session.get(item.play_url, **kwargs) as res:
                if res.status == 200:
                    extension = type_to_extension(res.headers.get('Content-Type'))
                    media_save_path = Path(self.folder).joinpath(f"{item.id}.{extension}")
                    with open(media_save_path, 'wb') as f:
                        f.write(await res.content.read())
                    print('success!', "Download media to", media_save_path)
                else:
                    print(f"Cannot download {item.id},response status {res.status} ")

    async def handle(self, item, **kwargs):

        return await self.process(item, **kwargs)


if __name__ == '__main__':
    url="https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f2c0000bj638na6tgqciffa6ajg&ratio=720p&line=0"
    get_real_url(url)

