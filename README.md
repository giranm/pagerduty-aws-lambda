# pagerduty-aws-lambda

A collection of useful AWS Lambda Python scripts which extends functionality for a given PagerDuty instance.

## Development Setup

### Python

To ensure consistency between local and AWS runtimes, we recommend using [pyenv](https://github.com/pyenv/pyenv) to manage your Python workspace.  
This will allow you to switch between specific versions of Python as well as managing the appropriate virtual environment.

#### Install target version of Python using pyenv

To install a specific version of Python to your machine, use the following command:  
`$ pyenv install 3.7.7`

```bash
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.7.7.tar.xz...
-> https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tar.xz
Installing Python-3.7.7...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.7.7 to /Users/giran/.pyenv/versions/3.7.7
```

#### Set global version of Python for runtime using pyenv

`$ pyenv global 3.7.7`

To verify this has been set globally:  
`$ pyenv global`

```
3.7.7
```

`$ pyenv versions`

```bash
  system
* 3.7.7 (set by /Users/giran/dev/python/pagerduty-aws-lambda/update-incident-urgency/.python-version)
...
```

#### Create virtualenv using pyenv

To create a virtual environment for developing AWS Lambda functions, use the following:  
`$ pyenv virtualenv aws-lambda`

```bash
Looking in links: /var/folders/ny/bh58b2cd69d8k5kpsclwj31h0000gn/T/tmpttg4jtds
Requirement already satisfied: setuptools in /Users/giran/.pyenv/versions/3.7.7/envs/aws-lambda/lib/python3.7/site-packages (41.2.0)
Requirement already satisfied: pip in /Users/giran/.pyenv/versions/3.7.7/envs/aws-lambda/lib/python3.7/site-packages (19.2.3)
```

#### Enter virtualenv using pyenv

`$ pyenv activate aws-lambda`

If successful, the terminal prompt will have the virtualenv prefixed.  
i.e. `(aws-lambda) giran@Girans-MacBook-Pro.local ~ $`

#### Install dependencies to virtualenv using requirements file (Local Runtime)

`$ cd PROJECT_FOLDER`  
`$ pip install -r requirements.txt`

Example output for installing the [requests](https://requests.readthedocs.io/en/master/) module:

```bash
Collecting requests==2.23.0 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/1a/70/1935c770cb3be6e3a8b78ced23d7e0f3b187f5cbfab4749523ed65d7c9b1/requests-2.23.0-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests==2.23.0->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/5e/c4/6c4fe722df5343c33226f0b4e0bb042e4dc13483228b4718baf286f86d87/certifi-2020.6.20-py2.py3-none-any.whl (156kB)
     |████████████████████████████████| 163kB 1.5MB/s
Collecting chardet<4,>=3.0.2 (from requests==2.23.0->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests==2.23.0->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl
Collecting idna<3,>=2.5 (from requests==2.23.0->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 7.0MB/s
Installing collected packages: certifi, chardet, urllib3, idna, requests
Successfully installed certifi-2020.6.20 chardet-3.0.4 idna-2.10 requests-2.23.0 urllib3-1.25.9
WARNING: You are using pip version 19.2.3, however version 20.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

#### Invoke lambda script using local Python instance

A cli-wrapper script `lambda_function_test.py` should be used to invoke `lambda_function.py` using the appropriate event/args.

`(aws-lambda) $ ~/.pyenv/versions/aws-lambda/bin/python path/to/lambda_function_test.py`

### AWS

Once your local Python script works as intended, you will need to upload this using the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).  
The remaining sections of this guide assumes you have installed the CLI, and have authenticated correctly against the correct profile/region.

#### Install dependencies to local disk using requirements file (AWS Runtime)

Assuming you are in the correct project folder:  
`$ pip install -r requirements.txt -t .`

Requests module output is similar to before, but with additional files added to local folder path.  
This is the preferred method for packaging `requests` given the removal of the [Botocore vendored version](https://aws.amazon.com/blogs/developer/removing-the-vendored-version-of-requests-from-botocore/) as of October 2019.

```bash
Collecting requests==2.23.0 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/1a/70/1935c770cb3be6e3a8b78ced23d7e0f3b187f5cbfab4749523ed65d7c9b1/requests-2.23.0-py2.py3-none-any.whl
Collecting idna<3,>=2.5 (from requests==2.23.0->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/89/e3/afebe61c546d18fb1709a61bee788254b40e736cff7271c7de5de2dc4128/idna-2.9-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests==2.23.0->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/57/2b/26e37a4b034800c960a00c4e1b3d9ca5d7014e983e6e729e33ea2f36426c/certifi-2020.4.5.1-py2.py3-none-any.whl
Collecting chardet<4,>=3.0.2 (from requests==2.23.0->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests==2.23.0->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl
Installing collected packages: idna, certifi, chardet, urllib3, requests
Successfully installed certifi-2020.4.5.1 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.9
WARNING: You are using pip version 19.2.3, however version 20.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

`$ ls -l .`

```bash
total 8
drwxr-xr-x   3 giran  staff    96  1 Jun 11:54 bin
drwxr-xr-x   7 giran  staff   224  1 Jun 11:54 certifi
drwxr-xr-x   8 giran  staff   256  1 Jun 11:54 certifi-2020.4.5.1.dist-info
drwxr-xr-x  43 giran  staff  1376  1 Jun 11:54 chardet
drwxr-xr-x  10 giran  staff   320  1 Jun 11:54 chardet-3.0.4.dist-info
drwxr-xr-x  11 giran  staff   352  1 Jun 11:54 idna
drwxr-xr-x   8 giran  staff   256  1 Jun 11:54 idna-2.9.dist-info
drwxr-xr-x  21 giran  staff   672  1 Jun 11:54 requests
drwxr-xr-x   8 giran  staff   256  1 Jun 11:54 requests-2.23.0.dist-info
-rw-r--r--   1 giran  staff    16  1 Jun 11:52 requirements.txt
drwxr-xr-x  16 giran  staff   512  1 Jun 11:54 urllib3
drwxr-xr-x   8 giran  staff   256  1 Jun 11:54 urllib3-1.25.9.dist-info
```

#### Create zip file containing serverless code

`$ zip -r9 [PROJECT_NAME].zip * -x "bin/*" requirements.txt README.md`

```bash
  adding: certifi/ (stored 0%)
  adding: certifi/__init__.py (stored 0%)
  ...
  adding: urllib3-1.25.9.dist-info/ (stored 0%)
  adding: urllib3-1.25.9.dist-info/RECORD (deflated 62%)
  adding: urllib3-1.25.9.dist-info/WHEEL (deflated 14%)
  adding: urllib3-1.25.9.dist-info/top_level.txt (stored 0%)
  adding: urllib3-1.25.9.dist-info/LICENSE.txt (deflated 41%)
  adding: urllib3-1.25.9.dist-info/INSTALLER (stored 0%)
  adding: urllib3-1.25.9.dist-info/METADATA (deflated 64%)
```

#### Update zip file with newer code

`$ zip -g [PROJECT_NAME].zip lambda_function.py`

```bash
updating: lambda_function.py (deflated 22%)
```

#### Upload local zip to update remote AWS Lambda function

`$ aws lambda update-function-code --function-name [PROJECT_NAME] --zip-file fileb://[PROJECT_NAME].zip`

```bash
{
    "FunctionName": "[PROJECT_NAME]",
    "FunctionArn": "arn:aws:lambda:us-east-1:864672256020:function:[PROJECT_NAME]",
    "Runtime": "python3.7",
    "Role": "arn:aws:iam::864672256020:role/pd-github-public-repo-lambda",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 917186,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2020-06-01T15:13:51.878+0000",
    "CodeSha256": "NEL7Y8c6D8lJWNuw/u2APB0JWu7QgylxJCJJMHc5bko=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "3f4c0130-4cff-415f-8769-f514a3d20332",
    "State": "Active",
    "LastUpdateStatus": "Successful"
}
```

#### Invoke remote AWS Lambda from local CLI (returns JSON response)

`$ aws lambda invoke --function-name [PROJECT_NAME] --payload '{"key": "value"}' output.txt`

```bash
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```
