'''
The module contains methods responsible for parsing arguments passed to the console
'''


def parse_arguments(args_list: list):
    '''
    Parses the arguments entered into the console and returns them
    '''
    order_path = None
    price_list_path = None
    file_name = None

    for args in args_list:
        if 'order_path=' in args:
            order_path = args.split('=')[-1]
            # TODO

        if 'price_list_path=' in args:
            price_list_path = args.split('=')[-1]
            # TODO

        if 'file_name=' in args:
            file_name = args.split('=')[-1]
            # TODO

    return order_path, price_list_path, file_name
