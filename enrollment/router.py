import os
from action import Action

from fastapi import APIRouter, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import ValidationError

from enrollment.model import Enrollment
from enrollment.form import EnrollmentForm

enrollment_router = APIRouter()

do = Action()

if os.path.exists("views"):
    views = Jinja2Templates(directory="views")
else:
    raise Exception("Could not find Views directory. Expecting 'views'.")

# http://127.0.0.1:10000/enroll
@enrollment_router.get("/enroll", response_class=HTMLResponse)
async def read_item(request: Request):
    form = EnrollmentForm()
    return views.TemplateResponse("enrollment/form.html", { "request": request, "form": form })

#pylint: disable=too-many-arguments
@enrollment_router.post("/enroll")
async def enroll(
        request: Request, 
        agency: str = Form(), 
        system_owner: str = Form(),
        assessor: str = Form(),
        software_admin: str = Form(),
        acquisition_officer: str = Form(),
        agency_aws_account_id: str = Form(),
        rules_of_behavior_accepted: str = Form()
    ):
    
    try:
        enrollment = Enrollment(
            agency = agency, 
            system_owner = system_owner,
            assessor = assessor,
            software_admin = software_admin,
            acquisition_officer = acquisition_officer,
            agency_aws_account_id = agency_aws_account_id,
            rules_of_behavior_accepted = rules_of_behavior_accepted,
            proposal_id = ''
        )

        result = do.create_proposal(enrollment)

        if result:
            enrollment.proposal_id = result['ProposalId']
            return views.TemplateResponse("enrollment/complete.html", { "request": request, "enrollment": enrollment })

        return views.TemplateResponse("enrollment/error.html", { "request": request, "detail": "Proposal creation with the provider was not successful." }, status_code=500)
    except ValidationError as e:
        # raise HTTPException(status_code=500, detail="The enrollment request could not be completed.") from e
        return views.TemplateResponse("enrollment/error.html", { "request": request, "detail": "The enrollment request could not be completed." }, status_code=500)







# @enroller.post("/upload/{filename}")
# async def upload_and_process(filename: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(process_file, filename)
#     return {"message": "processing file"}



# # http://127.0.0.1:10000/items/123
# @enroller.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return views.TemplateResponse("item.html", { "request": request, "id": id })


# ORJSONResponse,JSONResponse,