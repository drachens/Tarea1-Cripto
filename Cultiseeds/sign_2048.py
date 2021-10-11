from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
r = open(",,/generate.txt","r")
for linea in r:
    passw = linea.strip("\n")    
emailw="jetilunnumma-7859@yopmail.com"
driver.get("https://cultiseeds.cl/mi-cuenta/")

a = driver.find_element_by_xpath("//input[@id='reg_email']")
a.send_keys(emailw)
a = driver.find_element_by_xpath("//input[@id='reg_password']")
a.send_keys(passw)
a = driver.find_element_by_xpath("//button[@class='woocommerce-Button woocommerce-button button woocommerce-form-register__submit']")
a.click()