import sys
import uuid
import os
import base64
from flask import Flask, request

app = Flask(__name__)

sys.path.append("../launcher")
from launcher import launcher

@app.route('/ping',methods=['POST','GET'])
def ping():
    return "pong"


@app.route('/exec_code',methods=['POST','GET'])
def exec_code():
    #try:
    data = request.form
    strNewFileName = "../launcher/code/" + str (uuid.uuid4 ()) + ".txt"
    #decode the code
    decoded_bytes = base64.b64decode(data['code'])
    original_string = decoded_bytes.decode('utf-8')
    NewFile = open (strNewFileName, "w")
    NewFile.write (original_string)
    NewFile.close () 
    args=["../launcher/templates/generic.py",strNewFileName,str(data['list_id']),str(data['item_id']) ]
    ret = launcher.Launch(args)
    #os.remove (strNewFileName)
    return ret
    #except:
    #    return "Error"