import configparser
import os


class iniFile:
    def __init__(self):
        config_dir = os.path.join(os.path.dirname(__file__), '..', 'config')
        self.config_path = os.path.abspath(os.path.join(config_dir, 'config.ini'))


    def read_ini(self, section):
        try:
            ini_result = {}
            config = configparser.ConfigParser()
            config.read(self.config_path)

            if config.has_section(section):
                for k, v in config.items(section):
                    ini_result[k] = v
            return ini_result

        except Exception as e:
            print(f"An error occurred while reading from the ini file: {e}")
            return {}

    def write_ini(self, section, write_data):
        try:
            config = configparser.ConfigParser()
            config.read(self.config_path)

            for k, v in write_data.items():
                config[section][k] = v

            with open(self.config_path, mode='w') as configfile:
                config.write(configfile)
        except Exception as e:
            print(f"An error occurred while writing to the ini file: {e}")


    def write_ini_signup_acc(self, email, passwd, member_uuid):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        sleep(2)
        config['account']['mail'] = email
        config['account']['password'] = passwd
        config['account']['member_uuid'] = member_uuid
        with open(self.config_path, mode='w') as configfile:
            config.write(configfile)

    @staticmethod
    def read_env_ini(section, env='sit0x'):
        ini_result = {}
        config = configparser.ConfigParser()
        config.read(rf'../config/env_{env}.ini')
        ini_file = config.items(section)
        for items in ini_file:
            ini_result.setdefault(str(items[0]), str(items[1]))
        # print(ini_result)
        return ini_result


if __name__ == "__main__":
    run = iniFile()
    p = run.read_ini('account')
    # z = run.read_ini('login_account')
    # y = run.read_ini_old('account')
    print(p)
    # print(z)
    # print(y)
    run.write_ini('account', {'mail': 'test'})
