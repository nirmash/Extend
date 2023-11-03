import subprocess
import uuid

class launcher:
    def Launch(args: list[str]):
        #try:
        tplName = args [0]
        codeFile = args [1]
        print(args)
        #open the code file
        strCode = open (codeFile, "r").read ()
        #open the template file
        strTpl = open (tplName, "r").read ()
        #inject the code into the template
        strNew = strTpl.replace ("#$CODE$", strCode)
        #write the new file to the runtime directory
        strNewFileName = '../launcher/runtime/' + str (uuid.uuid4 ()) + ".py"
        NewFile = open (strNewFileName, "w")
        NewFile.write (strNew)
        NewFile.close () 
        #run the new file
        if len(args) < 3:
            ret = subprocess.run(["python3", strNewFileName], capture_output=True).stdout
        else:
            ret = subprocess.run(["python3", strNewFileName, str(args[2:])], capture_output=True).stdout
        #delete the new file
        #os.remove (strNewFileName)
        return ret
        #except:
        #    return "Error"