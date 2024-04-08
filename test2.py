# 使用requests库实现爬虫
# base链作测试

'''
base:
https://www.geckoterminal.com/_next/data/MPw9oApqmVnpOFYxI7Fmh/en/explore/new-crypto-pools/base.json?network=base
curl 'https://www.geckoterminal.com/_next/data/MPw9oApqmVnpOFYxI7Fmh/en/explore/new-crypto-pools/base.json?network=base' \
  -H 'authority: www.geckoterminal.com' \
  -H 'accept: */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cookie: _sharedid=db320619-e101-407f-a5ac-9e5bfc100cdb; ahoy_visitor=f1ee90f4-74cf-4dde-aeeb-3b1c864a8f7f; OptanonAlertBoxClosed=2024-03-30T11:15:36.227Z; eupubconsent-v2=CP8RPcAP8RPcAAcABBENAuEsAP_gAEPgABJ4g1NX_H__bW9r8X73aft0eY1P99j77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIEu3bBIQNlHJDUTVigaogVryDMakWcgTNKJ6BkiFMRO2dYCF5vmwtj-QKY5vp993dx2Det_dv83dzyz4VHn3a5_2e0WJCdA58tDfv9bROb-9IPd_58v4v0_F_rE2_eT1l_tevp7D8-ft87_XW-9_fff79LgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQagCzDQqIA-yJCQg0DCKBACoKwgIoEAAAAJA0QEAJgwKdgYBLrCRACAFAAMEAIAAUZAAgAAEgAQiACQAoEAAEAgUAAIAAAgEADAwABgAsBAIAAQHQIUwIIFAsAEjMiIUwIAoEggJbKhBIAgQVwhCLPAggERMFAAACQAVgACAsFgMSSAlYkECXEG0AABAAgEEIFQik7MAQwJmy1V4om0ZWkBaIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAACAA.f_wACHwAAAAA; _pbjs_userid_consent_data=3145127298759532; ahoy_visit=47ddfb77-8437-47c5-85b7-6932e993025f; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Apr+02+2024+10%3A06%3A29+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202312.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=bb290096-7714-4fb7-9a6c-e23a0b4a0b87&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1%2CV2STACK42%3A1&geolocation=DE%3BNW&AwaitingReconsent=false; mp_604ec6861e5a709347ca3e3807a92e0f_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18e8f125bcf52c4-0151092ca0f083-1e525637-16a7f0-18e8f125bcf52c4%22%2C%22%24device_id%22%3A%20%2218e8f125bcf52c4-0151092ca0f083-1e525637-16a7f0-18e8f125bcf52c4%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.coingecko.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.coingecko.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.coingecko.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.coingecko.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; amp_2d2f38=4YbxPB5YqsT4tw2VYQfNMB...1hqe6f6v6.1hqe8tkld.30.0.30; cto_bundle=lwmD_l9BdU81Y0xLNjZNZEU1ZiUyQjMzU0xIUW9WNHN1RzBEOTdnOVU1c3hGeTFxcGpqZ0JEWUFselpBTEJUUk9WSFRndXBEd1dBeGh0UmlLVTc0Z01ySmd0cWM1OEJQWWpSQkhRaVhZOEptU1JKbkh3NnZsM2FhV011dkZkbTdNR0Eya0hI; cto_bidid=im6WoV91MDh3OUZxb3UwaVdCVVFtbm1RclF2ZDc3WWElMkI4cVdsUjRrV2E5bGhRaDNoQkpJc0Q3cjdvUTQ0bkxraVhUQWV1dUN0aVdOdks1V1lLUXRjN0dLMzhBJTNEJTNE; __cf_bm=PmxjQudUGkftgCPnk3Rz.TCoHHm47N4amV3LyilcqGQ-1712023700-1.0.1.1-a5GrYR1F9d7UoFYwk7ZA6ZDp6nwSwBbQ5wNMWd1gU2G73Cuiv5O9EjWVvxc7MGgo1fWKmuG9TEo2vhwYhdFbLA' \
  -H 'if-none-match: W/"871mnb1v822tzn"' \
  -H 'purpose: prefetch' \
  -H 'referer: https://www.geckoterminal.com/base/pools' \
  -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'sec-ch-ua-platform: "Android"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36' \
  -H 'x-nextjs-data: 1' \
  --compressed

  
DEGEN / WETH
"id": "163416532",
        "type": "pool",
        "attributes": {
            "address": "0x2c4909355b0c036840819484c3a882a95659abf3",
            "name": "DEGEN / WETH",
            "from_volume_in_usd": "3197477.15537675",
            "to_volume_in_usd": "3197477.15537675",
            "api_address": "0x2c4909355b0c036840819484c3a882a95659abf3",
            "swap_count_24h": 4856,
            "price_percent_change": "-14.89%",
            "price_percent_changes": {
                "last_5m": "-0.7%",
                "last_15m": "-1.29%",
                "last_30m": "-0.46%",
                "last_1h": "-2.93%",
                "last_6h": "-8.81%",
                "last_24h": "-14.89%"
            },
            "pool_fee": null,
            "base_token_id": "31312229",
            "token_value_data": {
                "30162518": {
                    "fdv_in_usd": 336405050.69519454,
                    "market_cap_in_usd": 0.0
                },
                "31312229": {
                    "fdv_in_usd": 1725265512.531636,
                    "market_cap_in_usd": 582543307.3778956
                }
            },
            "price_in_usd": "0.0467432171441508",
            "reserve_in_usd": "1552168.23923",
            "aggregated_network_metrics": {
                "total_swap_volume_usd_24h": "7944186636.16181413003916",
                "total_swap_volume_usd_48h_24h": "5963446341.4079387658375",
                "total_swap_count_24h": 11924391,
                "total_swap_volume_percent_change_24h": "33.2146913270663025544156661132967674806761954941777095"
            },
            "pool_created_at": "2024-01-11T23:59:02.457Z"
        },
curl 'https://app.geckoterminal.com/api/p1/base/pools?include=dex%2Cdex.network%2Cdex.network.network_metric%2Ctokens&page=1&include_network_metrics=true' \
  -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Referer: https://www.geckoterminal.com/' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36' \
  -H 'sec-ch-ua-platform: "Android"' \
  --compressed
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
import time
import calendar

def checkBase():
    url = 'https://app.geckoterminal.com/api/p1/base/pools'
    params = {
        'include': 'dex,dex.network,dex.network.network_metric,tokens',
        # 改page换页
        'page': '1',
        'include_network_metrics': 'true'
    }
    headers = {
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.geckoterminal.com/',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua-platform': '"Android"'
    }

# response2 = requests.get('https://www.geckoterminal.com/zh/base/pools/0xd0b53d9277642d899df5c87a3966a349a798f224')
# soup = BeautifulSoup(response2.text, 'lxml')
# print(soup.title)
# time_tag = soup.select('#__next > div > main > div.flex.w-full.flex-col.gap-y-2.md\:flex-row.md\:gap-x-4.md\:gap-y-0.md\:px-4 > div.min-w-layout.flex.flex-col.md\:hidden > div.space-y-2.px-2.sm\:px-4 > div > div.rounded.border.border-gray-800.min-w-\[20rem\].flex-1.p-2.sm\:p-4.md\:min-w-0.md\:flex-none > table > tbody > tr:nth-child(4) > td > span' )
#                         #__next > div > main > div.flex.w-full.flex-col.gap-y-2.md\:flex-row.md\:gap-x-4.md\:gap-y-0.md\:px-4 > div.min-w-layout.flex.flex-col.md\:hidden > div.space-y-2.px-2.sm\:px-4 > div > div.rounded.border.border-gray-800.min-w-\[20rem\].flex-1.p-2.sm\:p-4.md\:min-w-0.md\:flex-none > table > tbody > tr:nth-child(4) > td > span
# # print('time!!!' + time_tag)
# print(time_tag[0].text)
# exit(0)

# 200页是因为我没找到一个链的币有50 * 200个以上
    for i in range(1, 11):
        params['page'] = str(i)

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            content = response.text
            contentJson = json.loads(content)
            print(len(contentJson['data'])) # 50 每页有50个
            if(len(contentJson['data']) == 0) :
                break

            for item in contentJson['data']:
                attr = item['attributes']
                print(item['id'])
                print(attr['name'])
                print(attr['address'])
                print(attr['api_address'])
                # 24H VOL 币池的24小时交易量
                print(attr['swap_count_24h']) 
                # 币的创建时间 UTC时间
                timeStr = attr['pool_created_at']
                print(timeStr) 
                # Age
                timeNum = (int)(getCurUtcTime() - getUtcTime(timeStr))
                # 超过一天的币没有大的潜力
                if(timeNum > 60 * 60 * 24):
                    continue
                ageStr = timeDiffToStr(timeNum)
                print(ageStr)
                # LIQUIDITY 币池的流动性

                # FDV
                # Market Cap
                # TwitterUrl
                # TwitterFollow

                # https://www.geckoterminal.com/zh/base/pools/0xd0b53d9277642d899df5c87a3966a349a798f224
                # https://www.geckoterminal.com/zh/base/pools/ + attr['api_address']
                print('\n')
        else:
            print('请求失败:', response.status_code)

    # print(content)
def printRed(s):
    print('\033[31m' + str(s) + '\033[0m')

def getCurUtcTime():
    return time.time()

def getUtcTime(timeStr):
    dt = datetime.strptime(timeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
    timestampUtc = calendar.timegm(dt.utctimetuple()) + (dt.microsecond / 1e6)
    printRed(timestampUtc)
    return timestampUtc

def timeDiffToStr(timeNum):
    diffSeconds = int(timeNum)
    minute = 60
    if diffSeconds < minute:
        return f"{diffSeconds}秒前"
    return f"{diffSeconds // minute}分钟前"

if __name__ == '__main__':

    # check ISO 8601时间转成UTC时间戳
    # time_str =  "2024-01-11T23:59:02.457Z"
    # dt = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    # timestamp_utc = calendar.timegm(dt.utctimetuple()) + (dt.microsecond / 1e6)
    # timestamp = time.mktime(dt.timetuple()) + (dt.microsecond / 1e6)
    # printRed(timestamp)
    # printRed(timestamp_utc) #utc时间比unix时间多8小时

    # 微信上要发的消息
    message = ''
    checkBase()
    # checkBase()
