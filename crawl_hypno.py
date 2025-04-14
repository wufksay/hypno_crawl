import requests
class Crawl_hypno(object):
    def __init__(self,url_list,cookie):
        self.url_list = url_list
        self.cookie = cookie
    def crawl(self):
        for i,url in enumerate(self.url_list):
            try:
                resp = requests.get(url,cookies=self.cookie,verify=False)
                with open(f'hypno_html/hypno{i}.html', 'w') as f:
                    f.write(resp.text)
            except requests.exceptions.SSLError as e:
                print(f"SSL 错误: {e}, URL: page{i}.html")

