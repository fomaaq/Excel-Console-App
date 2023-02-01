'''
A console application that converts an order file into an invoice file
with prices obtained from a price list file
'''
import sys
import src.app_utils.arguments_parser as arguments_parser
import src.app_utils.app_interrupter as app_interrupter
import src.order_converter as order_converter

# Start of the console program
if __name__ == '__main__':

    # Getting a list of arguments entered in the console
    args = sys.argv

    # Getting the path to the order and price list files and the name of the invoice file to be saved
    order_path, price_list_path, file_name = arguments_parser.parse_arguments(args_list=args)

    # Checking the indication of required arguments
    if order_path is None:
        app_interrupter.interrupt_app(error_message='The path to the order file is not entered',
                                      exit_code=10001)

    if price_list_path is None:
        app_interrupter.interrupt_app(error_message='The path to the price list file is not entered',
                                      exit_code=10002)

    if file_name is None:
        app_interrupter.interrupt_app(error_message='The name of the saved invoice file is not entered',
                                      exit_code=10003)

    # Converting a file
    order_converter.convert_order_to_invoice(order_path=order_path,
                                             price_list_path=price_list_path,
                                             file_name=file_name)
