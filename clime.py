import requests
from bs4 import BeautifulSoup
import os

def fetch_urls(base_url):
    # 发送请求获取HTML内容
    response = requests.get(base_url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'lxml')

    # select：#__next > div > main > div.h-full.w-full > div.scrollbar-thin.gutter-stable.overflow-y-auto.mx-4 > div > div > table > tbody > tr:nth-child(1) > td.bg-black.px-4.py-1.font-normal.transition-all.ease-in-out.group-hover\:bg-gray-900.whitespace-nowrap.border-b.border-gray-800\/80.first\:border-l.last\:border-r.h-\[3\.375rem\].md\:py-\[0\.3125rem\].xl\:h-\[2\.8125rem\].sticky.left-0.z-10 > div > a

    # 使用XPath的模式来找到所有的a标签
    # 注意：BeautifulSoup不支持XPath，这里我们通过CSS选择器来模拟XPath的功能
    # a_tags = soup.select('div.main div div table tbody tr td div a')
    # test_tag = soup.find_all(name = 'a', class_ = "caption-1 truncate flex flex-col font-light text-gray-400 xl:flex-row xl:items-center" )
    print(soup.title)
    for child in soup.recursiveChildGenerator():
        if child.name:
            print(child.name)
    test_tag = soup.select("#__next > div > main > div.h-full.w-full > div.scrollbar-thin.gutter-stable.overflow-y-auto.mx-4 > div > div > table > tbody > tr:nth-child(1) > td.bg-black.px-4.py-1.font-normal.transition-all.ease-in-out.group-hover\:bg-gray-900.whitespace-nowrap.border-b.border-gray-800\/80.first\:border-l.last\:border-r.h-\[3\.375rem\].md\:py-\[0\.3125rem\].xl\:h-\[2\.8125rem\].sticky.left-0.z-10 > div > a")
    print(test_tag)
    print(len(test_tag))
    # print(a_tags)
    # 获取所有链接
    hrefs = [a['href'] for a in a_tags if a.has_attr('href')]
    print(hrefs)

    return hrefs[:50]  # 限制为前50个元素

def save_web_content(urls, folder='webhrefs'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, url in enumerate(urls, start=1):
        response = requests.get(url)
        # 假设我们只需要保存网页的文本内容
        filename = os.path.join(folder, f'web_{i}.html')
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f'Saved {url} to {filename}')

if __name__ == '__main__':
    base_url = 'https://www.geckoterminal.com/base/pools'
    urls = fetch_urls(base_url)
    # save_web_content(urls)
