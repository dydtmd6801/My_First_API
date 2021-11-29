from flask import Flask, request
import mysql.connector as myconn
import requests

app = Flask(__name__)

setdb = {
    "username":"",
    "password":"",
    "host":"127.0.0.1",
    "database":"login_data",
    "port":"3306"
}

@app.route("/register", methods=["POST"])
def register():

    con = myconn.connect(**setdb)
    cur = con.cursor()

    register = request.get_json()
    if register:
        if "id" in register and "pw" in register:
            if register["id"] and register["pw"]:
                register_id = register["id"]
                register_pw = register["pw"]
                sql = f"insert into member values ('{register_id}','{register_pw}')"
                cur.execute(sql)
                con.commit()
                con.close()
                return {"status":"success"}
            else:
                return {"value_error":"no_value"}
        else:
            return {"key_error":"key_is_id_and_pw"}
    else:
        return {"data_error":"no_data"}

@app.route("/send", methods=["POST"])
def send():

    con = myconn.connect(**setdb)
    cur = con.cursor()

    user_data = request.get_json()
    if user_data:
        if "id" in user_data and "pw" in user_data and "msg" in user_data:
            if user_data["id"] and user_data["pw"] and user_data["msg"]:
                user_data_id = user_data["id"]
                user_data_msg = user_data["msg"]
                sql = f"select * from member where id='{user_data_id}'"
                cur.execute(sql)
                result = cur.fetchall()
                print(result[0])
                if result:
                    text = {"text":user_data_msg + "유용승"}
                    url = ''
                    res = requests.post(url, json=text)
                    print("res : " + str(res.status_code))
                    return {"status":"success"}
                else:
                    return {"result_error":"no_result"}
            else:
                return {"value_error":"no_value"}
        else:
            return {"key_error":"id_pw_msg"}
    else:
        return {"data_error","no_data"}    

app.run(host="0.0.0.0", port=8080, debug=True)