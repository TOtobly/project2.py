# project2.py
import requests,json
def get_date():
    url = 'https://api.ip.sb/jsonip'
    proxy_date = {
        'http':'http://50180+JP+50180-183285069680:totoha@JP-30m.geosurf.io:8000/',
        'https':'http://50180+JP+50180-183285069680:totoha@JP-30m.geosurf.io:8000/'
    }
    response = requests.get(url,proxies=proxy_date)
    j = json.loads(response.text)
    print(j)
get_date()
