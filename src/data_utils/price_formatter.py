'''
The module contains methods for preparing price list data to be combined with invoice data
'''
import src.data_utils.excel_manager as excel_manager


def format_price(price_list_path: str):
    '''
    Formats the price list data to merge with the invoice data,
    returns the price data and prints a message
    '''
    # Opens the price list file
    price_data = excel_manager.open_excel(price_list_path)

    # Checks if the price list matches the sample
    excel_manager.check_price_columns(price_data=price_data)

    # Formats the price list for merging
    price_data['Part no.'] = price_data['Part no.'].map(remove_spaces)

    print('The price list is formatted')
    return price_data


def remove_spaces(item):
    '''
    Removes spaces from item and return it
    '''
    return item.replace(' ', '')
