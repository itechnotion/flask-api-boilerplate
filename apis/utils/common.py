from flask import make_response, jsonify

def output_json(data,message,status=True,code=200,headers=None):
    datares=jsonify(data=data,status=status,message=message)
    resp = make_response(datares, code)
    resp.headers.extend(headers or {})
    return resp