# excel_console_app
This is a console application that uses the Pandas library to convert an order file into an invoice file using prices from a price list file.

-- --

## Calculator structure

- [desktop_calculator_oop.py](https://github.com/fomaaq/desktop_calc/blob/main/desktop_calculator_oop.py) -- the main file of the calculator that runs it
- [src/](https://github.com/fomaaq/desktop_calc/tree/main/src) -- contains the main calculator configuration file and a folder with widgets:
- - [src/caclulator.py](https://github.com/fomaaq/desktop_calc/blob/main/src/calculator.py) -- the main calculator configuration file that contains parameters, classes and methods for setting up, running and operating the calculator
- [src/widgets/](https://github.com/fomaaq/desktop_calc/tree/main/src/widgets) -- contains calculator widgets:
- - [src/widgets/window.py](https://github.com/fomaaq/desktop_calc/blob/main/src/widgets/window.py) -- contains classes and methods for configuring the window widget
- - [src/widgets/label.py](https://github.com/fomaaq/desktop_calc/blob/main/src/widgets/label.py) -- ccontains classes and methods for configuring the text label widget
- - [src/widgets/button.py](https://github.com/fomaaq/desktop_calc/blob/main/src/widgets/button.py) -- contains classes and methods for configuring the button widget
- - [src/widgets/icon_calc.png](https://github.com/fomaaq/desktop_calc/blob/main/src/widgets/icon_calc.png) -- icon for the window widget
- [alpha_version/desktop_calculator_old.py](https://github.com/fomaaq/desktop_calc/blob/main/alpha_version/desktop_calculator_old.py) -- alpha version of the calculator without OOP implementation

-- --

## Calculator creation motivation

I created this calculator with GUI for:
- study library for creating a GUI on python
- create a project with the implementation of OOP
- implement encapsulation

-- --

## Preview

The calculator is controlled using a graphical keyboard
The calculator can perform basic calculations

Example of calculator operation:

![Demo](https://github.com/fomaaq/desktop_calc/blob/main/imgs/demo.gif)

Detailed descriptions of modules and methods are given in the documentation

-- --

## How to run
Python version 3.10 was used at launch

The requirements are specified in the [requirements.txt](https://github.com/fomaaq/desktop_calc/blob/main/requirements.txt)
