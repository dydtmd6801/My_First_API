import mysql.connector as myconn
# import ~ as - : ~를 -로 바꾸어 사용가능
# db연동에서는 dbconnector와 dbcursor가 가장 중요
from datetime import datetime

setdb = {
    "user":"",
    "password":"",
    "host":"127.0.0.1",
    "database":"study",
    "port":"3306"
}
# db설정을 세팅한다.

conn = myconn.connect(**setdb)
# db에 연결
cur = conn.cursor()
# cursor, db에 연결의 cursor를 cur에 저장

visit_time_data = datetime.now()
#.strftime("%Y-%m-%d")
jumin_data = input()
result_data = 1

sql = f"insert into dbtest values ('{visit_time_data}', '{jumin_data}', '{result_data}')"
# sql 쿼리를 작성
print(sql)
cur.execute(sql)
# cur 변수안의 내용을 sql 쿼리를 넣어 실행한다.
conn.commit()
# insert into를 쓰고 commit을 필수로 해 줘야함
result = cur.fetchall()
# db의 결과를 result에 저장
conn.close()
# db 연동을 끊음
print(result)