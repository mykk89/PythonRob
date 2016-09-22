import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
import webbrowser
import requests
 
def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data
 
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
 
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

save_path = 'D:\\workspace\\zuidaima.html'
def saveFile(data):
    
    f_obj = open(save_path, 'w', encoding='UTF-8') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()
 
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
 
url_base = 'http://www.zuidaima.com/'
opener = getOpener(header)
op = opener.open(url_base)
data = op.read()
#data = ungzip(data)     # 解压
#_xsrf = getXSRF(data.decode())
 
url = url_base+'user/login.htm?redirect_url=%2F'
id = 'lzyufo@126.com'
password = 'lzyyhc'
postDict = {
       # '_xsrf':_xsrf,
        'account': id,
        'password': password,
        'rememberme': 'on'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

postSth = {
    'Content-Disposition': 'form-data',
    'name="r"': 'u4SpMlGJhG',
    'name="content"': '天气变凉了' 
    
}
#postData = urllib.parse.urlencode(postSth).encode()
url = url_base + 'mood/create.htm'
#po = opener.open(url, postData)

data=data.decode('UTF-8', 'ignore')
saveFile(data)
#webbrowser.open(save_path)

#payload = {'content':'天气变凉了'}  
r = requests.post(url, postSth)  
with open(save_path, "w") as f:  
    f.write(r.content.decode())  
print('完成')
