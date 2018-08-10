# Transaction E-mail Generator

## How to Set Up

1. Download this app to your local system & navigate to the app's directory.
1. Install requirements (ie, [Chalice](https://github.com/aws/chalice)) using [pip](https://pypi.org/project/pip/).
1. Make sure your [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) credentials are properly configured.
1. Create a new bucket in your AWS S3.
1. Edit the value of `bucket_name` in `app.py` so that it equals the name of your new bucket. You can do this by running `sed -i 's/bucket_value_to_be_replaced/WRITE_YOUR_BUCKET_NAME_HERE/g' app.py` or by editing `app.py` manually.

## How to Run

1. Run `chalice deploy` in your CLI (this will create your Lambda function upstream).
1. Upload a file to your AWS S3 bucket.
1. Check the logs of your newly-created Lambda function for the generated e-mail. You can reach these logs by navigating to your Lambda function in the AWS console, selecting the "Monitoring" tab, and selecting "View Logs in CloudWatch." Select the most recent Log Stream to view the logs as well as the text of the generated e-mail.

## How to Run Tests

1. Run `python tests/utils.py` in you CLI.
