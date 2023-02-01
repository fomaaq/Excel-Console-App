'''
The module contains methods for creating an invoice data
'''

import excel_manager
import pandas as pd


def create_invoice_data(order_path: str, price_data):
    '''
    Creates invoice data from the order and price list, returns it and prints a message
    '''
    order_data = excel_manager.open_excel(path=order_path)

    # Checks if the order matches the sample
    excel_manager.check_order_columns(order_data=order_data)

    # Creates invoice data
    invoice_data = order_data[['Part no.',
                               'Description',
                               'Ordered quantity (pcs)',
                               'Price, EUR',
                               'Total amount, EUR']]

    # Fills in unit prices in the invoice data
    invoice_data = pd.merge(invoice_data, price_data, on='Part no.', how='inner')
    invoice_data['Price, EUR_x'] = invoice_data['Price, EUR_y']

    # Prepares the invoice data for saving in the required format
    invoice_data = invoice_data.drop('Price, EUR_y', axis='columns')
    invoice_data = invoice_data.rename(columns={'Price, EUR_x': 'Price, EUR'})
    invoice_data['Total amount, EUR'] = invoice_data['Ordered quantity (pcs)'] * invoice_data['Price, EUR']

    print('Invoice data has been created')
    return invoice_data
