import logging
import requests as rq
from retrying import retry
# 禁用安全请求警告

logging.captureWarnings(True)

get_timeout = 5
retry_max_number = 10
retry_min_random_wait = 1000
retry_max_random_wait = 5000


def retry_exception_func(exception):
    result = isinstance(exception, (rq.ConnectionError, rq.ReadTimeout))
    if result:
        print("Exception", type(exception), "occured,retring...")
    return result


@retry(stop_max_attempt_number=retry_max_number, wait_random_min=retry_min_random_wait,
       wait_random_max=retry_max_random_wait, retry_on_exception=retry_exception_func)
def _get(url, **kwargs):
    kwargs.update({'verify': False, 'timeout': get_timeout})
    res = rq.get(url, **kwargs)
    if res.status_code != 200:
        raise rq.ConnectionError("Expected status_code 200,but get {}".format(res.status_code))
    return res.json()


def get(url, **kwargs):
    try:
        result = _get(url, **kwargs)
    except (rq.ConnectionError, rq.ReadTimeout):
        result = {}
    return result

if __name__ == '__main__':
    pass

