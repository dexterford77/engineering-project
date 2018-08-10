from datetime import date
from decimal import Decimal
import logging

ASSUMED_NUMBER_OF_COMMISSIONS = 3
log = logging.getLogger()



def validate_commissions(num_of_commissions):
    """
    Returns true if input number of commissions matches assumed number of commissions.
    """
    return num_of_commissions == ASSUMED_NUMBER_OF_COMMISSIONS


def create_email_body(file_contents, filename):
    """
    Parses information from file and returns formatted email body as a string.
    """

    """
    CHANGE NOTES:
    Method was not only inefficient, but actually buggy/broken as well:
    - removed unnecessary space on left in "trans_amount_lines" by more accurately defining starting location of commission amount in file (ie, at index 29 rather than 28)
    - fixed error that disincludes last commission amount from total by changing line index cutoff from "-2" to "-1"
    - convert string to float earlier on, making "lstrip(0)" method unnecessary
    - removed unnecessary "to_dec" method; convert total to accurate decimal place by using basic math instead
    Final version much more readable & clear; unnecessary extra methods & iteration successfully refactored into simpler step-by-step code; major bug fixed.
    """
    
    # 29:39 contains the transaction amount
    trans_amount_lines = [line[29:39] for line in file_contents][2:-1]
    # converts each transaction amount string to decimal
    decimal_converted_lines = [float(i)/100 for i in trans_amount_lines]
    log.debug('Transaction amounts: %s', decimal_converted_lines)
    # sums transaction amounts
    summed_lines = sum(decimal_converted_lines)
    todays_date = date.today()
    body_format = {
                    'file_name': filename,
                    'summed_lines': str(summed_lines),
                    'todays_date': str(todays_date)
                  }
    body = '''
The ACH file {file_name} with a total ACH amount of ${summed_lines} \
has been successfully transmitted to the bank on {todays_date}.
'''.format(**body_format)
    return body


def get_num_of_commissions(file_contents):
    """
    Parses file data to return total number of commissions as an integer.
    """

    """
    CHANGE NOTES:
    Method was returning value as a string, causing validation errors.
    - Corrected method so that it returns value as integer.
    - Implemented regression test to ensure method outputs value as integer.
    """

    commission_lines = list(file_contents.splitlines())
    # 18:21 on the final line contains the number of commissions
    num_of_commissions = commission_lines[-1][18:21]
    log.debug('Number of commissions: %s', num_of_commissions)
    num_of_commissions = int(num_of_commissions)
    return num_of_commissions

