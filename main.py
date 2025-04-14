from  crawl_hypno import Crawl_hypno
from  parser_hypno import Parser_hypno
from crawl_source import Crawl_source
from parser_source import Parser_source
from collections import deque
import json
import os
url_list = [f'https://hypnotube.com/channels/9/cuckold-hypnotube/rating/page{i}.html' for i in range(1,6)]
with open('cookie.json', 'r') as f:
    cookie = f.read()
cookie = json.loads(cookie)
if __name__ == '__main__':
    crawl = Crawl_hypno(url_list,cookie)
    crawl.crawl()
    html_list = [None] * 5
    for i in range(0,5):
        with open(f'hypno_html/hypno{i}.html','r') as f:
            html_list[i] = f.read()
    parser = Parser_hypno(html_list)
    parser.paeser()
    d = deque()
    for i in range(0,5):
        with open(f'hypno_html/links_in_html{i}.txt','r') as f:
            d.append(f.readlines())
    total_url = [item for item in d]
    total_url = [i[:-1] for item in total_url for i in item]
    crawl_source_url = Crawl_source(total_url,cookie)
    crawl_source_url.crawl()
    source_html_list = [file for file in os.listdir('source_html') if not(os.path.isdir(file))]
    source_html_list_update = [None] * len(source_html_list)
    for i,source_html in enumerate(source_html_list):
        with open('source_html/' + source_html,'r') as f:
            source_html_list_update[i] = f.read()
    parser_source = Parser_source(source_html_list_update)
    parser_source.paeser()