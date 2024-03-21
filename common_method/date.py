import datetime


class Datetimes:

    @staticmethod
    def timestamp() -> str:
        datetime_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return datetime_str
    # get today time format yyyy-mm-dd-hh-MM-SS

    @staticmethod
    def timestamp_day() -> str:
        datetime_str = datetime.datetime.now().strftime('%m%d')
        return datetime_str
    # get today time format yyyy-mm

    @staticmethod
    def datetime_checkout() -> str:
        datetime_go_back_date = datetime.datetime.now().strftime('%Y-%m-%d')
        return datetime_go_back_date
    # get today time format yyyy-mm-dd

    @staticmethod
    def datetime_log() -> str:
        datetime_log = datetime.datetime.now().strftime('%Y-%m-%d-%H')
        return datetime_log
    # get today time format yyyy-mm-dd -HH

    @staticmethod
    def date_period_format(dates: str, delta_days: int) -> str:
        date_format = datetime.datetime.strptime(str(dates), '%Y-%m-%d')
        current_date = date_format - datetime.timedelta(days=delta_days)
        current_date_format = current_date.strftime('%Y-%m-%d')
        return current_date_format
    '''Format a date that is a certain number of days before the start date.

    Args:
        dates (str): The start date in the format '%Y-%m-%d'.
        delta_days (int): The number of days before the start date.

    Returns:
        str: The formatted date.
    '''


if __name__ == "__main__":
    run = Datetimes()
    p = run.date_period_format('2024-01-30', 1)
    y = run.timestamp()
    print(p)
    print(y)
