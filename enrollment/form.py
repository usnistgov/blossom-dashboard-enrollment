from wtforms import Form, BooleanField, StringField, validators, SubmitField
import enrollment.model as Enrollment

class EnrollmentForm(Form):
    agency    = StringField(
        'Agency', 
        validators = [
            validators.InputRequired(),
            validators.Length(min=3, max=128),
            validators.Regexp(
                regex=Enrollment.enrollment_tag_validation['pattern'],
                message=Enrollment.enrollment_tag_validation['message']
            )
        ]
    )

    system_owner = StringField(
        'System Owner', 
        validators = [
            validators.InputRequired(),
            validators.Length(min=3, max=128),
            validators.Regexp(
                regex=Enrollment.enrollment_tag_validation['pattern'],
                message=Enrollment.enrollment_tag_validation['message']
            )
        ]
    )

    assessor = StringField(
        'Assessor', 
        validators = [
            validators.InputRequired(),
            validators.Length(min=3, max=128),
            validators.Regexp(
                regex=Enrollment.enrollment_tag_validation['pattern'],
                message=Enrollment.enrollment_tag_validation['message']
            )
        ]
    )

    software_admin = StringField(
        'Software Administrator', 
        validators = [
            validators.InputRequired(),
            validators.Length(min=3, max=128),
            validators.Regexp(
                regex=Enrollment.enrollment_tag_validation['pattern'],
                message=Enrollment.enrollment_tag_validation['message']
            )
        ]
    )

    acquisition_officer = StringField(
        'Acquisition Officer', 
        validators = [
            validators.InputRequired(),
            validators.Length(min=3, max=128),
            validators.Regexp(
                regex=Enrollment.enrollment_tag_validation['pattern'],
                message=Enrollment.enrollment_tag_validation['message']
            )
        ]
    )

    agency_aws_account_id = StringField(
        'Agency AWS Account ID', 
        validators = [
            validators.InputRequired(),
            validators.Length(min=3, max=128),
            validators.Regexp(
                regex=Enrollment.enrollment_tag_validation['pattern'],
                message=Enrollment.enrollment_tag_validation['message']
            )
        ]
    )

    rules_of_behavior_accepted = BooleanField(
        'I have read and accept the Rules of Behavior.', 
        validators = [
            validators.InputRequired(),
            validators.Length(min=1, max=1),
            validators.Regexp(
                regex=Enrollment.enrollment_tag_validation['pattern'],
                message=Enrollment.enrollment_tag_validation['message']
            )
        ]
    )

    submit = SubmitField(label='Request Enrollment')