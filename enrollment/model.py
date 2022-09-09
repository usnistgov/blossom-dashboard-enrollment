import re
from fastapi import FastAPI
from pydantic import BaseModel, validator

enrollment_tag_validation = {
    'pattern': r"^[A-Za-z0-9]+[ A-Za-z0-9\_\.\:\/\=\+\-]{0,127}$",
    'message': "Is not an AWS Blockhain compatible tag. Tag keys can be a maximum of 128 characters and contain only unicode letters, digits, whitespace, and the following characters: _.:/=+-"
}

class Enrollment(BaseModel):
    """
    This model contains the required information for an enrollment request.
    """
    agency: str
    system_owner: str
    assessor: str
    software_admin: str
    acquisition_officer: str
    agency_aws_account_id: str
    rules_of_behavior_accepted: str
    proposal_id: str


    @validator("agency","system_owner","assessor","software_admin","acquisition_officer","agency_aws_account_id","rules_of_behavior_accepted")
    def aws_blockchain_tag(val, field):
        print(f"{'*'*5} Assessing {field} {val} {'*'*5}")
        if not re.match(enrollment_tag_validation['pattern'], val):
            print(f"{'*'*10} Error Validating Tag {'*'*10}")
            raise ValueError(enrollment_tag_validation['message'])
            # raise StrRegexError(pattern=enrollment_tag_validation['pattern'])
        
        return val

    class Config:
        schema_extra = {
            "example": {
                "agency": "DOC/NIST",
                "system_owner": "Paul E. Cee",
                "assessor": "",
                "software_admin": "",
                "acquisition_officer": "",
                "agency_aws_account_id": "",
                "rules_of_behavior_accepted": "",
                "proposal_id": ""
            }
        }



