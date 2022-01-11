from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import sqlite3

class best_food(BaseModel):
    place : str
    menu : str
    content : str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/insert")
def insert(item:best_food):
    place_data = item.place
    menu_data = item.menu
    content_data = item.content

    con = sqlite3.connect("best_food")
    cur = con.cursor()

    sql = f"insert into best_food values ('{place_data}', '{menu_data}', '{content_data}')"
    print(sql)
    cur.execute(sql)
    con.commit()
    con.close()
    return {"status":"success"}

@app.post("/search_all")
def search_all():

    con = sqlite3.connect("best_food")
    cur = con.cursor()

    sql = "select * from best_food"
    # result = cur.execute(sql).fetchall()
    # print(result)
    for row in cur.execute(sql):
        print(row)
    return {"status":"search_success"}

if __name__ == "__main__":
    uvicorn.run("best_food:app", host="0.0.0.0", port=5000,debug=True)