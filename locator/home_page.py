from selenium import webdriver
from selenium.webdriver.common.by import By

class home:

    menu_bar = (By.XPATH, '(//li/a[text()="交易資訊"])[2]')
    daily_price = (By.XPATH, '((//*[@id="mega"]/ul/li[2]/div/div/ul[1]/li[10]/a))')




