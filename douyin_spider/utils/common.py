"""In the module,it provides some common functions to use

Available functions:

"""
import datetime
import re
from datetime import timedelta, time, date
import dateparser
import requests as rq
from douyin_spider.config import birthday_sep, headers, dytk_base_url, HEADERS


def set_class_attr(self, data):
    """
    use list to set attribute dynamically
    :param self:object
    :param data:attribute list
    :return:
    """

    for key in data:
        setattr(self, key, key)


def parse_datetime(date):
    """
    parse string date to datetime type
    :param date:
    :return:
    """
    if not date:
        return None
    if isinstance(date, str) and date.find(birthday_sep):
        return dateparser.parse(date)
    elif isinstance(date, str):
        return fix_cn_parse_year_error(dateparser.parse(str(date)))
    elif isinstance(date, int):
        return dateparser.parse(str(date))


def fix_cn_parse_year_error(date_obj):
    """
    fix dateparser lib can't parse " 月 日" bug
    :param date_obj:
    :return:
    """
    year = date_obj.year
    str_date = date_obj.strftime("%m-%d %H:%M:%S")
    str_date = str(int(year) - 1) + "-" + str_date
    new_date_obj = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    return new_date_obj


def dateparser_parse(date):
    """
    parse string date to datetime type
    :param date:
    :return:
    """
    return dateparser.parse(date)


def get_array_first(array):
    """
    get array first
    :param array:
    :return:
    """
    if array and isinstance(array, list) and len(array) >= 1:
        return array[0]
    return None


def get_current_timestamp():
    """
    get current timestamp
    :return: timestamp
    """
    now = datetime.datetime.now()
    return int(now.timestamp())


def get_real_url(url):
    """
    parse url to read share url
    :param url: origin url
    :return:real url
    """
    if isinstance(url, str):
        res = rq.get(url, headers=headers)
        return res.url


def get_real_address_from_short(url):
    """
    parse short url to read share url
    :param url:short url
    :return:real url
    """
    if isinstance(url, str):
        res = rq.get(url, headers=HEADERS, allow_redirects=False)
        return res.headers['Location'] if res.status_code == 302 else None


def get_user_dytk_by_id(user_id):
    """
    get user dytk parameter by user id in share url
    :param user_id:
    :return:
    """
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
