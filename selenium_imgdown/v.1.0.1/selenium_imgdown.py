from bs4 import BeautifulSoup as bs
import urllib.parse as parse
from selenium import webdriver
import os
from datetime import datetime

class WebImgDownloader:
    def __init__(self, base, driverLoc):
        self.base = base
        self.driver = webdriver.Chrome(driverLoc)

    def __one(self, url, selector, src, folder):
        try:
            url = parse.urljoin(self.base, url)
            self.driver.get(url)
            html = self.driver.page_source
            soup = bs(html, 'html.parser')
            
            title = self.regularize(soup.select('title')[0].get_text())
            print(title)
            
            log = f'{datetime.now()}\n{title}'
            path = f'{folder}/{title}'
            if not os.path.isdir(path):
                os.mkdir(path)
            
            imgs = soup.select(selector)
            i = 0      
            for img in imgs:
                i += 1
                url = parse.urljoin(self.base, img[src])
                file = f'{i}.jpg'
                request.urlretrieve(url, f'{path}/{file}')
                print(file)
        except KeyboardInterrupt:
            print('강제 종료')
            log += '(강제 종료) '
        except Exception as e:
            print('error : ', e)
            log += f' error -> {e}\n'
        except:
            print('Unexpected Error')
            log += '(Unexpected Error)'
        finally:
            log += f' : {i}장 다운로드\n'
            self.writeLog(log)
    def one(self, url, selector, src, folder):
        self.writeLog('============ one ============\n')
        self.__one(url, selector, src, folder)
        self.writeLog('=============================\n')

    def multi(self, url, link_selector, link_src, file_selector, file_src, folder, start=None, end=None):
        url = parse.urljoin(self.base, url)
        self.driver.get(url)
        html = self.driver.page_source
        soup = bs(html, 'html.parser')  

        links = soup.select(link_selector)[start:end]
        i = 0
        self.writeLog('============ multi ==========\n')
        for link in links:
            i += 1
            url = link[link_src]
            parse.urljoin(self.base, url)
            self.__one(url, file_selector, file_src, folder)
            
        self.writeLog('f{i}개 다운로드\n')
        self.writeLog('=============================\n')

    def regularize(self, title):
        title = title.replace('\\', '_')\
                        .replace('/', '_')\
                        .replace(':', '_')\
                        .replace('>', '_')\
                        .replace('<', '_')\
                        .replace('*', '_')\
                        .replace('?', '_')\
                        .replace('"', '_')\
                        .replace('|', '_')
        return title

    def writeLog(self, log):
        with open('log.txt', 'a') as f:
            f.write(log)
            f.close()

    def close(self):
        self.driver.quit()

