import os
import logging

class Logger:
    def __init__(self, log_file):
        log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'log_files'))
        log_path = os.path.join(log_dir, log_file)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
