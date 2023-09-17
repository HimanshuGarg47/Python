from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("file:///D:/myCode/Python/Ex_Files_Python_Automation_Testing_Upd/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
login_form = driver.find_element(By.ID, 'loginForm')
print("My login form element is:")
print(login_form)
driver.close()
