from selenium_imgdown import WebImgDownloader as wid

## """New tokki"""

##base = 'https://newtoki20.net/'
##driverLoc = 'C:/Users/강하일/Downloads/chromedriver_win32/chromedriver'
##w = wid(base, driverLoc)

## """one"""

##url = 'https://newtoki22.com/bbs//board.php?bo_table=webtoon&wr_id=256540'
##file_selector = 'div.view-content img'
##file_src = 'data-original'
##folder = 'C:/Users/강하일/Desktop/mytong/웹툰/나 혼자만 레벨업'
##w.one(url, file_selector, file_src, folder)

## """multi"""

##for page in range(1, 8):
##    url = 'https://newtoki22.net/bbs/search.php?stx=%EC%9D%BC%EC%A7%84%EB%85%80+%EA%B8%B8%EB%93%A4%EC%9D%B4%EA%B8%B0&gr_id=&srows=20&onetable=&page=' + str(page+1)
##    link_selector = 'div.media > div.media-body > a'
##    link_src = 'href'
##    file_selector = 'div.view-content > img'
##    file_src = 'data-original'
##    folder = 'C:/Users/강하일/Desktop/mytong/웹툰/일진 길들이기'
##    w.multi(url, link_selector,link_src, file_selector, file_src, folder)


##"""Mana Moa"""

base = 'https://manamoa.net/'
driverLoc = 'C:/Users/강하일/Desktop/study/sel/chromedriver'
w = wid(base, driverLoc)

## """one"""

##url = 'https://manamoa.net/bbs/board.php?bo_table=manga&wr_id=261261'
##file_selector = 'div.view-content > img'
##file_src = 'src'
##folder = 'C:/Users/강하일/Desktop/mytong/만화/욘n무'
##w.one(url, file_selector, file_src, folder)

## """multi"""

url = 'https://manamoa.net/bbs/page.php?hid=manga_detail&manga_id=1689'
link_selector = 'div.chapter-list > div.slot > a'
link_src = 'href'
file_selector = 'div.view-content > img'
file_src = 'src'
folder = 'C:/Users/강하일/Desktop/mytong/만화/흑의계약자_칠흙의 꽃'
w.multi(url, link_selector,link_src, file_selector, file_src, folder)

## common

w.close()
