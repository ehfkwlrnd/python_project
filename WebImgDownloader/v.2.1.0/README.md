# README

* 세팅
	1. 파이썬 버전 3.6 이상으로 설치

	2. 파이썬모듈 설치
		```text
		명령 프롬프트에서 다음과 같이 입력하여 필요한 파이썬 모듈을 설치한다.
		pip install requests
		pip install beautifulsoup4
		pip install selenium
		```
		
	3. 크롬 드라이버 다운로드

	   ![img02][link02]

	   [link02]:./img/02.png
	   
	   버전 확인

	   

	   ![img03][link03]

	   [link03]:./img/03.png
	   
	   버전에 맞는 크롬 드라이버 다운로드

* 클래스 구분
	1. WebImgDownloader
		
		> requests로 html소스 읽어옴
	2. SWebImgDownloader
		
		> selenium으로 html소스 읽어옴
		
	3. TWebImgDownloader 
	
		> requests로 html소스 읽어오고 스레싱하여 작억
		
	4. STWebImgDownloader
	
		> selenium으로 html소스 읽어오고 스레싱하여 작업
	
* 사용법
	1. url 확인

		![img04][link04]
		
		[link04]:./img/04.png
		
		url 확인
		
		
		
	2. 셀렉터 확인
		
		![img05][link05]
		
		[link05]:./img/05.png
		
		개발자 도구를 이용하여 셀렉터 확인
		
		
		
	3. 코드 실행

		```python
		#WebImgDownloader 사용 (TWebImgDownloader도 마찬가지)
	   from webimgdownloader import WebImgDownloader as wid
	   
	   base = 'https://comic.naver.com'
	   w = wid(base)
	   
	   url = 'https://comic.naver.com/webtoon/detail.nhn?titleId=734348&no=1&weekday=thu'
	   title_selector = 'div.view > h3'
	   img_selector = '#comic_view_area > div >img'
	   img_src = 'src'
	   folder = 'D:/Users/yuno/Desktop/testfolder'
	   w.one(url, title_selector, img_selector, img_src, folder)
	   ```
	   ```python
	   #SWebImgDownloader 사용 (STWebImgDownloader도 마찬가지)
	   from webimgdownloader import SWebImgDownloader as swid
	   
	   base = 'https://comic.naver.com'
	   driverLoc = 'D:/Users/yuno/Desktop/driver/chromedriver'
	   w = swid(base, driverLoc)
	   
	   url = 'https://comic.naver.com/webtoon/detail.nhn?titleId=734348&no=1&weekday=thu'
	   img_selector = '#comic_view_area > div >img'
	   img_src = 'src'
	   folder = 'D:/Users/yuno/Desktop/testfolder'
	   w.one(url, title_selector, img_selector, img_src, folder)
	   
	   w.close()
	   ```
  
   
  
   
  
   
  
   
  



