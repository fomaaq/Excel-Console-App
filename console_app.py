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
                                      exit_code=10002)

    # Converting a file
    order_converter.convert_order_to_invoice(order_path=order_path,
                                             price_list_path=price_list_path,
                                             file_name=file_name)

# exit_moments:
    # 1. excel_manager exit:
    #   1.1. file_exist exit:
    #       1) excel_manager.check_save_path_exist: если файл с именем, равным file_name уже существует
    #       2) excel_manager.check_file_saved: если сохраненный файл не существует
    #   1.2 1) excel_manager.open_excel: если не может открыть файл, т.к. не находит его
    #   1.3. check_columns exit:
    #       1) excel_manager.check_price_columns: если столбцы прайса не сходятся с образцом
    #       2) excel_manager.check_order_columns: если столбцы заказа не сходятся с образцом
    # 2. arguments exit
    #   1) console_app: если order_path is None
    #   2) console_app: если price_list_path is None
    #   3) console_app: если file_name is None
