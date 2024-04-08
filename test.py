from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import os
import time

# 现在设计是机器模拟手动看，找到存在时间少于1小时的币，而官方twitter上关注数值大于20000的项目
# way suggestions：pool大小 200w - 2000w，尽量改成3分钟，使用机器人交易防止滑县
# questions： 要不要继续使用这种模拟查找的方式？ 要不要去高级的爬虫？110页的币怎么快速的进行遍历？

# todo1：添加循环计时：每间隔3分钟统计数据
# todo2: 添加翻页功能：pages
# todo3: 挂到服务器上：mac服务器，ssh连接，方便
# todo4: 发送微信提醒：使用PyOfficeRobot
# todo？：添加其他的链？：先搞base链，因为way神对base链项目熟悉，所以稳一点，下一步就是Solana链

def checkBase():
    driver = webdriver.Chrome(options=options)
    # todo：目前是只做了第一页，而且数据只有20，可能是js渲染需要时间等待 
    driver.get("https://www.geckoterminal.com/base/pools")
    time.sleep(20)
    html = driver.page_source
    print(html)
    soup = BeautifulSoup(html, 'lxml')
    test_tag = soup.find_all(name = 'a', class_ = "caption-1 truncate flex flex-col font-light text-gray-400 xl:flex-row xl:items-center" )
    print(test_tag)
    print(len(test_tag))
    hrefs = [a['href'] for a in test_tag if a.has_attr('href')]
    print(hrefs)
    for u in hrefs:
        if(checkSample(u)):
            print('找到一个好的币：' + u )
            # todo 记录币名字，Twitter的url：u，产生时间，【5分，小时，日，月收益】，币的地址
            # 微信机器人提醒发群
    # checkSample(hrefs[0])
    driver.quit()

def checkSample(linkUrl):
    print('linkUrl:' + linkUrl)
    driver = webdriver.Chrome(options=options)
    url = topUrl + linkUrl
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # time
    time_tag = soup.select('#__next > div > main > div.flex.w-full.flex-col.gap-y-2.md\:flex-row.md\:gap-x-4.md\:gap-y-0.md\:px-4 > div.min-w-layout.flex.flex-col.md\:hidden > div.space-y-2.px-2.sm\:px-4 > div > div.rounded.border.border-gray-800.min-w-\[20rem\].flex-1.p-2.sm\:p-4.md\:min-w-0.md\:flex-none > table > tbody > tr:nth-child(4) > td > span' )
    # print('time!!!' + time_tag)
    print(time_tag[0].text)
    # todo 检查这个币的存在时间
    timeNum = time_to_seconds(time_tag[0].text)
    if(timeNum > 60*60):
        return False

    # twitter
    twitter_tag = soup.find_all(name = 'a', class_ = "inline-flex items-center justify-center gap-1 font-normal text-white focus:outline-none transition-all duration-150 active:translate-y-2 bg-gray-900 border border-gray-800 shadow-button-tertiary hover:bg-gray-800 hover:shadow-gray-600 hover:border-gray-600 text-sm rounded-md shadow-none active:transform-none h-full w-7 p-1.5" )
    print(twitter_tag)
    print(len(twitter_tag))
    hrefs = [a['href'] for a in twitter_tag if a.has_attr('href')]
    print(hrefs)
    twitterUrl = ''
    for href in hrefs:
        if 'twitter' in href:
            twitterUrl = href
            break
    driver.quit()
    if(twitterUrl != ''):
        print('twitterUrl:' + twitterUrl)
        if (checkTwitterFollow(twitterUrl)):
            return True
    return False
    

def checkTwitterFollow(twitterUrl):
    driver = webdriver.Chrome(options=options)
    driver.get(twitterUrl)
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    follows = soup.select('#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-175oi2r.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a > span.css-1qaijid.r-bcqeeo.r-qvutc0.r-poiln3.r-1b43r93.r-1cwl3u0.r-b88u0q > span')
    print(follows[0].text) # 2.8万
    num = chinese_number_to_int(follows[0].text)
    print(num)
    # 2.8万 -> 28000
    driver.quit()
    if(num > 20000):
        return True
    return False

