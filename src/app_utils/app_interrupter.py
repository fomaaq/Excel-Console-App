'''
The module contains a method for printing an error message and interrupting the app
'''


def interrupt_app(error_message: str, exit_code: int):
    '''
    Prints an error message and exits the app
    '''
    print(error_message)
    exit(exit_code)
