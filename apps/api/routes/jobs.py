
from fastapi import APIRouter

router = APIRouter(prefix="/jobs")

@router.get("/")
def jobs():
    return [
        {
            "title": "Software Engineer",
            "company": "Google"
        }
    ]
