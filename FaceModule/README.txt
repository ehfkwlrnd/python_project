# README

# 해당 모듈의 목적 : Azure Face Web API를 빠르게 이용하도록 모듈화

# 필요한 모듈 : requests, json

# class : FaceAPI
- field :
  - (string) key : 
  - (string) endPoint : 
  
+ method :
  + Detect(imgPath) : 사진의 얼굴을 인식하여 결과값 반환
    - (string) imgPath: 사진의 url
   