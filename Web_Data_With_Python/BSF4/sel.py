import time
from selenium import webdriver

browser = webdriver.Chrome("D:/Downloads/chromedriver_win32/chromedriver.exe")
browser.get('https://physicswallah.live/login')


username_elem  = browser.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-auth-new/ion-content/article/ion-row/ion-col/section/ion-row/ion-col[2]/section/app-login/div/ion-grid/ion-row/ion-col/section/ion-row/ion-col[2]/ion-item/ion-row/ion-col[3]/ion-input/input')
username_elem.send_keys(8437389759)
get_otp = browser.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-auth-new/ion-content/article/ion-row/ion-col/section/ion-row/ion-col[2]/section/app-login/div/ion-grid/ion-row/ion-col/section/ion-row/ion-col[5]/ion-row/ion-col/ion-button')
get_otp.click() 

time.sleep(5)
password_elem = browser.find_element_by_xpath('//*[@id="ngx-otp-input-0"]')
time.sleep(3)
password_elem.send_keys(373667)
login_elem = browser.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-auth-new/ion-content/article/ion-row/ion-col/section/ion-row/ion-col[2]/section/app-otp/div/ion-grid/ion-row/ion-col/section[1]/ion-row/ion-col[5]/ion-row/ion-col/ion-button//button')
login_elem.click()

time.sleep(3)
home_elem = browser.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-menu/ion-content/section/ion-menu-toggle/ion-item[1]')
home_elem.click()


