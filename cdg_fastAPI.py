from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from starlette.requests import Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

template = Jinja2Templates(directory="./jinja_first")

app = FastAPI()

@app.get("/cdg/{cdg_num}", response_class=HTMLResponse)
async def cdg(request:Request, cdg_num:str):
    result = int(0)
    cnt = int(2)
    cdg_pass = cdg_num
    cdg_num = cdg_num.replace("-","")
    if len(cdg_num) == 13:
        for i in range(0, 12):
            result += int(cdg_num[i]) * cnt
            cnt += 1
            if(cnt >= 10):
                cnt = 2
        result = result % 11
        result = 11 - result
        if(int(abs(result)) == int(cdg_num[12])):
            return template.TemplateResponse("index.html",{"request":request, "id":cdg_pass, "status":"올바른 주민등록번호"})
        else:
            return template.TemplateResponse("index.html",{"request":request, "id":cdg_pass, "status":"틀린 주민등록번호"})
    else:
        return {"status":"enough_data"}

if __name__ == "__main__":
    uvicorn.run("cdg_fastAPI:app", host="0.0.0.0", port=5000, debug=True)