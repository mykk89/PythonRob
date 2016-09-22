# coding = utf-8
from selenium import webdriver
import time

save_path = 'D:\\workspace\\zuidaima.html'
def saveFile(data):
    
    f_obj = open(save_path, 'w', encoding='UTF-8') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()
    
browser = webdriver.PhantomJS(executable_path='C:\\Users\\Edward\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.5\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
browser.get("http://www.zuidaima.com/user/login.htm?redirect_url=%2F")

browser.find_element_by_id("account").send_keys("lzyufo@126.com")
browser.find_element_by_id("password").send_keys("lzyyhc")
browser.find_element_by_id("login").click()
time.sleep(3)
browser.find_element_by_id("mood_input").send_keys("下午气温很舒服，适合写代码")
browser.find_element_by_id("mood_publish").click()
html = browser.execute_script("return document.documentElement.outerHTML")

saveFile(html)
