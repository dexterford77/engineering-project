from datetime import date
from decimal import Decimal

ASSUMED_NUMBER_OF_COMMISSIONS = 3


def validate_commissions(num_of_commissions):
    return num_of_commissions == ASSUMED_NUMBER_OF_COMMISSIONS


def create_email_body(path):
    def to_dec(s): return Decimal('{}.{}'.format(s[:-2], s[len(s)-2:]))
    with path.open() as f:
        # 28:39 contains the transaction amount
        trans_amount_lines = [line[28:39] for line in f][2:-2]
    decimal_converted_lines = list()
    for line in trans_amount_lines:
        s = line.lstrip('0')
        decimal_converted_lines.append(to_dec(s))
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
    num_of_commissions = commission_lines[-1][18:21]
    num_of_commissions.lstrip('0')
    return num_of_commissions
