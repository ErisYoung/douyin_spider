import logging
import requests as rq
from retrying import retry
from douyin_spider.config import get_timeout, retry_max_random_wait, retry_min_random_wait, retry_max_number

# disable the security warning
logging.captureWarnings(True)


def retry_exception_func(exception):
    """
    callback function of retry decorator
    :param exception:
    :return:if occurs one exception,then return True,else return False
    """
    result = isinstance(exception, (rq.ConnectionError, rq.ReadTimeout))
    if result:
        print("Exception", type(exception), "occured,retring...")
    return result


@retry(stop_max_attempt_number=retry_max_number, wait_random_min=retry_min_random_wait,
       wait_random_max=retry_max_random_wait, retry_on_exception=retry_exception_func)
def _get(url, **kwargs):
    """
    request url
    :param url:
    :param kwargs:
    :return:
    """
    kwargs.update({'verify': False, 'timeout': get_timeout})
    res = rq.get(url, **kwargs)
    if res.status_code != 200:
        raise rq.ConnectionError("Expected status_code 200,but get {}".format(res.status_code))
    return res.json()


def get(url, **kwargs):
    """
    get json data from API
    :param url:
    :param kwargs:
    :return:
    """
    try:
        result = _get(url, **kwargs)
    except (rq.ConnectionError, rq.ReadTimeout):
        result = {}
    return result


if __name__ == '__main__':
    pass
