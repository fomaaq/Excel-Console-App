import price_formatter
import invoice_creator
import excel_manager


def convert_order_to_invoice(order_path, price_list_path, file_name):
    price_data = price_formatter.format_price(price_list_path=price_list_path)

    invoice_data = invoice_creator.create_invoice(order_path=order_path,
                                                  price_data=price_data)

    excel_manager.save_excel(data=invoice_data, file_name=file_name)
