import sys
import uuid
import os
from flask import Flask, request

app = Flask(__name__)

sys.path.append("../launcher")
from launcher import launcher

@app.route('/exec_code',methods=['POST'])
def exec_code():
    try:
        data = request.form
        strNewFileName = "../launcher/code/" + str (uuid.uuid4 ()) + ".txt"
        NewFile = open (strNewFileName, "w")
        NewFile.write (str(data['code']))
        NewFile.close () 
        args=["../launcher/templates/generic.py",strNewFileName]
        ret = launcher.Launch(args)
        os.remove (strNewFileName)
        return ret
    except:
        return "Error"