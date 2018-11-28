import os
import sys
import subprocess

output = subprocess.check_output("ls break/", shell = True).split()

for directory in output:
    output_2 = subprocess.check_output("ls break/" + directory + "/*.py", shell = True).split()
    for file_name in output_2:
        subprocess.check_output("python -m py_compile " + file_name, shell=True)
        
os.system("cp -R ./break/* /usr/local/lib/python2.7/dist-packages/jarabe/")