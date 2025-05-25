from fastapi import FastAPI, Query
from typing import List
import json
import os

app = FastAPI()

# Load marks data from JSON file at startup
def load_marks():
    json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
    with open(json_path, "r") as f:
        return json.load(f)

MARKS_DB = load_marks()

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    results = [{"name": n, "mark": MARKS_DB.get(n, 0)} for n in name]
    return {"results": results}
