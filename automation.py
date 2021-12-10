# from selenium import webdriver
from selenium import webdriver
chrome_browser = webdriver.Chrome()
# by default it searches the driver file in the path of Windows folder in the C drive

# print(chrome_browser)
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# print('Selenium Easy Demo' in chrome_browser.title)
# # we are checking here whether we are on the same page or not, if yes, it will return true

assert 'Selenium Easy Demo' in chrome_browser.title
# # if the above is not true, assert will error out, otherwise code will continue

show_message_button = chrome_browser.find_element_by_class_name("btn-default")
# the above command basically grabs this
# <button type="button" onclick="showInput();" class="btn btn-default">Show Message</button>

# we can find that button by CSS selector as well, using the below command
# show_message_button = chrome_browser.find_element_by_css_selector('#get-input > .btn')


# print(button_text)
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()    # to clear any previous message
user_message.send_keys("Hello there!")     # selenium is typing the message

show_message_button.click()     # selenium is clicking the button

output_message = chrome_browser.find_element_by_id('display')

print('Hello there!' in output_message.text)
print(output_message.get_attribute('innerHTML'))

assert 'Hello there!' in output_message.text

chrome_browser.close()
# chrome_browser.quit()    # or we can use this

'''
sometimes the .close() , or .quit() method doesn't work. Because of some backgroud updates, etc. 
and each .close() closes one instance only. so in case more than 1 instance of the browser is opened by the 
program, we need to p
ass multiple .close()

many websites identify the use of selenium and blocks the activity. "Verify you are not a robot" checkbox.
so there is a way around that, we use 'Waits' so do things slowly, so the server thinks that this is being 
done by a human.
'''



# @gfg_decorator
# def hello_decorator():
#     print("Gfg")

# '''Above code is equivalent to -

# def hello_decorator():
#     print("Gfg")
    
# hello_decorator = gfg_decorator(hello_decorator)'''
















# # importing libraries
# import time
# import math

# # decorator to calculate duration
# # taken by any function.
# def calculate_time(func):
	
# 	# added arguments inside the inner1,
# 	# if function takes any arguments,
# 	# can be added like this.
# 	def inner1(*args, **kwargs):

# 		# storing time before function execution
# 		begin = time.time()
		
# 		func(*args, **kwargs)

# 		# storing time after function execution
# 		end = time.time()
# 		print("Total time taken in : ", func.__name__, end - begin)

# 	return inner1



# # this can be added to any function present,
# # in this case to calculate a factorial
# @calculate_time
# def factorial(num):

# 	# sleep 2 seconds because it takes very less time
# 	# so that you can see the actual difference
# 	time.sleep(2)
# 	print(math.factorial(num))

# # calling the function.
# factorial(10)











# # Python program to illustrate functions
# # can be treated as objects
# def shout(text):
# 	return text.upper()

# print(shout('Hello'))

# yell = shout

# print(yell('Hello'))

