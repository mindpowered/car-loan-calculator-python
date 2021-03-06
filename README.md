
carloancalculator
=================
Car Loan Auto Loan Payment Calculator - Calculate financing on a new car including trade-in and taxes

![Build Status](https://mindpowered.dev/assets/images/github-badges/build-passing.svg)

Contents
========

* [Source Code and Documentation](#source-code-and-documentation)
* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Support](#support)
* [Licensing](#licensing)

# Source Code and Documentation
- Source Code: [https://github.com/mindpowered/car-loan-calculator-python](https://github.com/mindpowered/car-loan-calculator-python)
- Documentation: [https://mindpowered.github.io/car-loan-calculator-python](https://mindpowered.github.io/car-loan-calculator-python)

# About
This package aims to calculate the following:
- Given the price of a new car, what is the payment?
- Given a certain payment, what is the max price of the new car?

The calculation takes into account:
- The interest rate of the car loan
- The term (length) of the car loan
- Applicable Taxes
- Trade-in value and amount owing
- Down payment

# Requirements
- Requires Python 3.x. Due to security fixes and new features Python 3.7 or later is recommended.
- pip


Third-party dependencies may have additional requirements.

# Installation
You can retrieve the carloancalculator package from the Python Package Index https://pypi.org/ using pip. First make sure you have python3 and python3-pip installed. Then you can start by making a `requirements.txt` file in your working directory with the carloancalculator requirement in it. You can add any other packages to your requirements here, each as a separate line.

requirements.txt:
```
mindpowered-carloancalculator>0
```
Now you can use pip to install the carloancalculator package: `python3 -m pip install -r requirements.txt`
If you would like to update the package, simply run the above command again.


# Usage
```python
from mindpowered_carloancalculator import *

cc = CarLoanCalculator()
clc.CalcPayments(33429, 4500, 0, 10000, 2000, 0.7, 3.99);


```


# Support
We are here to support using this package. If it doesn't do what you're looking for, isn't working, or you just need help, please [Contact us][contact].

There is also a public [Issue Tracker][bugs] available for this package.

# Licensing
This package is released under the MIT License.



[bugs]: https://github.com/mindpowered/car-loan-calculator-python/issues
[contact]: https://mindpowered.dev/support/?ref=car-loan-calculator-python/
[docs]: https://mindpowered.github.io/car-loan-calculator-python/
[licensing]: https://mindpowered.dev/?ref=car-loan-calculator-python
[purchase]: https://mindpowered.dev/purchase/
