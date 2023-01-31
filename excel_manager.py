import pandas as pd


def open_excel(path: str):
    try:
        dataframe = pd.read_excel(io=path)
        return dataframe

    except FileNotFoundError:
        print(f'The data file was not found: {path}\nCheck that the file exists and the path to it')
        exit()


def check_price_columns(price_data):
    sample_price_columns = {'Part no.', 'Price, EUR'}
    price_columns = set(list(price_data.columns))

    if price_columns == sample_price_columns:
        print('The price list matches the sample')
        pass
    else:
        print('The price list file does not match the sample')
        exit()


def check_order_columns(order_data):
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
    data.to_excel(excel_writer=file_name, index=False)
    print(f'File "{file_name}" saved')
