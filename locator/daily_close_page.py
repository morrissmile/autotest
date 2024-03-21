from selenium import webdriver
from selenium.webdriver.common.by import By

class DailyClosePrice:

    select_month = (By.XPATH, '//select[@name="mm"]')
    input_stock = (By.XPATH, '//input[@name="stockNo"]')
    search_btn = (By.XPATH, '//button[@class="search"]')