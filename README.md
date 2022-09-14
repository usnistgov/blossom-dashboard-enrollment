# Service Administration Dashboard (SAD) - Enrollment

> [Requirements Defined in Issue 57](https://github.com/usnistgov/blossom/issues/57)

## Local Installation

### Set Up Project

#### Initialize Virtual Environment (For New Environment)

```
python -m venv .nist-py-env
```

#### Activate Environment (Windows)

```
.nist-py-env\Scripts\activate.bat
```

#### Activate Environment (macOS)

```
source .nist-py-env/bin/activate
```

#### Install Requirements

```
pip install -r requirements.txt
```

### Running the Command Line Interface (CLI)

#### Available Commands

```
python app.py
```

#### Test Output

```
python app.py test
```

### Running the Application Programming Interface (API) Locally

This method requires you to set up a local credential file for AWS if you want to create the actual proposals in AWS.

Set up requires the [blossom](https://github.com/usnistgov/blossom) repository is similar to:

```
python3 /Code/blossom/util/aws_saml_auth.py
cat ~/.aws/credentials
export AWS_PROFILE='saml'
aws --profile saml sts get-caller-identity
```

```
docker-compose -f docker-compose-local.yml up
```

or with any development services/features:

```
docker-compose -f docker-compose-local.yml --profile=development up
```

### Running in the AWS Environment

This method will request a token when the proposal is being created. This is configured using the .env referenced in docker-compose.yaml.  The format is shown in `sample.env`.  The default location is `~/.env`.

```
docker-compose up -d
```