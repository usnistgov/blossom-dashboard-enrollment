import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path
from action import Action

from enrollment.router import enrollment_router

respond = Action()
description = Path("README.md").read_text(encoding='utf-8')
enroller = FastAPI(
    title="Enrollment Dashboard",
    description=description,
    version="0.0.1",
    # swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)
templates = None

if os.path.exists("assets"):
    enroller.mount("/assets", StaticFiles(directory="assets"), name="assets")
else:
    raise Exception("Could not find Assets directory. Expecting 'assets/'.")

if os.path.exists("views"):
    views = Jinja2Templates(directory="views")
else:
    raise Exception("Could not find Views directory. Expecting 'views/'.")

@enroller.get("/")
def read_root():
    return RedirectResponse("/enroll")

@enroller.get("/status")
def read_status():
    return RedirectResponse("/assets/index.html")

@enroller.get("/about")
def read_about():
    return RedirectResponse("/docs")


enroller.include_router(enrollment_router)