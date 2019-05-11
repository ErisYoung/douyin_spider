# douyin_spider

Crawler of DouYin App

## Environment

> Python3

## Installation
First of all,you need install and configure **Node.js**

```bash
$ git clone git@github.com:ErisYoung/douyin_spider.git
$ cd douyin_spider
$ pip install -r requirements.txt
```

## Usage

And you can use like:

```python
from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.handler.video import VideoHandler
from douyin_spider.handler.music import MusicHandler
from douyin_spider.handler.mongodb import MongoHandler
from douyin_spider.enter.hot_top import hot_top20

video_handler = VideoHandler(folder='./videos')
music_handler = MusicHandler(folder='./musics')
mongo_handler = MongoHandler()
downloader = VideoDownloader([video_handler])

result = hot_top20()

for item in result.data:
    downloader.download(item)

print("success")

```

Result:

![EfYcRA.png](https://s2.ax1x.com/2019/05/11/EfYcRA.png)
![EfY6Gd.png](https://s2.ax1x.com/2019/05/11/EfY6Gd.png)
![EfYgxI.png](https://s2.ax1x.com/2019/05/11/EfYgxI.png)
![EfYyPH.png](https://s2.ax1x.com/2019/05/11/EfYyPH.png)
![EfYrIe.png](https://s2.ax1x.com/2019/05/11/EfYrIe.png)

## More examples

See [tests](tests)

## More Downloader

See [downloaders](douyin_spider/downloaders)

## More Handler

See [handler](douyin_spider/handler)