def chinese_number_to_int(chinese_number):
    units = {'千': 10000,'万': 10000, '亿': 100000000}
    unit = 1
    for u in units:
        if u in chinese_number:
            unit = units[u]
            chinese_number = chinese_number.replace(u, '')
            break
    return int(float(chinese_number) * unit)

def time_to_seconds(time_str):
    # 定义每个时间单位对应的秒数
    time_units = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 24 * 3600,
        "week": 7 * 24 * 3600,
        "month": 30 * 24 * 3600,
        "year": 365 * 24 * 3600,
    }
    
    # 将输入字符串分割为数量和单位
    parts = time_str.split()
    if len(parts) != 2:
        raise ValueError("Invalid time format. Please use the format '<number> <unit>'.")
    
    number, unit = parts
    number = int(number)  # 将数量转换为整数
    
    # 处理单位的单数和复数形式
    unit = unit.lower().rstrip('s')
    if unit not in time_units:
        raise ValueError(f"Unknown time unit: {unit}")
    
    # 计算总秒数
    total_seconds = number * time_units[unit]
    
    return total_seconds
    # 2 months -> 2 * 60 * 30 * 24 * 60 * 60
    # # 示例
    # print(chinese_number_to_int('2.8万'))  # 输出: 28000
    # print(chinese_number_to_int('1.5亿'))  # 输出: 150000000

    # follows = 
    # <span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3" style="text-overflow: unset;">2.8万</span>
# 设置Selenium浏览器选项，以便模拟浏览器用户代理

# 初始化WebDriver


# 打开网页

# 等待20秒钟，让JavaScript加载完成

# 获取页面源代码

# test_tag = soup.find_all("#__next > div > main > div.h-full.w-full > div.scrollbar-thin.gutter-stable.overflow-y-auto.mx-4 > div > div > table > tbody > tr:nth-child(1) > td.bg-black.px-4.py-1.font-normal.transition-all.ease-in-out.group-hover\:bg-gray-900.whitespace-nowrap.border-b.border-gray-800\/80.first\:border-l.last\:border-r.h-\[3\.375rem\].md\:py-\[0\.3125rem\].xl\:h-\[2\.8125rem\].sticky.left-0.z-10 > div > a")




# url = topUrl + hrefs[0]
# driver2.get(url)
# time.sleep(5)
# html2 = driver.page_source
# driver2.quit()


# [<a class="caption-1 truncate flex flex-col font-light text-gray-400 xl:flex-row xl:items-center" href="/base/pools/0xc9034c3e7f58003e6ae0c8438e7c8f4598d5acaa" title="DEGEN / WETH 0.3%"><span><span class="text-gray-200">DEGEN</span>/<!-- -->WETH</span><div class="caption-3 truncate text-gray-500 hover:no-underline xl:ml-2">Degen</div></a>]
# print(soup.title)
# print(soup)
# 关闭浏览器
# driver.quit()

# 现在你可以使用BeautifulSoup或其他工具来解析html变量中的内容

def checkTwitterFollowRequest(twitterUrl):
    response = requests.get(twitterUrl)
    # driver = webdriver.Chrome(options=options)
    # driver.get(twitterUrl)
    # time.sleep(10)
    # html = driver.page_source
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'lxml')
    follows = soup.select('#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-175oi2r.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a > span.css-1qaijid.r-bcqeeo.r-qvutc0.r-poiln3.r-1b43r93.r-1cwl3u0.r-b88u0q > span')
    print(follows[0].text) # 2.8万
    num = chinese_number_to_int(follows[0].text)
    print(num)
    # 2.8万 -> 28000
    # driver.quit()
    if(num > 20000):
        return True
    return False

if __name__ == '__main__':
    topUrl = 'https://www.geckoterminal.com'
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    # checkBase()
    # checkSample('/base/pools/0xc9034c3e7f58003e6ae0c8438e7c8f4598d5acaa')
    # checkTwitterFollow('https://twitter.com/degentokenbase')
    checkTwitterFollowRequest('https://twitter.com/degentokenbase')

    # test for time_to_seconds
    # print(time_to_seconds('2 months'))
    # print(time_to_seconds('2 days'))
    # print(time_to_seconds('2 minutes'))
    # print(time_to_seconds('1 day'))
    # print(time_to_seconds('2 hours'))
    # print(time_to_seconds('2 months'))
    # print(time_to_seconds('2 years'))
    

