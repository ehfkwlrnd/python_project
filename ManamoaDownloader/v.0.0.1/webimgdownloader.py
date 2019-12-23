#version 2.1.0

from bs4 import BeautifulSoup as bs
import urllib.request as req
import urllib.parse as parse
from selenium import webdriver
import os
from datetime import datetime
from zipfile import ZipFile
import requests
import threading


class WebImgDownloader:
    def __init__(self, base):
        self.base = base
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'}

    def __one(self, url, title_selector, img_selector, img_src, folder):
        log = ''
        i = 0
        try:
            url = parse.urljoin(self.base, url)
            html = requests.get(url, headers=self.headers).text
            soup = bs(html, 'html.parser')

            title = self.regularize(soup.select(title_selector)[0].get_text())
            print(title)

            log = f'{datetime.now()}\n{title}'
            path = f'{folder}/{title}.zip'
            with ZipFile(path, 'w') as zf:
                imgs = soup.select(img_selector)
                for img in imgs:
                    i += 1
                    url = parse.urljoin(self.base, img[img_src])
                    file = f'{i}.jpg'
                    r = requests.get(url, headers=self.headers)
                    zf.writestr(file, r.content)
                    print(file)
        except KeyboardInterrupt:
            print('강제 종료')
            log += '(강제 종료) '
            raise KeyboardInterrupt
        except Exception as e:
            print('error : ', e)
            log += f' error -> {e}\n'
        except:
            print('Unexpected Error')
            log += '(Unexpected Error)'
        finally:
            log += f' : {i}장 다운로드\n'
            self.writeLog(log)

    def one(self, url, title_selector, img_selector, img_src, folder):
        self.writeLog('============ one ============\n')
        self.__one(url, title_selector, img_selector, img_src, folder)
        self.writeLog('=============================\n')

    def multi(self, url, title_selector, link_selector, link_href, img_selector, img_src, folder, start=None, end=None):
        url = parse.urljoin(self.base, url)
        html = requests.get(url, headers=self.headers).text
        soup = bs(html, 'html.parser')

        links = soup.select(link_selector)[start:end]
        i = 0
        self.writeLog('============ multi ==========\n')
        try:
            for link in links:
                i += 1
                url = link[link_href]
                parse.urljoin(self.base, url)
                self.__one(url, title_selector, img_selector, img_src, folder)
        except KeyboardInterrupt:
            pass

        self.writeLog(f'{i}개 다운로드\n')
        self.writeLog('=============================\n')

    def regularize(self, title):
        title = title.replace('\\', '_') \
            .replace('/', '_') \
            .replace(':', '_') \
            .replace('>', '_') \
            .replace('<', '_') \
            .replace('*', '_') \
            .replace('?', '_') \
            .replace('"', '_') \
            .replace('|', '_')
        return title

    def writeLog(self, log):
        with open('log.txt', 'a') as f:
            f.write(log)

class TWebImgDownloader:
    def __init__(self, base):
        self.base = base
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'}
        opener = req.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        req.install_opener(opener)

    def __one(self, url, title_selector, img_selector, img_src, folder):
        log = ''
        i = 0
        try:
            url = parse.urljoin(self.base, url)
            html = requests.get(url, headers=self.headers).text
            soup = bs(html, 'html.parser')

            title = self.regularize(soup.select(title_selector)[0].get_text())
            print(title)

            log = f'{datetime.now()}\n{title}'
            
            path = f'{folder}/{title}'
            if not os.path.isdir(path):
                os.mkdir(path)
                
            imgs = soup.select(img_selector)
            for img in imgs:
                i += 1
                url = parse.urljoin(self.base, img[img_src])
                file = f'{i}.jpg'
                threading.Thread(target=req.urlretrieve, args=(url, f'{path}/{file}')).start()
                print(file)
        except KeyboardInterrupt:
            print('강제 종료')
            log += '(강제 종료) '
            raise KeyboardInterrupt
        except Exception as e:
            print('error : ', e)
            log += f' error -> {e}\n'
        except:
            print('Unexpected Error')
            log += '(Unexpected Error)'
        finally:
            log += f' : {i}장 다운로드\n'
            self.writeLog(log)

    def one(self, url, title_selector, img_selector, img_src, folder):
        self.writeLog('============ one ============\n')
        self.__one(url, title_selector, img_selector, img_src, folder)
        self.writeLog('=============================\n')

    def multi(self, url, title_selector, link_selector, link_href, img_selector, img_src, folder, start=None, end=None):
        url = parse.urljoin(self.base, url)
        html = requests.get(url, headers=self.headers).text
        soup = bs(html, 'html.parser')

        links = soup.select(link_selector)[start:end]
        i = 0
        self.writeLog('============ multi ==========\n')
        try:
            for link in links:
                i += 1
                url = link[link_href]
                parse.urljoin(self.base, url)
                self.__one(url, title_selector, img_selector, img_src, folder)
        except KeyboardInterrupt:
            pass

        self.writeLog(f'{i}개 다운로드\n')
        self.writeLog('=============================\n')

    def regularize(self, title):
        title = title.replace('\\', '_') \
            .replace('/', '_') \
            .replace(':', '_') \
            .replace('>', '_') \
            .replace('<', '_') \
            .replace('*', '_') \
            .replace('?', '_') \
            .replace('"', '_') \
            .replace('|', '_')
        return title

    def writeLog(self, log):
        with open('log.txt', 'a') as f:
            f.write(log)

