from chalice import Chalice
import boto3
import logging
from chalicelib.utils import create_email_body, get_num_of_commissions, validate_commissions

log = logging.getLogger()
log.setLevel(logging.INFO)

bucket_name = 'bucket_value_to_be_replaced'
app = Chalice(app_name='chalice_email_processing')

@app.on_s3_event(bucket=bucket_name)
def handler(event):
    """
    Whenver an object is uploaded to the user-specified bucket, this lambda function will be invoked.
    """
    s3 = boto3.client('s3')
    if event:
        filename = str(event.key)
        file_obj = s3.get_object(Bucket = bucket_name, Key = filename)
        file_contents = file_obj["Body"].read().decode('utf-8')
        run_file(file_contents, filename)


def run_file(file_contents, filename):
    log.info('Reading commission file...')
    num_of_commissions = get_num_of_commissions(file_contents)
    log.info('Validating file...')
    commission_is_valid = validate_commissions(num_of_commissions)
    email_body = create_email_body(file_contents.splitlines(), filename) if commission_is_valid else 'Failed to validate'

    print(email_body)


if __name__ == '__main__':
    main()
