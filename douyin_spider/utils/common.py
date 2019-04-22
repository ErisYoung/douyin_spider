import datetime
from datetime import timedelta,time,date
import dateparser

birthday_sep='-'

def set_class_attr(self,data):
    for key in data:
        setattr(self,key,key)


def parse_datetime(date):
    if not date:
        return None
    if isinstance(date,str) and date.find(birthday_sep):
        return dateparser.parse(date)
    elif isinstance(date,str):
        return fix_cn_parse__year_error(dateparser.parse(str(date)))
    elif isinstance(date,int):
        return dateparser.parse(str(date))

def fix_cn_parse__year_error(date_obj):
    year = date_obj.year
    str_date = date_obj.strftime("%m-%d %H:%M:%S")
    str_date = str(int(year)-1) + "-" + str_date
    new_date_obj = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    return new_date_obj

def dateparser_parse(date):
    return dateparser.parse(date)


def get_array_first(array):
    if array and isinstance(array,list) and len(array)>=1:
        return array[0]
    return None

if __name__ == '__main__':
    date_obj=parse_datetime("1993-01-01")
    print(date_obj)




