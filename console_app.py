import pandas as pd


def excel_rework(in_data, price_data):
    in_data = pd.read_excel(io='data/in.xlsx')
    price_data = pd.read_excel(io='data/price.xlsx')

    format_price_data = price_data.copy()

    def map_remove_spaces(item):
        return item.replace(' ', '')

    format_price_data['Part no.'] = format_price_data['Part no.'].map(map_remove_spaces)

    out_data = in_data[['Part no.', 'Description', 'Ordered quantity (pcs)', 'Price, EUR', 'Total amount, EUR']]

    out_data = pd.merge(out_data, format_price_data, on='Part no.', how='inner')

    out_data['Price, EUR_x'] = out_data['Price, EUR_y']

    out_data = out_data.drop('Price, EUR_y', axis='columns')

    out_data = out_data.rename(columns={'Price, EUR_x': 'Price, EUR'})

    out_data['Total amount, EUR'] = out_data['Ordered quantity (pcs)'] * out_data['Price, EUR']

    out_data.to_excel(excel_writer='data/out.xlsx', index=False)


excel_rework()
