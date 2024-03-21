import pandas

class csv_base():
    @staticmethod
    def csv_read(file_path):
        df = pandas.read_csv(file_path)
        # print(df)
        csv_list = df.values.tolist()
        return csv_list

    '''
        file_name: csv name
        file: list data
        columns: row title  
    '''
    @staticmethod
    def csv_write_new(file_name, file, columns):
        new_df = pandas.DataFrame.from_records(file, columns=columns)
        new_df.to_csv(f'../tests/csv_files/{file_name}', index=False)



if __name__ == "__main__":
    test = csv_base()
    test.csv_read('../tests/csv_files/login.csv')
