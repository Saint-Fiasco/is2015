# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://localhost:8000/accounts/login/?next=/")
    wd.find_element_by_id("id_username").click()
    wd.find_element_by_id("id_username").clear()
    wd.find_element_by_id("id_username").send_keys("admin")
    wd.find_element_by_id("id_password").click()
    wd.find_element_by_id("id_password").clear()
    wd.find_element_by_id("id_password").send_keys("admin")
    wd.find_element_by_xpath("//form[@class='form-signin']/button").click()
    wd.find_element_by_xpath("//div/div[1]/div[2]/div/div[2]/div/ul/li[1]/a").click()
    wd.find_element_by_xpath("//div/div[1]/div[2]/div/div[2]/div/ul/li[1]/ul/li[2]/a").click()
    wd.find_element_by_xpath("//div[2]/div[1]/div[2]/div/div[2]/div/ul/li[1]/a").click()
    wd.find_element_by_xpath("//div[2]/div[1]/div[2]/div/div[2]/div/ul/li[1]/ul/li[1]/a").click()
    wd.find_element_by_id("id_nombre_usuario").click()
    wd.find_element_by_id("id_nombre_usuario").clear()
    wd.find_element_by_id("id_nombre_usuario").send_keys("Nuevo Usuario2")
    wd.find_element_by_id("id_password").click()
    wd.find_element_by_id("id_password").clear()
    wd.find_element_by_id("id_password").send_keys("12345")
    wd.find_element_by_id("id_password_repeat").click()
    wd.find_element_by_id("id_password_repeat").clear()
    wd.find_element_by_id("id_password_repeat").send_keys("12345")
    wd.find_element_by_id("id_nombre").click()
    wd.find_element_by_id("id_nombre").clear()
    wd.find_element_by_id("id_nombre").send_keys("Nuevo Nombre")
    wd.find_element_by_id("id_apellido").click()
    wd.find_element_by_id("id_apellido").clear()
    wd.find_element_by_id("id_apellido").send_keys("Apellido")
    wd.find_element_by_id("id_telefono").click()
    wd.find_element_by_id("id_telefono").clear()
    wd.find_element_by_id("id_telefono").send_keys("Telefono")
    wd.find_element_by_id("id_documento").click()
    wd.find_element_by_id("id_documento").clear()
    wd.find_element_by_id("id_documento").send_keys("1234125")
    wd.find_element_by_id("id_telefono").click()
    wd.find_element_by_id("id_telefono").clear()
    wd.find_element_by_id("id_telefono").send_keys("123512")
    wd.find_element_by_xpath("//form[@id='crear']//button[.='Crear']").click()
    wd.find_element_by_xpath("//div/div[1]/div[2]/div/div[2]/div/ul/li[1]/a").click()
    wd.find_element_by_xpath("//div/div[1]/div[2]/div/div[2]/div/ul/li[1]/ul/li[2]/a").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
