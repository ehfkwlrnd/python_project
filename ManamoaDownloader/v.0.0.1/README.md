# ManamoaDownloader
> 마나모아 사이트의 만화를 다운로드하는 프로그램

webimgdownloader 모듈을 사용하여 이미지를 다운받는 기능을, tkinter모듈을 사용하여 GUI프로그램으로 만들보았다.

## 사용 예제

* params.txt 에 프로그램 실행에 필요한 정보들이 담겨있다. driverLoc에는 chromedriver의 위치를 지정해준다. 나머진 마나모아 사이트 정보가 바뀔때 조금씩 수정하면 된다.

  ![img01][img01]

  ![img02][img02]

* ManamoaDownloader.py를 실행하면 굉장히 직관적인 프로그램이 실행된다. 이후는 설명없이 잘 사용할 수 있을 것이다.

## 개발 환경 설정

윈도우 기준으로 작성되었으며, 다음과 같이 pip를 통해 파이썬 모듈을 설치해야 함

```sh
pip install requests
pip install beautifulsoup4
pip install selenium
```

## 업데이트 내역

* 0.0.1
    * 코드 최초 작성(연습용이기 때문에 업데이트 예정은 없음)

## 정보

ehfkwlrnd – ehfkwlrnd@naver.com

[https://github.com/ehfkwlrnd/python_project](https://github.com/ehfkwlrnd/python_project)



<!-- Markdown link & img dfn's -->

[img01]: ./img/01.png
[img02]: ./img/02.png

