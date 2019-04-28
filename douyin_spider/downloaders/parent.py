import math
import types
import asyncio
import time
from tqdm import tqdm,trange

INIT_DOWNLOADER_BATCH_SIZE=10

class Downloader(object):
    def __init__(self,handlers=None,batch_size=INIT_DOWNLOADER_BATCH_SIZE):
        """
        init downloadr
        :param handlers: init handlers
        :param batch_size:  init batch_size ，default
        """
        self.handlers=handlers or []
        self.batch=batch_size

    def add_handler(self,handler):
        """
        add handler to downloader
        :param handler:
        :return:
        """
        self.handlers.append(handler)

    @property
    def handlers(self):
        """
        return handlers of downloader
        :return:
        """
        return self.handlers

    @handlers.setter
    def handlers(self,handlers):
        """
        set handlers of downloader
        :param handlers:
        :return:
        """
        self.handlers=handlers

    def update_bars(self,size=1):
        """
        update tqdm‘s bar
        :param size:
        :return:
        """
        self.bar.update(size)

    async def handle_one_item(self,item):
        """
        need overwrite
        :param item: single item
        :return:
        """
        raise NotImplementedError

    def handle_items(self,items):
        """
        handle items
        :param items:
        :return:
        """
        items_size=len(items)
        with tqdm(total=items_size) as self.bar:
            base_step=int(math.ceil(items_size/self.batch))
            for i in range(base_step):
                current_items=items[i*self.batch:(i+1)*self.batch]
                loop=asyncio.get_event_loop()
                tasks=[asyncio.ensure_future(self.handle_items(current_item)) for current_item in current_items]
                for task in tasks:
                    task.add_done_callback(self.update_bars)
                loop.run_until_complete(asyncio.wait(tasks))

    def download(self,input_items):
        """
        download input_items
        :param input_items:
        :return:
        """
        if isinstance(input_items,types.GeneratorType):
            temp=[]
            for item in input_items:
                print("handling ",item,'...')
                temp.append(item)
                if len(temp)==self.batch:
                    self.handle_items(temp)
                    temp=[]
            self.handle_items(temp)
        elif isinstance(input_items,list):
            self.handle_items(input_items)
        else:
            self.handle_items([input_items])


if __name__ == '__main__':
    with tqdm(total=100) as bar:
        for i in range(10):
            time.sleep(0.1)
            bar.update(10)