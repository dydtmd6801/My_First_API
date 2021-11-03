from flask import Flask, request
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():

    con = sqlite3.connect("User_Data.db", check_same_thread=False)
    cur = con.cursor()

    User_Data = request.get_json()
    if User_Data:
        if "name" in User_Data:
            if User_Data["name"]:
                User_Data_value = User_Data["name"]
                sql = f"select * from play_data where username='{User_Data_value}'"
                cur.execute(sql)
                result = cur.fetchall()
                return json.dumps(result)
            else:
                return {"value":"not_found_value"}
        else:
            return {"key_error":"key_is_name"}
    else:
        return {"data_error":"not_found_data"}

@app.route("/top", methods=["POST"])
def top():

    con = sqlite3.connect("User_Data.db", check_same_thread=False)
    cur = con.cursor()

    User_Data = request.get_json()
    if User_Data:
        if "count" in User_Data:
            if User_Data["count"]:
                User_Data_value = User_Data["count"]
                if User_Data_value.isdigit() == True:
                    sql = f"select * from play_data order by score desc limit {User_Data_value}"
                    cur.execute(sql)
                    result = cur.fetchall()
                    return json.dumps(result)
                else:
                    return {"typeError":"integer"}
            else:
                return {"value":"not_found_value"}
        else:
            return {"key_error":"key_is_count"}
    else:
        return {"data_error":"not_found_data"}

@app.route("/insert", methods=["POST"])
def insert():

    con = sqlite3.connect("User_Data.db", check_same_thread=False)
    cur = con.cursor()

    User_Data_Time = datetime.now()
    User_Data = request.get_json()
    User_Data_Score = request.get_json()
    if User_Data and User_Data_Score:
        if "name" in User_Data and "score" in User_Data_Score:
            if User_Data["name"] and User_Data_Score["score"]:
                User_Data_value = User_Data["name"]
                User_Data_Score_value = User_Data_Score["score"]
                if User_Data_Score_value.isdigit() == True:
                    sql = f"insert into play_data values ('{User_Data_value}', {User_Data_Score_value},'{User_Data_Time}')"
                    print(sql)
                    cur.execute(sql)
                    con.commit()
                    return {"status":"save_data"}
                else:
                    return {"score_value":"only_integer"}
            else:
                return {"value":"not_found_value"}
        else:
            return {"key_error":"key_is_name_and_score"}
    else:
        return {"data_error":"not_found_data"}


app.run(host='0.0.0.0', port=8080, debug=True)