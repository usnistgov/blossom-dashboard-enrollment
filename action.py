import re
import boto3, dotenv, os, requests
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, ValidationError
from botocore.exceptions import ClientError

r"""Enrollment Dashboard: Command Line Interface"""


class Action(object):
    """Access to the Enrollment Dashboard actions class via terminal."""
    def test(self):
        """Test Output: Just prints 'Testing'"""
        print("Testing")


    def create_proposal(self, enrollment):

        try:

            if os.environ.get('AWS_PROFILE') == 'saml':
                print("Using Local Environment")
                client = boto3.client('managedblockchain')
            else:
                print("Using AWS Environment")
                session = requests.get(f"{os.environ.get('AUTH_HOST')}{os.environ.get('AUTH_PATH')}")
                session_config = session.json()

                client = boto3.client('managedblockchain',
                                region_name=os.environ.get('AWS_REGION'),
                                aws_access_key_id=session_config['AccessKeyId'],
                                aws_secret_access_key=session_config['SecretAccessKey'],
                                aws_session_token=session_config['Token']
                            )                

            proposal = enrollment.dict()
            proposal.pop("proposal_id", None)

            response = client.create_proposal(
                NetworkId=os.environ.get('NID'),
                MemberId=os.environ.get('MID'),
                Actions={
                    'Invitations': [
                        {
                            'Principal': enrollment.agency_aws_account_id
                        },
                    ]
                },
                Description=f"Request for enrollment: {enrollment.agency}",
                Tags=proposal
            )

        except ClientError as e:
            print(f"Error Creating Proposal!! {e}")
            return False
        

        print("*"*100)
        print(f"Mock Creation of Enrollment ({type(enrollment)})")
        print(f"{enrollment}")
        print(response)
        print("*"*100)
            
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return response
        else:
            return None



        