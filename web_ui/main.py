from time import sleep
from selenium.webdriver.support.ui import Select
from common_method.basecode import Basecode
from selenium import webdriver


class get_stock_info(Basecode):
    def __init__(self):
        # 调用父类的初始化方法，不再需要传入日志文件名作为参数
        super().__init__()

    def get_daily_close_price(self):
        try:
            self.driver.maximize_window()

            self.driver.get('https://www.twse.com.tw/zh/')
            sleep(3)
            self.logger.info("Scan finished successfully")

            # print(path.elementpath.menu_bar)
            self.driver.find_element(*path.elementpath.menu_bar).click()
            # sleep(3)
            # self.driver.find_element(*path.elementpath.daily_price).click()
            # sleep(3)
            # select_month_element = driver.find_element(*path.elementpath.select_month)
            # select = Select(select_month_element)
            # select.select_by_value("1"
            # self.driver.find_element(*path.elementpath.input_stock).send_keys('2330')
            # sleep(3)
            # self.driver.find_element(*path.elementpath.search_btn).click()
            # sleep(3)
            #
            # driver.get_screenshot_as_file(rf'./2330.png')
            #
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    run = get_stock_info()
    run.get_daily_close_price()
