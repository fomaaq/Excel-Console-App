'''
The main module that contains methods that convert an order into an invoice
'''
import excel_manager
import price_formatter
import invoice_creator


def convert_order_to_invoice(order_path: str, price_list_path: str, file_name: str):
    '''
    Converts order and invoice
    '''
    # Checks whether the invoice file with the entered name can be saved
    excel_manager.check_save_path_exist(file_name=file_name)

    # Initializes the price data
    price_data = price_formatter.format_price(price_list_path=price_list_path)

    # Initialize the invoice data
    invoice_data = invoice_creator.create_invoice_data(order_path=order_path,
                                                       price_data=price_data)

    # Saves the invoice file
    excel_manager.save_excel(data=invoice_data, file_name=file_name)

    # Checks whether the invoice file is saved
    excel_manager.check_file_saved(file_name=file_name)
