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

####The first approach:choose downloader and handler to download what you want 

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
💨note:if you use mongo_handler to save data,you should have one and start it

Result:

![4.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux5fnxzj30wp0e078x.jpg)
![5.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux5kulnj319x09uwmp.jpg)
![6.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux4gxauj319k09ldg6.jpg)
![7.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux4i58yj312b0e8ju0.jpg)

####The second approach:use command-line arguments
first,you should get share_url you want

<p align="center">
<img src="https://ws3.sinaimg.cn/large/005BYqpggy1g2yuhcwjxij30ku112qns.jpg" width="160">
<img src="https://ws3.sinaimg.cn/large/005BYqpggy1g2yuhansloj30ku112jt2.jpg" width="160">
<img src="https://ws3.sinaimg.cn/large/005BYqpggy1g2yuhb3f0vj30ku112jv8.jpg" width="160">
</p>

and put the url as the input parameters,default download 10 videos
```bash
cd douyin_spider/tests
python assign_share_url.py -u "http://v.douyin.com/6Gf7FG/" 

```
💨note:you should use "" to package the url,or it will report errors in Windows

please use --help to get more parameters:
```bash
python assign_share_url.py --help
```

#####💨note:if you have another question,you can issue it

## More examples

See [tests](tests)

## More Downloader

See [downloaders](douyin_spider/downloaders)

## More Handler

See [handler](douyin_spider/handler)




