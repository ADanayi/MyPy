import urllib.request
import json
from base64 import b64encode

def __ready_json(req):
    if type(req) == dict:
        req = str(json.dumps(req))
    if type(req) == str:
        req = req.encode('utf-8')
    return req

def __add_basic_auth(req, username, password):
    user_pass = "{}:{}".format(username, password)
    user_pass_b = user_pass.encode()
    user_pass_e = b64encode(user_pass_b).decode('ascii')
    req.add_header('Authorization', "Basic {}".format(user_pass_e))

def __create_request(url, json, user_agent='Mozilla/5.0'):
    req = urllib.request.Request(url, json)
    req.add_header('content-type', 'application/json')
    req.add_header('User-Agent', user_agent)
    return req

def __fetch_response(req, timeout):
    response = urllib.request.urlopen(req, timeout=timeout)
    resp = json.loads(response.read())
    return resp

def j2j(url, req_json, timeout=10):
    json = __ready_json(req_json)
    # print(type(json), json)
    req = __create_request(url, json)
    resp = __fetch_response(req, timeout)
    return resp

def j2j_auth_basic(url, req_json, user_name, password, timeout=10):
    json = __ready_json(req_json)
    req = __create_request(url, json)
    __add_basic_auth(req, user_name, password)
    resp = __fetch_response(req, timeout)
    return resp
