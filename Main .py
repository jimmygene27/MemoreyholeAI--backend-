
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow CORS for frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScanRequest(BaseModel):
    name: str
    email: str
    location: str

@app.get("/")
def root():
    return {"status": "MemoryHoleAI API is online."}

@app.post("/scan")
def scan(data: ScanRequest):
    # Simulated results for testing
    return {
        "name": data.name,
        "email": data.email,
        "location": data.location,
        "exposure": [
            {"site": "Spokeo", "status": "Found"},
            {"site": "BeenVerified", "status": "Found"},
            {"site": "Whitepages", "status": "Not Found"},
            {"site": "MyLife", "status": "Found"},
            {"site": "Intelius", "status": "Found"}
        ],
        "summary": "4 out of 5 major brokers have your data."
    }
