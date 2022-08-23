from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser 
# #incognito parameter passed
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })
driver = webdriver.Chrome(chrome_options=opt,executable_path="/Users/saurabhkumar/repository/interview-assistant/Bot/chromedriver")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://us04web.zoom.us/wc/join/75179179427")

inputElement = driver.find_element(By.XPATH, '//*[@id="inputname"]')
inputElement.send_keys('Saurabh Kumar')

l=driver.find_element(By.XPATH, '//*[@id="joinBtn"]')
l.click()

inputElement = driver.find_element(By.XPATH, '//*[@id="inputpasscode"]')
inputElement.send_keys('E27mYw')

l=driver.find_element(By.XPATH, '//*[@id="joinBtn"]')
l.click()

#to refresh the browser
# driver.refresh()
#to close the browser