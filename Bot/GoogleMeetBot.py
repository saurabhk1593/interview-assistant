from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
c = webdriver.ChromeOptions()
c.add_argument('--profile-directory=MyProfile')
c.add_argument("user-data-dir=/Users/saurabhkumar/Library/Application\ Support/Google/Chrome/Default") 
# #incognito parameter passed
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options = c)
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("http://meet.google.com/ybk-xjjg-zen")
#to refresh the browser
driver.refresh()
#to close the browser


