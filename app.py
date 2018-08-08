from pathlib import Path

from utils import create_email_body, get_num_of_commissions, validate_commissions
import click
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)


@click.command()
@click.option('--file_path', help='relative path to the bank file to read', required=True)
def main(file_path: str):
    """
    Simple runner method to read a commission file, validate, and create an email body
    :param file_path: relative path to the file to read
    :return: contents of an email that could be sent
    """
    log.info('Reading commission file...')
    path_obj = Path(file_path)
    num_of_commissions = get_num_of_commissions(path_obj)
    log.info('Validating file...')
    commission_is_valid = validate_commissions(num_of_commissions)
    email_body = create_email_body(path_obj) if commission_is_valid else 'Failed to validate'

    print(email_body)


if __name__ == '__main__':
    main()
