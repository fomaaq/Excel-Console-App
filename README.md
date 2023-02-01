# excel_console_app
This is a console application that uses the Pandas library to convert an order file into an invoice file using prices from a price list file.

-- --

## App structure

- [console_app.py](https://github.com/fomaaq/excel_console_app/blob/main/console_app.py) -- the main file of app that runs it
- [src/](https://github.com/fomaaq/excel_console_app/tree/main/src) -- contains the main app module and a folders with utils:
- - [src/order_converter.py](https://github.com/fomaaq/excel_console_app/blob/main/src/order_converter.py) -- the main app module that contains methods that convert an order into an invoice
- [src/app_utils/](https://github.com/fomaaq/excel_console_app/tree/main/src/app_utils) -- contains app utils:
- - [src/app_utils/app_interrupter.py](https://github.com/fomaaq/excel_console_app/blob/main/src/app_utils/app_interrupter.py) -- contains a method for printing an error message and interrupting the app
- - [src/app_utils/arguments_parser.py](https://github.com/fomaaq/excel_console_app/blob/main/src/app_utils/arguments_parser.py) -- contains methods responsible for parsing arguments passed to the console
- [src/data_utils/](https://github.com/fomaaq/excel_console_app/tree/main/src/data_utils) -- contains data utils:
- - [src/data_utils/excel_manager.py](https://github.com/fomaaq/excel_console_app/blob/main/src/data_utils/excel_manager.py) -- contains methods for working with excel files
- - [src/data_utils/invoice_creator.py](https://github.com/fomaaq/excel_console_app/blob/main/src/data_utils/invoice_creator.py) -- contains methods for creating an invoice data
- - [src/data_utils/price_formatter.py](https://github.com/fomaaq/excel_console_app/blob/main/src/data_utils/price_formatter.py) -- contains methods for preparing price list data to be combined with invoice data
- [data/](https://github.com/fomaaq/excel_console_app/tree/main/data) -- contains excel files of the order and price list, which are samples and on which the app was launched
- [invoice.xlsx](https://github.com/fomaaq/excel_console_app/blob/main/invoice.xlsx) -- the invoice file that was created by the app
-- --

## App creation motivation

I created this excel_console_app for:
- creating a console app
- study the library for working with dataframes
- implementations of excel file parsing
- simplifying the lives of my former colleagues, who will now be able to do their work faster and easier using this application

-- --

## How to use

To launch the application, you will need the order and price list files, which must necessarily match the sample

The following arguments must be entered in the console:

*order_path* -- path to the order file

*price_list_path* -- path to the price list file

*file_name* -- name of the invoice file to be created

App checks that the arguments are entered and starts its work:
1) checks that a file with the same name as you want to create does not exist, otherwise it returns an error
2) formats the data in the price list file for correct merging with the order file
3) creates invoice data from the order file and sets prices for each item according to the price list
4) saves the invoice file

Throughout the entire operation, the app prints messages about the success of any actions or prints error messages for the user and shuts down

Example of successful app execution: ![completed_successfully](https://github.com/fomaaq/excel_console_app/blob/main/imgs/completed_successfully.png)

### Errors and exit codes:
    1. Argument input errors:
        1.0.1. The path to the order file is not entered - 10001 
        1.0.1. The path to the price list file is not entered - 10002 
        1.0.1 The name of the saved invoice file is not entered - 10003 
    2. Errors with files:
        2.1. Checking the existence of the file:
            2.1.1. A file named {file_name} already exists, enter another file name - 20101
            2.1.1. Unable to save file - 20102
        2.2. File opening error:
            2.2.1. The data file was not found: {path}
                   Check path to it                    - 20201
        2.3. Errors of matching with the sample:
            2.3.1. The price list file does not match the sample - 20301
            2.3.2. The order file does not match the sample - 20302

Examples of errors:
|![arguments_error](https://github.com/fomaaq/excel_console_app/blob/main/imgs/arguments_error.png)|![error_already_existing_file](https://github.com/fomaaq/excel_console_app/blob/main/imgs/error_already_existing_file.png)|
|---|---|
|![error_match_sample](https://github.com/fomaaq/excel_console_app/blob/main/imgs/error_match_sample.png)|![file_open_error](https://github.com/fomaaq/excel_console_app/blob/main/imgs/file_open_error.png)|

Detailed descriptions of modules and methods are given in the documentation

-- --

## How to run
Python version 3.10 was used at launch

The requirements are specified in the [requirements.txt](https://github.com/fomaaq/excel_console_app/blob/main/requirements.txt)
