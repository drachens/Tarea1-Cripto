from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

r = open("../generate.txt","r")
for linea in r:
    passw = linea   
passw = passw[0:100]
emailw = "fabefefroko-9434@yopmail.com"

driver.get("https://www.growbarato.net/autenticacion?back=my-account")
time.sleep(5)
a = driver.find_element_by_xpath("//button[@class='cf2Lf6']")
a.click()
for i in range(100,0,-1):
    passw = passw[0:i]
    time.sleep(5)
    a = driver.find_element_by_xpath("//div[@class='col-md-6']/input[@name='email']")
    a.clear()
    a.send_keys(emailw)
    a = driver.find_element_by_xpath("//div[@class='input-group js-parent-focus']/input[@name='password']")
    a.send_keys(passw)
    a = driver.find_element_by_xpath("//footer[@class='form-footer clearfix']/button[@id='submit-login']")
    a.click()
    time.sleep(3)    
    try:
        b = driver.find_element_by_xpath("//a[@id='identity-link']")
        print("Caracteres de contraseña guardados: "+str(len(passw)))
        break
    except:
        next  
driver.close()