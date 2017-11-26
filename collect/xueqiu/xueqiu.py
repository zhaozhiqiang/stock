import urllib2


#url = 'https://xueqiu.com/S/SH600036'
url = 'https://xueqiu.com/v4/stock/quote.json?code=SH600036'
send_header = {
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           #'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2',
           'Cache-Control' : 'max-age=0',
           'Connection':'keep-alive',
           'Cookie': 's=g312npdpfq; device_id=789636086b06c210f1795379b516deaa; aliyungf_tc=AQAAAM8TVhc36QQAFjOetFFpOsjeShxE; xq_a_token=e3cae829e5836e234be00887406080b41c2cb69a; xq_a_token.sig=RqWjdP5W4mGqE-dvLBb-hqr3kNQ; xq_r_token=319673aba44e00bd0fed3702652be32b2349860e; xq_r_token.sig=J6CRpJiOVJCLsdVRN6tCvexELgw; u=651508853296157; Hm_lvt_1db88642e346389874251b5a1eded6e3=1507047447,1508853298; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1508854381; __utma=1.1326865660.1507047444.1507047444.1508854338.2; __utmc=1; __utmz=1.1507047444.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
           'DNT' : '1',
           'Host' : 'xueqiu.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
req = urllib2.Request(url, headers = send_header)
response = urllib2.urlopen(req)
html = response.read()
print(html)
#with open ('sh600036.html', 'w') as f:
#    f.write(html)