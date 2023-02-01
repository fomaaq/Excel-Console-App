'''
A console application that converts an order file into an invoice file
with prices obtained from a price list file
'''
import sys
import arguments_parser
import order_converter

# Start of the console program
if __name__ == '__main__':

    # Getting a list of arguments entered in the console
    args = sys.argv

    # Getting the path to the order and price list files and the name of the invoice file to be saved
    order_path, price_list_path, file_name = arguments_parser.parse_arguments(args_list=args)

    # Checking the indication of required arguments
    if order_path is None:
        print('The path to the order file is not entered')
        exit()

    if price_list_path is None:
        print('The path to the price list file is not entered')
        exit()

    if file_name is None:
        print('The name of the saved invoice file is not entered')
        exit()

    # Converting a file
    order_converter.convert_order_to_invoice(order_path=order_path,
                                             price_list_path=price_list_path,
                                             file_name=file_name)
