# -*- coding:utf-8 -*-
from flask import abort, jsonify, Flask, request, Response
import json
app = Flask(__name__)
success = {
    "error_code": 0,
    "error_msg": "success",
    "result": "0xabc"
}
error = {
    "error_code": 1,
    "error_msg": "params is not correctly",
    "result": ""
}

@app.route("/handle_data", methods=['POST'])
def handle_data():
    body = trans(request.get_data())
    if not body.get("method") in ["base16","base32","base58","base64"]:
        return error
    if body.get("payload") == None:
        return error
    return success

'''pretty json '''
def trans(payload):
    try:
        return json.loads(str(payload, "utf-8"))    
        # return json.dumps(a_json, sort_keys=True, indent=4, separators=(',', ':'))
    except:
        print("error when parsing payload")
        return payload
    
if __name__ == "__main__":
    app.run(host = "127.0.0.1",port = 6660,debug = True)
