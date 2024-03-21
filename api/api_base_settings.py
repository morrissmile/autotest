from code_function.basecode import Basecode


# from common.common_code import *
class Api_Key_Token(Basecode):

    def __init__(self):
        serversite = self.server_site['server_site']
        serverlist = ['00', '01', '02', '03', '04', '05', '07', '08', '13', '14', '35', '42', '201', '202', '203',
                      '205', '206', '207', '208', '209', '210', '211', '09']
        if self.test_env_ini['env'] == 'stage':
            # b2c server token
            self.sit_x_auth_token = ''
            self.b2c_server_url = 'https://'
            self.remote_config_manual_key = 'remote_config_manual_key'
            self.mkt_server_url = 'https://'
            # mkt server token key in header
            self.mkt_user_uuid = ''

        else:
            if serversite in serverlist:
                self.sit_x_auth_token = ''
                self.sit_promo_x_auth_token = ''
                self.b2c_server_url = f'https://api-b2c-{serversite}.com'
                self.remote_config_manual_key = 'remote_config_manual_key'
                self.mkt_server_url = f'https://api-mkt-{serversite}.com'
                # mkt server token key in header
                self.mkt_user_uuid = ''
            else:
                print(f'serversite should be {serverlist}')
                raise
