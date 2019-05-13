"""In the module,set default config parameters

"""

# downloader
INIT_DOWNLOADER_BATCH_SIZE = 10

# enter
headers = {'User-Agent': 'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet'}
hot_music_url = "https://aweme.snssdk.com/aweme/v1/hotsearch/music/billboard/?version_code=5.5.0&pass-region=1&pass-route=1&js_sdk_version=1.12.0.2&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=de1ae3452f4c0d33795e12fe4d4224fcf4f52160&os_api=18&ac=WIFI&os_version=11.3.1&device_platform=iphone&build_number=55011&device_type=iPhone7,2&iid=67030863950&idfa=A5198308-FD4E-40A4-9630-9900B20E38D7&type=0&mas=013ca1905d580de8826c40058f7ff140e876bcfd0fada8a0d228d8&as=a275c45cd77bdce5dd1867&ts=1556956599"
hot_positive_energy_url = 'https://api.amemv.com/aweme/v1/hotsearch/positive_energy/billboard/?version_code=5.5.0&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&aid=1128&os_version=11.3.1&device_platform=iphone&device_type=iPhone7,2'
hot_search_url = 'https://api.amemv.com/aweme/v1/hot/search/list/'
hot_star_url = "https://api.amemv.com/aweme/v1/hotsearch/star/billboard/?version_code=5.5.0&pass-region=1&pass-route=1&js_sdk_version=1.12.0.2&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=de1ae3452f4c0d33795e12fe4d4224fcf4f52160&os_api=18&ac=WIFI&os_version=11.3.1&device_platform=iphone&build_number=55011&device_type=iPhone7,2&iid=67030863950&idfa=A5198308-FD4E-40A4-9630-9900B20E38D7&type=0&mas=0154d1c244712b7a4cb317bdb0482cc5c3c640c3df778b22d554e1&as=a2b5dd7dd9d43c74639759&ts=1557386313"
hot_top_url = "https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/?version_code=5.5.0&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&os_version=11.3.1&device_platform=iphone&device_type=iPhone7,2"



music_to_video_url = "https://aweme.snssdk.com/aweme/v1/music/aweme/?version_code=5.5.0&pass-region=1&pass-route=1&js_sdk_version=1.12.0.2&app_name=aweme&vid=8151CF55-2B6D-49FE-899D-BE87BE3F70D9&app_version=5.5.0&device_id=19511267298&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=de1ae3452f4c0d33795e12fe4d4224fcf4f52160&os_api=18&ac=WIFI&os_version=11.3.1&device_platform=iphone&build_number=55011&device_type=iPhone7,2&iid=67030863950&idfa=A5198308-FD4E-40A4-9630-9900B20E38D7&cursor=0&music_id=6680033039914896142&pull_type=2&count=18&type=6&mas=01a7ff72fb345e84bf636b08f713894f4df3df39cefe5715102eb8&as=a235965c4e38acf80d0407&ts=1556965518"
music_to_video_headers = {'user-agent': 'Aweme 5.5.0 rv:55011 (iPhone; iOS 11.3.1; zh_CN) Cronet',
                          'x-khronos': '1556965519', 'x-pods': '',
                          'x-gorgon': '83000000000044942c0ab28e07fa479ba98685d18bc91ff08464'}
