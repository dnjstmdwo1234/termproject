import os
import sys
import urllib.request
import time

# 크롬브라우저를 조작하기 위한 모듈
from selenium import webdriver
# 크롤링을 위한 뷰티풀숲 모듈
from bs4 import BeautifulSoup
# 페이지 스크롤링을 위한 모듈
from selenium.webdriver.common.keys import Keys
# 크롬드라이버 저장 위치
driver = webdriver.Chrome('/home/다운로드')
# 암묵적으로 웹 자원을 최대 3초간 기다리기
driver.implicitly_wait(3)
# 망고플레이트 서울맛집 페이지 실행
driver.get('https://www.mangoplate.com/search/%EC%84%9C%EC%9A%B8/')
# 암묵적으로 웹 자원을 최대 1초간 기다리기
driver.implicitly_wait(1)
# 광고창 없애기
html = driver.page_source
# BeautifulSoup 사용하기
soup = BeautifulSoup(html, 'html.parser')
# 망고플레이트 서울맛집 검색결과 중 업체명을 restaurant 변수에 저장
notices = soup.select('main > article > div > div > div > section > div > ul > li > div > figure > figcaption > div > a > h2')
# 드라이버 종료
restaurant = []
# 메뉴바의 내용을 출력
for n in notices:
    restaurant.append(n.text.strip())
print(restaurant)
real_address = []
# 검색창에 전송할 주소 입력
for i in restaurant:
    # 네이버 지도 페이지 실행
    driver.get('https://map.naver.com/')
    # 암묵적으로 웹 자원을 최대 1초간 기다리기
    driver.implicitly_wait(1)
    driver.find_element_by_id('search-input').send_keys(i)
    # 각각의 업체명을 검색
    driver.find_element_by_xpath('//*[@class="spm spm_ssch nclicks(STA.go)"]').click()
    # html이라는 변수안에 페이지의 element(요소) 전부 가져오기
    driver.implicitly_wait(3)
    html = driver.page_source
    # BeautifulSoup 사용하기
    soup = BeautifulSoup(html, 'html.parser')
    # 검색결과 중 도로명 주소를 address 변수에 저장
    notices = soup.select('div > div > div > div > div > div > div > div >  ul > li > div > dl > dd')
    address = []
    # 메뉴바의 내용을 출력
    for n in notices:
        address.append(n.text.strip())
    # 출력된 address 중 address[0]에 들어있는 주소를 활용한다. 즉 네이버 지도 
    # 주소 검색에서 최상단에 위치한 것을 표시한다.
    real_address.append(address[0])

# 드라이버 종료
driver.close()

client_id = "EdZNtHONbxw2jRx6a_Fv"
client_secret = "SdSawUbcCR"
wedo_restaurant = []
keungdo_restaurant = []
for i in real_address:
    encText = urllib.parse.quote(i)
    url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        # response_body type이 str이란 것을 알았고 위도와 경도를 뽑아서 출력하기 위해 몇번째인지 직접 세서 아래와 같이 코드를 짰다.
        wedo_restaurant.append(float(response_body.decode('utf-8')[-98:-89]))
        keungdo_restaurant.append(float(response_body.decode('utf-8')[-60:-51]))
        
    else:
        print("Error Code:" + rescode)
print(wedo_restaurant,keungdo_restaurant)


