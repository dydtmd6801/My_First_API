from flask import Flask, request
import mysql.connector as cdgconn
from datetime import datetime

app = Flask(__name__)

setdb = {
    "user":"",
    "password":"",
    "host":"127.0.0.1",
    "database":"study",
    "port":"3306"
}

@app.route('/test', methods=['POST'])
def test():
    test = request.get_json()
    print(test)
    if not "key" in test:
        return {"reuslt" : "test_success"}
    else :
        return {"reuslt" : "test_fail"}

@app.route('/cdg', methods=['POST'])
def cdg():
    cdg_now_date = datetime.now()
    cdg_conn = cdgconn.connect(**setdb)
    cdg_cur = cdg_conn.cursor()
    result = 0
    cnt = 0
    user_data = request.get_json()
    if user_data:
        if "number" in user_data:
            if user_data["number"]:
                user_data_result = user_data["number"].replace("-","")
                for i in range(2,10):
                    result += int(user_data_result[cnt]) * i
                    cnt += 1
                for i in range(2,6):
                    result += int(user_data_result[cnt]) * i
                    cnt += 1
                result = result % 11
                result = result - 11
                if(int(abs(result)) == int(user_data_result[12])):
                    status = "True"
                    cdg_sql = f"insert into dbtest values ('{cdg_now_date}', '{user_data['number']}', '{status}')"
                    cdg_cur.execute(cdg_sql)
                    cdg_conn.commit()
                    cdg_conn.close()
                    return {"kimsu_is_good_teacher":"so delicious"}
                else:
                    status = "False"
                    cdg_sql = f"insert into dbtest values ('{cdg_now_date}', '{user_data['number']}', '{status}')"
                    cdg_cur.execute(cdg_sql)
                    cdg_conn.commit()
                    print(cdg_cur.fetchall())
                    cdg_conn.close()
                    return {"cdg":"no_cdg"}
            else:
                return {"value_error":"value_is_empty"}
        else:
            return {"key_error":"key = number"}
    else:
        return {"status":"fail"} 

app.run(host='0.0.0.0', port=8080, debug=True)