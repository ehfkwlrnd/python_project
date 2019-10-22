# README

# 해당 모듈의 목적 : 웹툰과 같은 연속적인 이미지의 다운로드

# 필요한 모듈 : urllib, BeautifulSoup, selenium

# class : WebImgDownloader
- field :
  - (string) base : 베이스가 되는 웹사이트 주소 (ex:https://www.naver.com)
  - (string) driver : 웹드라이버(크롬)
  
+ method :
  + one(url, selector, src, folder) : 1회차 분량의 이미지(만화)를 다운로드 받음
    - (string) url : 해당 페이지의 url
    - (string) selector : 만화 이미지에 해당하는 img태그의 selector
    - (string) src : img태그의 data링크 (주로 "src")
    - (string) folder : 이미지들이 저장될 폴더 경로
    
  + multi(url, link_selector, link_src, file_selector, file_src, folder, start=None, end=None) 
  : 목록 페이지를 바탕으로 여러회차의 이미지(만화)를 다운로드 받음
    - (string) url : 목록 페이지의 url
    - (string) link_selector : 목록태그들의 selector
    - (string) link_src : 목록태그 안의 링크 src (주로 "href")
    - (string) file_selecotr : 만화 이미지에 해당하는 img태그의 selector
    - (string) file_src : 만화 img태그의 data링크 (주로 "src")
    - (string) folder : 이미지들이 저장될 폴더 경로
    - (int) start : 목록 중 시작할 목록의 인덱스 (즉, 다운받지 않을 목록의 개수)
    - (int) end : 목록 중 끝마칠 목록의 인덱스
    
  + close() : WebImgDownloader를 사용 후 close 하도록 한다.
