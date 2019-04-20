import datetime
from datetime import timedelta,time,date
import dateparser

def parse_datetime(date_string):
    if not date_string:
        return None
    return fix_cn_parse__year_error(dateparser.parse(str(date_string)))

def fix_cn_parse__year_error(date_obj):
    year = date_obj.year
    str_date = date_obj.strftime("%m-%d %H:%M:%S")
    str_date = str(int(year)-1) + "-" + str_date
    new_date_obj = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    return new_date_obj

if __name__ == '__main__':
    date_obj=parse_datetime("4月20日 18:10")
    print(date_obj)


