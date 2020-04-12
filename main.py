#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request
from flask import make_response
import requests

try:
  from urllib.parse import urlparse
except:
  from urlparse import urlparse

app = Flask(__name__)

base_path = ''
key_prefix = "/bot"
telegram_api = "https://api.telegram.org"

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def home(path):
    if not request.full_path.startswith(key_prefix):
        return make_response("401 Unauthorized.", 401)
    method = request.method
    full_path = request.full_path
    url = telegram_api + full_path
    data = None if method.upper() == "GET" else request.form.to_dict()
    req = requests.request(method, url, data=data)
    return make_response(req.content, req.status_code)

def handler(environ, start_response):
    parsed_tuple = urlparse(environ['fc.request_uri'])
    li = parsed_tuple.path.split('/')
    global base_path
    if not base_path:
        base_path = "/".join(li[0:5])
    return app(environ, start_response)