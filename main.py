from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for any origin and GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow all origins
    allow_methods=["GET"],      # Only allow GET requests
    allow_headers=["*"],        # Allow all headers
)

# Load marks data from JSON file at startup
def load_marks():
    json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    # Convert list of dicts to a name:marks dictionary
    return {entry["name"]: entry["marks"] for entry in data}

MARKS_DB = load_marks()

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks = [MARKS_DB.get(n, 0) for n in name]
    return {"marks": marks}
