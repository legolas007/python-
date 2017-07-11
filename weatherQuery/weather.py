#coding: utf-8
import urllib.request
import json
from city import city

cityname = input("输入查询的城市：\n")
citycode = city.get(cityname)
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html'%citycode)
    content = urllib.request.urlopen(url).read()
    data = json.loads(content)
    res = data["weatherinfo"]
    str_tmp = ("%s :%s~%s")%(res["weather"],res["temp1"],res["temp2"])
    print(str_tmp)


