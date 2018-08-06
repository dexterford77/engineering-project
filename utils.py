from datetime import date
from decimal import Decimal

ASSUMED_NUMBER_OF_COMMISSIONS = 3


def validate_commissions(num_of_commissions):
    return num_of_commissions == ASSUMED_NUMBER_OF_COMMISSIONS


def create_email_body(path):
    # method was not only inefficient, but actually buggy/broken as well
    # removed unnecessary space on left in "trans_amount_lines" by more accurately defining location of commission amount in file (ie, at index 29 rather than 28)
    # fixed error that disincludes last commission amount from total by changing line index cutoff from "-2" to "-1"
    # convert string to float early on, making "lstrip(0)" method unnecessary
    # removed unnecessary "to_dec" method; convert total to accurate decimal place by using simple math instead
    # final version much more readable, clear; unnecessary extra methods & iteration successfully refactored into simpler step-by-step code; major bug fixed
    with path.open() as f:
        # 29:39 contains the transaction amount
        trans_amount_lines = [line[29:39] for line in f][2:-1]
    decimal_converted_lines = [float(i)/100 for i in trans_amount_lines]
    summed_lines = sum(decimal_converted_lines)
    todays_date = date.today()
    body_format = {
                    'file_name': path.name,
                    'summed_lines': str(summed_lines),
                    'todays_date': str(todays_date)
                  }
    body = '''
The ACH file has been successfully transmitted the file {file_name} with a \
total ACH amount of ${summed_lines} to the bank on {todays_date}.
'''.format(**body_format)
    return body


def get_num_of_commissions(path):
    with path.open() as f:
        commission_lines = list(f)
    num_of_commissions = int(commission_lines[-1][18:21])
    return num_of_commissions
