import os
import sys
import subprocess

ls_output = subprocess.check_output("ls ../testCaseExecutables/", shell = True)
test_files = ls_output.split()

os.system("mv ../temp/output.log ../temp/output2.log")
os.system("date >> ../temp/output.log")

for test_file_name in test_files:
    os.system("echo \"\" >> ../temp/output.log")
    subprocess.check_output("python -W ignore ../testCaseExecutables/" + test_file_name + " 2>> ../temp/output.log", shell=True)

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