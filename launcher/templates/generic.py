import sys


def injected (args):
    #$CODE$

def parse_args(args):
    try:
        str=args[2:len(sys.argv[1])-1]
        return str.replace("'", "").split(", ")
    except:
        return None


if __name__ == "__main__":

    if len(sys.argv) > 1:
        print (injected(parse_args(sys.argv[1])))
    else:
        print (injected (None))

