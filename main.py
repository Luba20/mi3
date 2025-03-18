from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid
import os
from typing import List

app = FastAPI()

# Assign the node ID from the environment variable
NODE_ID = os.getenv("NODE_ID", str(uuid.uuid4()))

class TimeDifferenceRequest(BaseModel):
    input_text: str  # Accepts plain text with timestamps

def parse_timestamp(timestamp: str) -> datetime:
    return datetime.strptime(timestamp, "%a %d %b %Y %H:%M:%S %z")

def time_difference(t1: str, t2: str) -> int:
    dt1 = parse_timestamp(t1)
    dt2 = parse_timestamp(t2)
    return abs(int((dt1 - dt2).total_seconds()))

@app.post("/calculate_time_difference", response_model=dict)
def calculate_time_difference(request: TimeDifferenceRequest):
    lines = request.input_text.strip().split("\n")
    
    if not lines:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    try:
        T = int(lines[0])  # Number of test cases
        if len(lines) != (T * 2 + 1):
            raise ValueError("Invalid number of lines provided")

        results = []
        for i in range(T):
            t1 = lines[1 + i * 2].strip()
            t2 = lines[2 + i * 2].strip()
            results.append(str(time_difference(t1, t2)))

        return {"id": NODE_ID, "result": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

