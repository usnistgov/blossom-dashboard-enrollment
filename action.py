import boto3, dotenv, os
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
            client = boto3.client('managedblockchain')

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



        