"""In the module,set default config parameters

you can set your own parameters

"""

# downloader
INIT_DOWNLOADER_BATCH_SIZE = 10

# get parameters
get_timeout = 5
retry_max_number = 10
retry_min_random_wait = 1000
retry_max_random_wait = 5000

# enter
headers = {'User-Agent': 'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}
hot_music_url = "https://aweme.snssdk.com/aweme/v1/hotsearch/music/billboard/?version_code=5.5.0&pass-region=1&pass-route=1&js_sdk_version=1.12.0.2&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=de1ae3452f4c0d33795e12fe4d4224fcf4f52160&os_api=18&ac=WIFI&os_version=11.3.1&device_platform=iphone&build_number=55011&device_type=iPhone7,2&iid=67030863950&idfa=A5198308-FD4E-40A4-9630-9900B20E38D7&type=0&mas=013ca1905d580de8826c40058f7ff140e876bcfd0fada8a0d228d8&as=a275c45cd77bdce5dd1867&ts=1556956599"
hot_positive_energy_url = 'https://api.amemv.com/aweme/v1/hotsearch/positive_energy/billboard/?version_code=5.5.0&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&aid=1128&os_version=11.3.1&device_platform=iphone&device_type=iPhone7,2'
hot_search_url = 'https://api.amemv.com/aweme/v1/hot/search/list/'
hot_star_url = "https://api.amemv.com/aweme/v1/hotsearch/star/billboard/?version_code=5.5.0&pass-region=1&pass-route=1&js_sdk_version=1.12.0.2&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=de1ae3452f4c0d33795e12fe4d4224fcf4f52160&os_api=18&ac=WIFI&os_version=11.3.1&device_platform=iphone&build_number=55011&device_type=iPhone7,2&iid=67030863950&idfa=A5198308-FD4E-40A4-9630-9900B20E38D7&type=0&mas=0154d1c244712b7a4cb317bdb0482cc5c3c640c3df778b22d554e1&as=a2b5dd7dd9d43c74639759&ts=1557386313"
hot_top_url = "https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/?version_code=5.5.0&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&os_version=11.3.1&device_platform=iphone&device_type=iPhone7,2"

# handler
GET_DICT_PARAMS = {'timeout': 50}
REDIRECT_URL_HEAD = "https://aweme.snssdk.com/aweme"

# models
HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}
share_challenge_base_url = "https://www.iesdouyin.com/aweme/v1/challenge/aweme/"
share_music_base_url = "https://www.iesdouyin.com/web/api/v2/music/list/aweme/"
share_user_base_url = "https://www.iesdouyin.com/web/api/v2/aweme/post/"

# commom
birthday_sep = '-'
dytk_base_url = "https://www.iesdouyin.com/share/user/{user_id}?utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy&iid=67030863950"

# extension
extension_to_type_mapping_dict = {
    'txt': 'text/plain',
    'htm': 'text/html',
    'html': 'text/html',
    'php': 'text/html',
    'css': 'text/css',
    'js': 'application/javascript',
    'json': 'application/json',
    'xml': 'application/xml',
    'swf': 'application/x-shockwave-flash',
    'flv': 'video/x-flv',

    # images
    'png': 'image/png',
    'jpe': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'gif': 'image/gif',
    'bmp': 'image/bmp',
    'ico': 'image/vnd.microsoft.icon',
    'tiff': 'image/tiff',
    'tif': 'image/tiff',
    'svg': 'image/svg+xml',
    'svgz': 'image/svg+xml',

    # archives
    'zip': 'application/zip',
    'rar': 'application/x-rar-compressed',
    'exe': 'application/x-msdownload',
    'msi': 'application/x-msdownload',
    'cab': 'application/vnd.ms-cab-compressed',

    # audio/video
    'mp3': 'audio/mpeg',
    'ogg': 'audio/ogg',
    'qt': 'video/quicktime',
    'mp4': 'video/mp4',
    'mov': 'video/quicktime',
    'wav': 'audio/x-wav',
    'avi': 'application/octet-stream',

    # adobe
    'pdf': 'application/pdf',
    'psd': 'image/vnd.adobe.photoshop',
    'ai': 'application/postscript',
    'eps': 'application/postscript',
    'ps': 'application/postscript',

    # ms office
    'doc': 'application/msword',
    'rtf': 'application/rtf',
    'xls': 'application/vnd.ms-excel',
    'ppt': 'application/vnd.ms-powerpoint',

    # open office
    'odt': 'application/vnd.oasis.opendocument.text',
    'ods': 'application/vnd.oasis.opendocument.spreadsheet',
}
