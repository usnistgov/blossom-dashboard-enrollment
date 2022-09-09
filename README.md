# Service Administration Dashboard (SAD) - Enrollment

> [Requirements Defined in Issue 57](https://github.com/usnistgov/blossom/issues/57)

## Local Installation

### Set Up Project

#### Initialize Virtual Environment (For New Environment)

```
cd blossom-dashboard-enrollment
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

### Running the Application Programming Interface (API)

```
.nist-py-env/bin/uvicorn api:enroller --reload --host 0.0.0.0 --port 10000
```