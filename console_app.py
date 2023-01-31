import sys
import arguments_parser
import order_converter


if __name__ == '__main__':
    args = sys.argv
    order_path, price_list_path, file_name = arguments_parser.parse_arguments(args_list=args)

    if order_path is None:
        print("TODO ... ERROR")
        exit()

    if price_list_path is None:
        print("TODO ... ERROR")
        exit()

    if file_name is None:
        print("TODO ... ERROR")
        exit()

    order_converter.convert_order_to_invoice(order_path=order_path,
                                             price_list_path=price_list_path,
                                             file_name=file_name)
