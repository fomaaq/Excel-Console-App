'''
TODO
'''


def parse_arguments(args_list):
    order_path = None
    price_list_path = None
    file_name = None

    for args in args_list:
        if 'order_path=' in args:
            order_path = args.split('=')[-1]

        if 'price_list_path=' in args:
            price_list_path = args.split('=')[-1]

        if 'price_list_path=' in args:
            file_name = args.split('=')[-1]

    return order_path, price_list_path, file_name
