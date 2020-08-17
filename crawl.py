import requests
import json
url = 'https://fund.megabank.com.tw/ETFData/djjson/ETNEWSjson.djjson?a=1&P1=mega&P2=&P3=true&P4=false&P5=false'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
res = requests.get(url=url, headers=headers, verify=False)
con = res.text
con_list = json.loads(con)['ResultSet']['Result']
print('日期\t   標題')
for item in con_list:
    date = item['V1']
    title = item['V2']
    print(date, title)