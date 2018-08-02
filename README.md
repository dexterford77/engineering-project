# Engineering Project
This is a sample project containing several tasks mimicking what a developer on the AFR Dev Team may see.

## Background
Once a month, our payment vendor will send us a file indicating financial transfers for our agent's
commissions. This file must be validated for accuracy (i.e. the file is valid and contains the anticipated 
number of transactions) before being sent to the bank for processing. Once the file has been sent to the bank, 
an email is sent to predetermined recipients containing a summary of the transfer (the filename sent and 
the total dollar amount sent). 

## CLI, Running, and Requirements
For the purposes of simplicity, `app.py` contains a Command Line Interface to process the file. It takes a single 
argument of `--file_path` which is the relative path to the file to run against. For example, the file 
`corrupt.txt` could be processed by running `python app.py examples/corrupt.txt`. 
 
This process is written using Python 3.6 and contains python requirements in `requirements.txt` which can 
be installed using [pip](https://pypi.org/project/pip/). 

## Tasks
Once you set up and configure your development environment as you wish, here are some tasks to be performed. 
For the sake of this exercise, commit your solution to each task to your GitHub fork with a commit message 
containing the task number and a brief explanation of your work (similar to a traditional commit message).

1. Currently, none of these files are properly parsing! No matter which file is used, it always returns 
`Failed to validate`. Diagnose what's going on and implement a fix.

1. Within `utils.py` the method `create_email_body` creates more questions the longer you look at it and is
therefore not as efficient as it could be. Although efficiency is not a pain point currently, it is good 
practice to be mindful of efficient coding. Go ahead and rewrite this method to something simpler and 
explain why your solution is better than the existing implementation. 

1. As you look through this codebase, you'll notice a lack of documentation, logging, and tests. 
Add comments and docstrings as appropriate within methods. Implement a simple logger for the process
and add logging statements such that the logs indicate what the program is doing as well as give hints to 
what caused an error (corrupt or not-validated input file, network errors, etc). Try and find the balance
between detailed debug information and excessively noisy output. 
Also implement unittests for `create_email_body` and `get_num_of_commissions` methods. These can be fairly
simple tests, but be sure to include a regression test from the second task above so this issue won't happen again. 
For this task, we are looking at the quality of test cases you write, not quantity. About two cases per method 
will be sufficient. 
 
1. Currently this process runs on an AWS EC2 instance. As a new developer, you heard about this cool, new 
service AWS is offering called ['Lambda'](https://aws.amazon.com/lambda/). Rewrite `app.py` as 
a Lambda Function that gets a file off of S3 and processes it on demand 
([S3 Trigger](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)). In doing this you will need to 
implement a method to download the file (listed in the S3 Event Trigger) to local storage and process it. 

1. Lambda functions are great, but infrastructure as code and repeatable deployments are better. Create 
a repeatable deployment method for your newly created Lambda Function. For this exercise, you do not need
to worry about using a VPC. This deployment package should create any permissions and roles required for
the Lambda Function to run.  
There are several different tools out there to deploy to AWS. AWS has 
[several tools](https://docs.aws.amazon.com/lambda/latest/dg/automating-deployment.html) 
of their own, but do not feel restricted to only these tools. 

## Expectations
For this project, we are looking more at your methods and choice of technologies rather than the specific 
methods you use to produce the expected results. Technologies are rapidly changing these days and we must be 
open to learning what is out there and evaluate which technologies fit our use case the best. 

Don't get hung up on specific numbers of comments, tests, logs, etc. We will be more interested in the quality, 
i.e. how clear and concise your work is. 

## Conclusion
Once you have completed the above tasks and committed them to GitHub, create a Pull Request for us to review. 
Within your pull request, you can provide more information describing the thought process behind your choices
or other relevant comments on your work. 

Good Luck! 
