import excel_manager


def format_price(price_list_path: str):

    price_data = excel_manager.open_excel(price_list_path)

    excel_manager.check_price_columns(price_data=price_data)

    price_data['Part no.'] = price_data['Part no.'].map(map_remove_spaces)

    print('The price list is formatted')
    return price_data


def map_remove_spaces(item):
    return item.replace(' ', '')
