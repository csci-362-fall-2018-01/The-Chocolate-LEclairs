import os
import sys
import subprocess

ls_output = subprocess.check_output("ls ../testCaseExecutables/", shell = True)
test_files = ls_output.split()

os.system("touch ../temp/output.log")
os.system("mv ../temp/output.log ../temp/output2.log")
os.system("date >> ../temp/output.log")

for test_file_name in test_files:
    os.system("echo \"\" >> ../temp/output.log")
    os.system("echo Testing \"" + test_file_name + "\"... >> ../temp/output.log")
    os.system("python -W ignore ../testCaseExecutables/" + test_file_name + " 2>> ../temp/output.log")

f = open("../temp/output.log", "r")
lines = f.readlines()
f.close()

removenext = False
f = open("../temp/output.log", "w")
for line in lines:
    if not line.startswith(".") and not line.startswith("-"):
        if line.startswith("R"):
            removenext = True
            f.write(line)
        elif removenext == True:
            removenext = False
        else:
            f.write(line)
f.close()

moved_file = open("../temp/output2.log")

first_line = True
for line in moved_file:
    if first_line:
        os.system("echo \"\n\n\n\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" + line[:-1] + "\" >> ../temp/output.log")
    else:
        os.system("echo \"" + line[:-1] + "\" >> ../temp/output.log")
    first_line = False

moved_file.close()

os.system("rm ../temp/output2.log")

os.system("python genReport.py")
