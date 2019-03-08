import requests
r=requests.get('http://www.weather.com.cn/data/sk/101280101.html')
r.encoding='utf-8'
print("城市:"+ r.json()['weatherinfo']['city'],"\n温度:"+r.json()['weatherinfo']['temp'],"°\n湿度:"+r.json()['weatherinfo']['SD'])
