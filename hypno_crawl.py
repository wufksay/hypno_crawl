import requests
from bs4 import BeautifulSoup
import re
resp = [None] * 5
soup = [None] * 5
cookie = {'your cookies'}
for i in range(5):
    try:
        resp[i] = requests.get(
            f'https://hypnotube.com/channels/9/cuckold-hypnotube/rating/page{i}.html?durationTo=900',
            cookies=cookie,
            verify=False  # 忽略 SSL 验证
        )
        with open(f'hypno{i}.html', 'w') as f:
            f.write(resp[i].text)
        soup[i] = BeautifulSoup(resp[i].text, 'html.parser')
    except requests.exceptions.SSLError as e:
        print(f"SSL 错误: {e}, URL: page{i}.html")
for i in range(1, 5):
    with open(f'hypno{i}.html', 'r') as f:
        links_with_video = BeautifulSoup(f.read(), 'html.parser').find_all(
            'a', href=re.compile(r'video.*html$'))
    for link in links_with_video:
        try:
            url = link['href']  # 获取 href 属性值
            resp = requests.get(url, cookies=cookie, verify=False)  # 忽略 SSL 验证
            soup = BeautifulSoup(resp.text, 'html.parser')
            new_url = soup.find('source')['src']  # 获取 source 标签的 src 属性
            # with open(f'new_url[index + 6:-4]mp4','wb') as f:
            #     f.write(requests.get(new_url,cookies=cookie).content)
            with open('new_url.txt', 'a') as f:
                f.write(new_url + '\n')  # 写入新链接并换行
        except requests.exceptions.SSLError as e:
            print(f"SSL 错误: {e}, URL: {url}")
        except Exception as e:
            print(f"其他错误: {e}, URL: {url}")
