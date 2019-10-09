from bs4 import BeautifulSoup as bs
import urllib.request as request
import urllib.parse as parse
from selenium import webdriver
import os
from datetime import datetime

class WebImgDownloader:
    def __init__(self, base, driverLoc):
        self.base = base
        self.driver = webdriver.Chrome(driverLoc)
        
        opener = request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        request.install_opener(opener)

    def one(self, url, selector, src, folder):
        try:
            url = parse.urljoin(self.base, url)
            self.driver.get(url)
            html = self.driver.page_source
            soup = bs(html, 'html.parser')
            
            title = soup.select('title')[0].get_text()
            title = self.regularize(title)
            print(title)
            
            log = str(datetime.now()) + '\n\r'
            log += title
            folder = folder + '/' + title
            if not os.path.isdir(folder):
                os.mkdir(folder)
            
            imgs = soup.select(selector)
            i = 0      
            for img in imgs:
                i += 1
                url = img[src]
                parse.urljoin(self.base, url)
                file = str(i) + '.jpg'
                request.urlretrieve(url, folder+'/'+file)
                print(file)
        except Exception as e:
            print('error : ' + e)
            log += ' error -> ' + e
        finally:
            log += ' : ' + str(i) + '장 다운로드\n\r'
            self.writeLog(log)

    def multi(self, url, link_selector, link_src, file_selector, file_src, folder, start=None, end=None):
        url = parse.urljoin(self.base, url)
        self.driver.get(url)
        html = self.driver.page_source
        soup = bs(html, 'html.parser')  

        links = soup.select(link_selector)[start:end]
        i = 1
        self.writeLog('============ multi ===========\n\r')
        for link in links:
            url = link[link_src]
            parse.urljoin(self.base, url)
            self.one(url, file_selector, file_src, folder)
            i += 1
        self.writeLog(str(i)+'개 다운로드\n\r')
        self.writeLog('=============================\n\r')

    def regularize(self, title):
        title = title.replace('\\', '_')
        title = title.replace('/', '_')
        title = title.replace(':', '_')
        title = title.replace('>', '_')
        title = title.replace('<', '_')
        title = title.replace('*', '_')
        title = title.replace('?', '_')
        title = title.replace('"', '_')
        title = title.replace('|', '_')
        return title

    def writeLog(self, log):
        f = open('log.txt', 'a')
        f.write(log)
        f.close()

    def close(self):
        self.driver.quit()

