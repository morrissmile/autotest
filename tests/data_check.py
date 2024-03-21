'''CSV data validation'''

from common_method.csv_method import csv_base as csv

def data_validation():
    lists = csv.csv_read(file_path='./csv_files/login.csv')
    # print(lists)
    new_lists = []

    for row in lists:
        if row[3] >= 0 and row[3] <= 10000:
            if str(row[1]).startswith('886'):
                new_lists.append(row)

    columns = ["uid", "phone_number", "user_type", "login_count"]
    csv.csv_write_new(file_name='new_login.csv', file=new_lists, columns=columns)


if __name__ == "__main__":
    data_validation()