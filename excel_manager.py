'''
A module containing methods for working with excel files
'''
import os
import pandas as pd


def check_file_exist(file_path: str):
    '''
    Checks the existence of the file
    '''
    return os.path.exists(file_path)


def check_save_path_exist(file_name: str):
    '''
    Checks whether the invoice file with the entered name can be saved
    '''
    if check_file_exist(file_path=file_name):
        print(f'A file named {file_name} already exists, enter another file name to save')
        exit()


def open_excel(path: str):
    '''
    Opens the Excel file by the entered path and returns it as a data frame,
    prints an error message if it does not find the file by the entered path
    '''
    try:
        dataframe = pd.read_excel(io=path)
        return dataframe

    except FileNotFoundError:
        print(f'The data file was not found: {path}\nCheck that the file exists and the path to it')
        exit()


def check_price_columns(price_data):
    '''
    Checks the match of the columns in the price list file with the sample,
    printed an error message if a mismatch
    '''
    sample_price_columns = {'Part no.', 'Price, EUR'}
    price_columns = set(list(price_data.columns))

    if price_columns >= sample_price_columns:
        print('The price list matches the sample')
        pass
    else:
        print('The price list file does not match the sample')
        exit()


def check_order_columns(order_data):
    '''
    Checks the match of the columns in the order file with the sample,
    printed an error message if a mismatch
    '''
    sample_order_columns = {'Part no.',
                            'Description',
                            'Price, EUR',
                            'Total amount, EUR',
                            'Ordered quantity (pcs)'}
    order_columns = set(list(order_data.columns))

    if order_columns >= sample_order_columns:
        print('The order matches the sample')
        pass
    else:
        print('The order file does not match the sample')
        exit()


def save_excel(data, file_name: str):
    '''
    Saves the invoice file by the entered path
    '''
    data.to_excel(excel_writer=file_name, index=False)


def check_file_saved(file_name: str):
    '''
    Checks whether the invoice file is saved and prints a message about the successful saving of the file,
    or prints an error message
    '''
    if check_file_exist(file_name):
        print(f'File "{file_name}" saved')
    else:
        print('Unable to save file')
        exit()
