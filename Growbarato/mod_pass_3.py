from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

emailw = "hohoifumeume-5987@yopmail.com"
passw = "12345"

r = open("../pass.txt","r")
k = open("pass_verify_3.txt","w")

driver.get("https://www.growbarato.net/autenticacion?back=my-account")
time.sleep(5)
a = driver.find_element_by_xpath("//button[@class='cf2Lf6']")
a.click()
time.sleep(5)
a = driver.find_element_by_xpath("//div[@class='col-md-6']/input[@name='email']")
a.send_keys(emailw)
a = driver.find_element_by_xpath("//div[@class='col-md-6']/div[@class='input-group js-parent-focus']/input[@name='password']")
a.send_keys(passw)
a = driver.find_element_by_xpath("//footer[@class='form-footer clearfix']/button[@id='submit-login']")
a.click()
a = driver.find_element_by_xpath("//ul[@id='soy-menu-account']/li/a[@id='identity-link']")
a.click()
for linea in r:
    time.sleep(5)
    a = driver.find_element_by_xpath("//input[@name='password']")
    a.send_keys(passw)
    a = driver.find_element_by_xpath("//input[@name='new_password']")
    a.send_keys(linea)
    a = driver.find_element_by_xpath("//button[@class='btn btn-primary form-control-submit float-xs-right']")
    a.click()
    try:
        b = driver.find_element_by_xpath("//article[@class='alert alert-success']/ul/li")
        passw = linea
        k.write(linea.rstrip("\n")+" | FUNCIONA\n")
        next
    except:
        k.write(linea.rstrip("\n")+" | NO FUNCIONA\n")
    
r.close()
k.close()