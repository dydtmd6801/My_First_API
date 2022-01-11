from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from starlette.requests import Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import csv;

app = FastAPI()

template = Jinja2Templates(directory="./file_io")

@app.get("/file_io_exam/{date}", response_class=HTMLResponse)
async def file_io_exam(request: Request, date: str):
    with open("data.csv", "r") as f:
        reader = csv.DictReader(f)
        a = list(reader)
        transfer_date = []
        for row in a:
            if date in row["datetime"]:
                transfer_date.append(row)
        return template.TemplateResponse("index.html",{"request":request, "input_date":date, "date":transfer_date})
                
if __name__ == "__main__":
    uvicorn.run("file_io_fastAPI:app", host="0.0.0.0", port=5000, debug=True)