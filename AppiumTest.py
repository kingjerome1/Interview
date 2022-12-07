# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "12"
caps["appium:deviceName"] = "ROG Phone 5"
caps["appium:appPackage"] = "com.asus.calculator"
caps["appium:udid"] = "M9AIKN019611WNM"
caps["appium:appActivity"] = "com.asus.calculator.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
try:
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.save_screenshot('test_01.png')
    driver.findElement(By.id("00000000-0000-0173-0000-2b1600000159")) #卡片介紹
    driver.findElement(By.id("00000000-0000-0173-0000-2b1700000159")) #刷卡優惠
    driver.findElement(By.id("00000000-0000-0173-0000-2b1800000159")) #小數點(信用卡)
    driver.findElement(By.id("00000000-0000-0173-0000-2b1900000159")) #卡友登錄專區
    driver.findElement(By.id("00000000-0000-0173-0000-2b1a00000159")) #卡友理財服務
    driver.findElement(By.id("00000000-0000-0173-0000-2b1b00000159")) #卡友權益
    driver.findElement(By.id("00000000-0000-0173-0000-2b1c00000159")) #行動支付
    driver.findElement(By.id("00000000-0000-0173-0000-2b1d00000159")) #申請信用卡
    #信用卡下方共16個元素 8個android.view.View 8個android.widget.TextView
    driver.quit()

except Exception:
    print('Something wrong')
finally:
    print('第二題結束')  


#進入停發卡頁面後使用keyevent查找卡片數量
def check_cardcounts():
    for i in range(8):
        driver.keyevent(61) #Tab鍵
        driver.keyevent(66) #Enter鍵

try:
    check_cardcounts()
except Exception:
    print(Exception + "check_cardcounts()出錯")
finally:
    print('第三題結束')  