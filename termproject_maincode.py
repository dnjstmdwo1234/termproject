
from flask import Flask, render_template, request
import csv
import random
import os
import sys
import urllib.request
import time



# 따릉이위치
f = open('parkbicyclenew2.csv', 'r', encoding='UTF8')
rdr = csv.reader(f)
wedo = []
keungdo = []
for line in rdr:
    wedo.append(float(line[5]))
    keungdo.append(float(line[6]))
f.close()


# 공원위치
fp = open('park_location4.csv','r',encoding='utf=8')
crd = csv.reader(fp)
lat = []
lon = []
for lines in crd:
    lat.append(float(lines[5]))
    lon.append(float(lines[6]))

fp.close()



wedorestaurant = [127.03769, 127.03675, 127.04458, 127.02773, 126.98096, 126.98718, 127.10484, 127.03986, 126.91091, 127.04918, 127.02441, 127.03624, 126.97311, 126.91977, 127.04206, 126.9844, 126.9265, 126.89779, 126.93195, 127.00515]
keungdorestaurant = [37.525388, 37.525474, 37.549705, 37.52327, 37.560916, 37.541167, 37.508644, 37.522927, 37.551341, 37.523498, 37.471304, 37.523026, 37.573795, 37.546161, 37.522874, 37.486034, 37.561628, 37.526507, 37.607311, 37.55588]



# app 객체 생성
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
# 뷰함수 -> 화면 표시 함수
# templates 폴더 아래의 index.html 로 연결
def hello_world():
    return render_template('tvtvtv.html', wedo=wedo)


@app.route('/map/', methods=['POST'])
def apple():

    maping = request.form['maping']

   
    return render_template('jidopage.html', maping=maping, wedo=wedo, keungdo=keungdo, lat=lat, lon=lon, wedorestaurant = wedorestaurant, keungdorestaurant = keungdorestaurant)



# 앱 실행
if __name__ == "__main__":
    app.run(debug=True)

