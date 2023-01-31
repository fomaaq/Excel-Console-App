import excel_manager
import pandas as pd


def create_invoice(order_path: str, price_data):

    order_data = excel_manager.open_excel(path=order_path)

    excel_manager.check_order_columns(order_data=order_data)

    invoice_data = order_data[['Part no.',
                               'Description',
                               'Ordered quantity (pcs)',
                               'Price, EUR',
                               'Total amount, EUR']]

    invoice_data = pd.merge(invoice_data, price_data, on='Part no.', how='inner')

    invoice_data['Price, EUR_x'] = invoice_data['Price, EUR_y']

    invoice_data = invoice_data.drop('Price, EUR_y', axis='columns')

    invoice_data = invoice_data.rename(columns={'Price, EUR_x': 'Price, EUR'})

    invoice_data['Total amount, EUR'] = invoice_data['Ordered quantity (pcs)'] * invoice_data['Price, EUR']

    print('Invoice data has been created')

    return invoice_data
