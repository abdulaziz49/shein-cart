import requests
import re


def query_string_to_dict(query_string) -> dict:
    result = {}
    pairs = query_string.split('&')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            result[key] = value
    return result


# input
user_input = 'http://api-shein.shein.com/h5/sharejump/appjump?link=Vy4b13hk4x1&localcountry=YE&url_from=GM7483908192896647168'

url = user_input[:user_input.index('?')]
params = user_input[user_input.index('?') + 1:]

headers = {
    'Host': 'api-shein.shein.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
first_requests = requests.get(url=url, params=params, headers=headers)
shareId = re.search(r'\"shareId\":\"([^"]+)', first_requests.text)
group_id = shareId.group(1)
res = query_string_to_dict(params)

headers2 = {
    'Host': 'm.shein.com',
    'Smdeviceid': 'Wlsel6H6wYo1B25w/itTg95pXcK7jxU4Zn1hRnOh7giWKiL5K4AasaqdbNYK7QeF47p8qKNGboDo5GBb/PXpiLaI6WvkkPly8kzPM2HgvCAKWZZ8HNUZUf3JqzduJkvlrLyWUgiseQG2VSoa5ZR3EiKJcdDB7Fzl/YHGQHFcSxGLuBDbD+PMZXtvMR8ugQEL9E16yd0pYauL8eBvjGFK/GhfDDuUJlvoPL+6ZIilp/0WDcNYlP8AQsQzcWXG0Nv3+vhVWKZ4fcqE=1487577677129',
    'Armortoken': 'S1_2.3.1_YWU2pdzo8g6nJyp8gUI7AYgOX7ilGHd7SMBNCu2Nmx9PBll3nCctSjO6B98u3YE7rQ-vUI2ulum3I96nsLXT5Seipt4tpVGiWWgojRbiJWZgkTifsvMj42YWMfH29ZL8mWe6IP3nn0n9OpytTJO3sTaxsFX-mxhO2f55skNo46JD-6oqWaklVocjnbzKGI57kpO3gc866EM8zKdwPjIOjTfTymypNUpBflBUjHBL-Miho4BFYiLbqP6IppdE7jQupOYAGR1N8wDwO7ZN3wSJ36S3c_6EWZ8KsfKCaX5kZ3ggnWNWklc1bEJ7Nik2zp8dj7TI5GroaCu79TlMkP1IGw1708795473217',
    'X-Csrf-Token': 'bWOolpdu-5Rcrtv-X11n2EtpJOWnNiciiRFw',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Uber-Trace-Id': 'ffac591e7260ed81:ffac591e7260ed81:0:0',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Gw-Auth': 'a=xjqHR52UWJdjKJ0x6QrCsus66rNXR9@2.0.13&b=1708795526800&d=06942fbc37be6a98b8dee877d03ae8f6&e=TXWIpNzViNjM0M2Y4ZDI1MDUzZWVmMWIwMzhmYTE2Nzc4ZTQzYTMxYmQyOGViNTMwZDM3NGRjNGZhMDVkMzU0MDRlZA%3D%3D',
    'Timezone': 'GMT+3',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': f'https://m.shein.com/cart/share/landing?group_id={group_id}&local_country={res["localcountry"]}&utm_campaign=&url_from={res["url_from"]}',
    'Accept-Language': 'en-US,en;q=0.9',
}

params2 = {
    '_ver': '1.1.8',
    '_lang': 'en',
    'group_id': f'{group_id}',
    'local_country': 'YE',
}

response2 = requests.get(
    'https://m.shein.com/api/cart/socialShareGoodsInfo/get',
    params=params2,
    headers=headers2,
).json()

print(response2)
