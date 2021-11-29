from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
import uvicorn
import sqlite3

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class student_info(BaseModel):
    name: str
    code: str
    tel: Optional[str] = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/test")
def test(item:Item):
    print(item.name)
    return item

@app.post("/insert")
def insert(item:student_info):
    name_data = item.name
    code_data = item.code
    tel_data = item.tel

    con = sqlite3.connect("student_info")
    cur = con.cursor()

    sql = f"insert into student_info values ('{name_data}', '{code_data}', '{tel_data}')"
    print(sql)
    cur.execute(sql)
    con.commit()
    con.close()
    return {"status":"success"}

if __name__ == "__main__":
    uvicorn.run("FastAPI_Basic:app", host="0.0.0.0", port=5000,debug=True)