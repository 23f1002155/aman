from fastapi import FastAPI
import os

secret_key = os.environ.get("SECRET_KEY")


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
