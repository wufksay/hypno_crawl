from bs4 import BeautifulSoup
import re
class Parser_hypno(object):
    def __init__(self,html_list):
        self.html_list = html_list
    def paeser(self):
        for i,html in enumerate(self.html_list):
            soup = BeautifulSoup(html, 'html.parser')
            find_each_video = soup.find_all('a', href=re.compile(r'video.*html$'))
            each_url_list = [i['href'] + '\n' for i in find_each_video]
            with open(f'hypno_html/links_in_html{i}.txt','w') as f:
                f.writelines(each_url_list)
            