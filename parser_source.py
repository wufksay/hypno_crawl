from bs4 import BeautifulSoup
class Parser_source(object):
    def __init__(self,html_list):
        self.html_list = html_list
    def paeser(self):
        for i,html in enumerate(self.html_list):
            soup = BeautifulSoup(html, 'html.parser')
            download_url = soup.find('source')['src']
            with open(f'download.txt','a') as f:
                f.write(download_url + '\n')