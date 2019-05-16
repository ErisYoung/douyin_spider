# 抖音爬虫

抓取抖音App的视频爬虫

## 环境

> Python3

## 安装配置
首先，你需要安装并配置好**Node.js**环境,然后bash运行

```bash
$ git clone git@github.com:ErisYoung/douyin_spider.git
$ cd douyin_spider
$ pip install -r requirements.txt
```

## 使用方法

#### 第一种方式:选择下载器和处理器,自行编写

你可以按如下方式使用:

```python
from douyin_spider.downloaders.video import VideoDownloader
from douyin_spider.handler.video import VideoHandler
from douyin_spider.handler.music import MusicHandler
from douyin_spider.handler.mongodb import MongoHandler
from douyin_spider.enter.hot_top import hot_top20

video_handler = VideoHandler(folder='./videos')
music_handler = MusicHandler(folder='./musics')
mongo_handler = MongoHandler()
downloader = VideoDownloader([video_handler,music_handler,mongo_handler])

result = hot_top20()

for item in result.data:
    downloader.download(item)

print("success")

```

💨注意:如果要使用mongo_handler,则需要提前启动mongodb

结果:

![4.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux5fnxzj30wp0e078x.jpg)
![5.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux5kulnj319x09uwmp.jpg)
![6.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux4gxauj319k09ldg6.jpg)
![7.jpg](https://ws3.sinaimg.cn/large/005BYqpggy1g2yux4i58yj312b0e8ju0.jpg)


#### 第二种方式:使用命令行参数
首先获取你所需要的share-url

<p align="center">
<img src="https://ws3.sinaimg.cn/large/005BYqpggy1g2yuhcwjxij30ku112qns.jpg" width="160">
<img src="https://ws3.sinaimg.cn/large/005BYqpggy1g2yuhansloj30ku112jt2.jpg" width="160">
<img src="https://ws3.sinaimg.cn/large/005BYqpggy1g2yuhb3f0vj30ku112jv8.jpg" width="160">
</p>


然后把得到的url,输入命令行，默认下载10个视频
```bash
cd douyin_spider/tests
python assign_share_url.py -u "http://v.douyin.com/6Gf7FG/" 

```
💨注意:这里要使用"",否则Windows环境下会出现error

更多的参数使用自行help查阅:
```bash
python assign_share_url.py --help
```

##### 💨提示:有其他问题可以自行issue

## 更多的例子和入口

请看 [tests](tests)

## 更多的下载器

请看 [downloaders](douyin_spider/downloaders)

## 更多的处理器

请看 [handler](douyin_spider/handler)

#### 更新时间

2019-5-13: 👌处理_signature 签名参数,实测可行





