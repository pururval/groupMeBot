# based on https://github.com/apnorton/apnorton-demo-bot

import os
import json
import datetime

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if (data['name'] != 'apnorton' and (data['text'] =='who is on duty' or data['text'] =='Who is on duty' or data['text'] =='Who\'s on duty' or data['text'] =='who\'s on duty')):
    # msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    msg = getName()
    send_message(msg)

  return "ok", 200


def getName():
    x = datetime.datetime.now()
    today = x.strftime("%m") +"." + x.strftime("%d")+ "." + x.strftime("%y")
    data = [["A", "09.03.18"],["C and D", "09.03.18"],["E and F", "09.05.18"]];
    p = []

    for d in range(len(data)):
        if(data[d][1]==today):
            p.append([data[d][0]])

        if(len(p)==2):
            retval = ''.join(p[0])
            retval += ''.join(" and ")
            retval += ''.join(p[1])
            return retval
    return "idk"

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
