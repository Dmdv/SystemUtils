import os

__author__ = 'Dyachkov'

import string

def run(program, *args):
    # find executable
    for path in os.environ["PATH"].split(os.pathsep):
        file = os.path.join(path, program) + ".exe"
        if os.path.exists(file) :
            print (file)
        # try:

        #    return os.spawnv(os.P_WAIT, file, (file,) + args)
        #except os.error:
        #    pass
    raise (os.error, "cannot find executable")

run("python", "hello.py")
print ("")