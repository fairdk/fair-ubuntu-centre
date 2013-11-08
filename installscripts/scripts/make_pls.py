#!/usr/bin/python
import os
PATH = os.path.abspath(os.path.split(__file__)[0])
txt = open(os.path.join(PATH,"pls.template")).read()
if __name__ == "__main__":

    for filename in os.listdir(os.getcwd()):
        if filename[-3:] == "iso":
            pls_content = txt.replace("%FILENAME%", filename)
            f = open(filename[:-3]+"pls", "w")
            f.write(pls_content)
            f.close()

