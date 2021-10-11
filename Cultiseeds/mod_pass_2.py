from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
emailw = "presaneuffapa-3072@yopmail.com"
passw = "¥aaaAAA123@"
n_pass = "123aaaAAA@@@"
r = open("../pass.txt","r")
k = open("pass_verify.txt","w+")
driver.get("https://cultiseeds.cl/mi-cuenta/")

a = driver.find_element_by_xpath("//input[@id='username']")
a.send_keys(emailw)
a = driver.find_element_by_xpath("//input[@id='password']")
a.send_keys(passw)
a = driver.find_element_by_xpath("//button[@class='woocommerce-button button woocommerce-form-login__submit']")
a.click()
a = driver.find_element_by_xpath("//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--edit-account']/a")
a.click()
for linea in r:
    a = driver.find_element_by_xpath("//li[@id='menu-item-4100']/a")
    a.click() 
    a = driver.find_element_by_xpath("//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--edit-account']/a")
    a.click()
    a = driver.find_element_by_xpath("//input[@id='password_current']")
    a.send_keys(passw)
    a = driver.find_element_by_xpath("//input[@id='password_1']")
    a.send_keys(linea)
    a = driver.find_element_by_xpath("//input[@id='password_2']")
    a.send_keys(linea)
    a = driver.find_element_by_xpath("//button[@class='woocommerce-Button button']")
    a.click()
    try:
        b = driver.find_element_by_xpath("//div[@class='woocommerce-message']") #se registra
        k.write(linea.rstrip("\n")+" | FUNCIONA\n")
        passw = linea
        time.sleep(3)
        next
    except:
        try:
            b = driver.find_element_by_xpath("//ul[@class='woocommerce-error']") #No se registra
            k.write(linea.rstrip("\n")+" | NO FUNCIONA\n")
            next
        except:
            print("Error")
r.close()
k.close()

