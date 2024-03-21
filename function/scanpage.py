from basecode import Basecode
import requests
from time import sleep


class Scan_page(Basecode):
    def __init__(self, log_file_name):
        # 调用父类的初始化方法，传入日志文件名作为参数
        super().__init__(log_file_name)

    def wait_scan_finish(self):
        try:
            self.base.logger.info("Waiting for scan to finish...")  # 使用 self.base.logger 访问父类的日志记录器对象
            # customer login
            body = {
                "account": self.account_ini['mail'],
                "password": ""
            }
            headers = {
                'Content-Type': 'application/json',
                'Csrf-Token': 'test',
                'Connection': 'keep-alive'
            }
            customsign = requests.post(self.apifile['clogin'], headers=headers, json=body)
            customsign_result = customsign.json()
            self.base.logger.info(f"Customer sign API response: {customsign_result}")

            sleep(1)
            assert customsign_result['status'] == 0
            apicookie = customsign.cookies.get_dict()['ACCESS-TOKEN']

            # check scan status
            scan_status = 'pending'
            while scan_status == 'pending':
                customsign_cookies = {
                    "ACCESS-TOKEN": apicookie,
                    "CSRF-TOKEN": 'test',
                    # "Domain": ''
                }
                get_scan_status = requests.get(self.apifile['scan_status'], headers=headers, cookies=customsign_cookies)
                scan_status = str(get_scan_status.json()['data']['task_state'])
                sleep(20)  # 每20秒打一次API確認狀態

            self.base.logger.info("Scan finished successfully")
        except Exception as e:
            self.base.logger.error(f"An error occurred: {e}")
