from selenium import webdriver
# from selenium.webdriver.common.by import By
from locator.home_page import home
from locator.daily_close_page import DailyClosePrice
from common_method.log import Logger
from common_method.date import Datetimes


class Basecode:
    def __init__(self):
        # get time function
        # time = Datetimes.timestamp()
        log_time = Datetimes.datetime_log()

        # logger name and create logger class
        # get logger instance
        logger_instance = Logger(f"{log_time}.log")
        self.logger = logger_instance.get_logger()

        # locator
        self.home_page = home()
        self.daily_close_page = DailyClosePrice()

        # setup driver
        self.driver = webdriver.Chrome(executable_path='../chromedriver')

        # 其他初始化操作
        # base = Base()
        # self.time = base.timestamp()
        # self.checkout_time = base.datetime_checkout()
        # self.signup_account_ini = base.read_ini('account')
        # self.login_account_ini = base.read_ini('login_account')
        # self.adid = base.read_ini('adid')
        # self.test_env_ini = base.read_ini('testenv')
        # self.server_site = base.read_ini('server')
        # self.base = base