class SWebImgDownloader:
    def __init__(self, base, driverLoc):
        self.base = base
        self.driver = webdriver.Chrome(driverLoc)
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'}

    def __one(self, url, title_selector, img_selector, img_src, folder):
        log = ''
        i = 0
        try:
            url = parse.urljoin(self.base, url)
            self.driver.get(url)
            html = self.driver.page_source
            soup = bs(html, 'html.parser')
            
            title = self.regularize(soup.select(title_selector)[0].get_text())
            print(title)
            
            log = f'{datetime.now()}\n{title}'
            path = f'{folder}/{title}.zip'
            with ZipFile(path, 'w') as zf:
                imgs = soup.select(img_selector)
                for img in imgs:
                    i += 1
                    url = parse.urljoin(self.base, img[img_src])
                    file = f'{i}.jpg'
                    r = requests.get(url, headers=self.headers)
                    zf.writestr(file, r.content)
                    print(file)
        except KeyboardInterrupt:
            print('강제 종료')
            log += '(강제 종료) '
            raise KeyboardInterrupt
        except Exception as e:
            print('error : ', e)
            log += f' error -> {e}\n'
        except:
            print('Unexpected Error')
            log += '(Unexpected Error)'
        finally:
            log += f' : {i}장 다운로드\n'
            self.writeLog(log)
    def one(self, url, title_selector, img_selector, img_src, folder):
        self.writeLog('============ one ============\n')
        self.__one(url, title_selector, img_selector, img_src, folder)
        self.writeLog('=============================\n')

    def multi(self, url, title_selector, link_selector, link_href, img_selector, img_src, folder, start=None, end=None):
        url = parse.urljoin(self.base, url)
        self.driver.get(url)
        html = self.driver.page_source
        soup = bs(html, 'html.parser')  

        links = soup.select(link_selector)[start:end]
        i = 0
        self.writeLog('============ multi ==========\n')
        try:
            for link in links:
                i += 1
                url = link[link_href]
                parse.urljoin(self.base, url)
                self.__one(url, title_selector, img_selector, img_src, folder)
        except KeyboardInterrupt:
            pass
            
        self.writeLog(f'{i}개 다운로드\n')
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

class STWebImgDownloader:
    def __init__(self, base, driverLoc):
        self.base = base
        self.driver = webdriver.Chrome(driverLoc)
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'}

        opener = req.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        req.install_opener(opener)

    def __one(self, url, title_selector, img_selector, img_src, folder):
        log = ''
        i = 0
        try:
            url = parse.urljoin(self.base, url)
            self.driver.get(url)
            html = self.driver.page_source
            soup = bs(html, 'html.parser')
            
            title = self.regularize(soup.select(title_selector)[0].get_text())
            print(title)
            
            log = f'{datetime.now()}\n{title}'

            path = f'{folder}/{title}'
            if not os.path.isdir(path):
                os.mkdir(path)
                
            imgs = soup.select(img_selector)
            for img in imgs:
                i += 1
                url = parse.urljoin(self.base, img[img_src])
                file = f'{i}.jpg'
                threading.Thread(target=req.urlretrieve, args=(url, f'{path}/{file}')).start()
                print(file)

        except KeyboardInterrupt:
            print('강제 종료')
            log += '(강제 종료) '
            raise KeyboardInterrupt
        except Exception as e:
            print('error : ', e)
            log += f' error -> {e}\n'
        except:
            print('Unexpected Error')
            log += '(Unexpected Error)'
        finally:
            log += f' : {i}장 다운로드\n'
            self.writeLog(log)
    def one(self, url, title_selector, img_selector, img_src, folder):
        self.writeLog('============ one ============\n')
        self.__one(url, title_selector, img_selector, img_src, folder)
        self.writeLog('=============================\n')

    def multi(self, url, title_selector, link_selector, link_href, img_selector, img_src, folder, start=None, end=None):
        url = parse.urljoin(self.base, url)
        self.driver.get(url)
        html = self.driver.page_source
        soup = bs(html, 'html.parser')  

        links = soup.select(link_selector)[start:end]
        i = 0
        self.writeLog('============ multi ==========\n')
        try:
            for link in links:
                i += 1
                url = link[link_href]
                parse.urljoin(self.base, url)
                self.__one(url, title_selector, img_selector, img_src, folder)
        except KeyboardInterrupt:
            pass
            
        self.writeLog(f'{i}개 다운로드\n')
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
