from flask import Flask, request
import mysql.connector

app = Flask(__name__)

setdb = {
    "user":"",
    "password":"",
    "host":"127.0.0.1",
    "database":"product_store",
    "port":"3306"
}

conn = mysql.connector.connect(**setdb)
cur = conn.cursor()

@app.route("/store", methods=["POST"])
def store():
    product_name = request.get_json()
    product_price = request.get_json()
    if product_name and product_price:
        if "name" in product_name and "price" in product_price:
            if product_name["name"] and product_price["price"]:
                product_name_value = product_name["name"]
                product_price_value = product_price["price"]
                if product_price_value.isdigit() == True:
                    sql = f"insert into product values ('{product_name_value}','{product_price_value}')"
                    cur.execute(sql)
                    conn.commit()
                    return {"success":"store_finish"}
                else:
                    return {"type_error":"price_only_integer"}
            else:
                return {"value_error":"not_found_value"}
        else:
            return {"key_error":"key : name, price"}
    else:
        return {"data_error":"no_data"}

app.run(host="0.0.0.0", port=8080, debug=True)