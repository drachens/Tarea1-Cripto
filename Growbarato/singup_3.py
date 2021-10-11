from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
def pass2048(repeticiones):
    r = open("../generate.txt","r")
    for linea in r:
        passw = linea.strip("\n")    
    passw = passw*repeticiones
    return passw
passw = pass2048(15)
emailw="fabefefroko-9434@yopmail.com"
driver.get("https://www.growbarato.net/autenticacion?back=my-account")
time.sleep(10)
a = driver.find_element_by_xpath("//span[@class='cf1y60']")
a.click()
time.sleep(10)
a = driver.find_element_by_xpath("//div[@class='form-group']/div/input[@name='email']")
a.send_keys(emailw)
a = driver.find_element_by_xpath("//footer[@class='form-footer clearfix']/input[@class='btn btn-primary']")
a.click()
a = driver.find_element_by_xpath("//input[@name='firstname']")
a.send_keys("TestName")
a = driver.find_element_by_xpath("//input[@name='lastname']")
a.send_keys("TestLastName")
a = driver.find_element_by_xpath("//input[@name='password']")
a.send_keys(passw)
a = driver.find_element_by_xpath("//button[@class='btn btn-primary form-control-submit float-xs-right']")
a.click()
try:
    a = driver.find_element_by_xpath("//input[@name='password']")
    print("No se pudo utilizar esa contraseña de largo: "+str(len(passw)))
except:
    print("Contraseña de largo: "+str(len(passw))+" funciona")
    