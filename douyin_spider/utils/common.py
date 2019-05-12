import datetime
import re
from datetime import timedelta, time, date
import dateparser
import requests as rq

birthday_sep = '-'
headers = {'User-Agent': 'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}
dytk_base_url = "https://www.iesdouyin.com/share/user/{user_id}?utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy&iid=67030863950"
HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}


def set_class_attr(self, data):
    for key in data:
        setattr(self, key, key)


def parse_datetime(date):
    if not date:
        return None
    if isinstance(date, str) and date.find(birthday_sep):
        return dateparser.parse(date)
    elif isinstance(date, str):
        return fix_cn_parse__year_error(dateparser.parse(str(date)))
    elif isinstance(date, int):
        return dateparser.parse(str(date))


def fix_cn_parse__year_error(date_obj):
    year = date_obj.year
    str_date = date_obj.strftime("%m-%d %H:%M:%S")
    str_date = str(int(year) - 1) + "-" + str_date
    new_date_obj = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    return new_date_obj


def dateparser_parse(date):
    return dateparser.parse(date)


def get_array_first(array):
    if array and isinstance(array, list) and len(array) >= 1:
        return array[0]
    return None


def get_current_timestamp():
    now = datetime.datetime.now()
    return int(now.timestamp())


def get_real_url(url):
    if isinstance(url, str):
        res = rq.get(url, headers=headers)
        return res.url


def get_real_address_from_short(url):
    if isinstance(url, str):
        res = rq.get(url, headers=HEADERS, allow_redirects=False)
        return res.headers['Location'] if res.status_code == 302 else None


def get_user_dytk_by_id(user_id):
    url = dytk_base_url.format(user_id=user_id)
    res = rq.get(url, headers=headers)
    if res and res.status_code == 200:
        dytk = re.findall(r"dytk: '(.*)'", res.content.decode("utf_8"))
        return get_array_first(dytk)


if __name__ == '__main__':
    date_obj = parse_datetime("5月9日 15:00")
    print(date_obj)
    print(get_current_timestamp())
    print(get_user_dytk_by_id("56630472225"))
