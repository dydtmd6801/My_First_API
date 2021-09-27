from logging import debug
from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['post'])
def test():
    return {"reuslt" : "test_success"}

# github

app.run(host='0.0.0.0', port=8080, debug=True)