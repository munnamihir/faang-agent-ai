
from fastapi import FastAPI

app = FastAPI(title="FAANG Agent AI")

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "FAANG Agent AI"
    }
