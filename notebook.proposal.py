#%% Load Library
from enrollment.model import Enrollment
from action import Action
responder = Action()

#%% Configure Enrollment
sample = {
    "agency": "DOC/NIST",
    "system_owner": "Paul E. Cee",
    "assessor": "",
    "software_admin": "",
    "acquisition_officer": "",
    "agency_aws_account_id": "",
    "rules_of_behavior_accepted": ""
}
sample

#%% Create Object
enrollment = Enrollment(
    agency = sample['agency'], 
    system_owner = sample['system_owner'],
    assessor = sample['assessor'],
    software_admin = sample['software_admin'],
    acquisition_officer = sample['acquisition_officer'],
    agency_aws_account_id = sample['agency_aws_account_id'],
    rules_of_behavior_accepted = sample['rules_of_behavior_accepted']
)
enrollment

#%% Create Proposal
responder.create_proposal(enrollment)

#%%