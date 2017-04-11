#!/usr/bin/env python

#from __future__ import print_function
#from future.standard_library import install_aliases
#install_aliases()

#from urllib.parse import urlparse, urlencode
#from urllib.request import urlopen, Request
#from urllib.error import HTTPError

import json
import os
import ast

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json() # removed str
    #ret = json.loads(ast.literal_eval(req))
    #ret['result']['fulfillment'] = {"messages" : [{u'speech': u'HELLO THERE, WE MADE IT!', u'type': 0}], u'speech': u'HURRAY! WE MADE IT!'}
    #ret = make_response(json.dumps(ret))
    #print(ret)
    return ret2


if __name__ == "__main__":
	app.run()
