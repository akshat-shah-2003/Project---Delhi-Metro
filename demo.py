import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_pos():
    with open("A1_pos.json", "r") as f:
        poosition = json.load(f)
    return poosition