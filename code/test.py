import pytest
from requests import request
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



def test_a():
    assert 1==1
#连通测试百度，返回状态码200    
def test_baidu():
    resp=request(method="get",url="https://www.baidu.com")
    print(resp)
    assert resp.status_code==200
#天气接口api测试，获取json返回信息   
def test_weatherapi():
    payload = {'area': '南京' }

    encoded_payload = urllib.parse.urlencode(payload)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp=request(method='post',url='https://route.showapi.com/9-2?appKey=D19e65a0e7124CaCa34d5d2087AeA6dB',data=encoded_payload,headers=headers)
    city=resp.json()['showapi_res_body']['f1']
    print(f'南京{time.localtime()[1]}月{time.localtime()[2]}日{city['night_air_temperature']}到{city['day_air_temperature']}℃ {city['day_weather']}转{city['night_weather']}')
    assert resp.json()['showapi_res_code']==0
    assert resp.json()['showapi_res_body']['cityInfo']['c5']=='南京'
#webdriver配置
@pytest.fixture
def setup_driver():
    chromedriver_path = r"C:\Users\npcleishen2\.wdm\drivers\chromedriver\win64\138.0.7204.168\chromedriver-win32\chromedriver.exe"
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()
    yield driver
    driver.quit()

#切换窗口句柄测试
def test_newpage(setup_driver):
    driver = setup_driver
    index = r"https://47f4201c.r2.cpolar.top"
    driver.get(index)
    time.sleep(5)
    current_window = driver.current_window_handle
    luma_page = driver.find_element(By.XPATH, '//*[@id="luma-test-link"]pip')
    luma_page.click()
    for handle in driver.window_handles:
        if handle!= current_window:
            driver.switch_to.window(handle)
            break
    assert driver.current_url == 'https://magento.softwaretestingboard.com/'

#测试正确密码
def test_truepwd(setup_driver):
    driver = setup_driver
    index = r"https://47f4201c.r2.cpolar.top"
    driver.get(index)
    time.sleep(5)
    search_box = driver.find_element(By.XPATH, '//*[@id="homePassword"]')
    search_box.send_keys('morohikosei')
    driver.find_element(By.XPATH, '//*[@id="unlockHome"]').click()
    image_element = driver.find_element(By.XPATH, '//*[@id="homeImageContainer"]/img')
    assert image_element.is_displayed()

    
"""
#page object model
class Basepage:
    def __init__(self,url):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
    
    def quit(self):
        self.driver.quit()
     
    def find(self,by,value):
        try:
            wait = WebDriverWait(self.driver, 10)
            self.element = wait.until(EC.presence_of_element_located((by, value)))
            return self.element
        except Exception as e:
            print(f"查找元素异常{e}")
            return None
    def send(self,keys):
            if self.element:
                self.element.send_keys(keys)
                self.element.send_keys(Keys.ENTER)
"""
        
        

if __name__=="__main__":
    pytest.main(["-sv","E:/jupyter/test.py"])        
        