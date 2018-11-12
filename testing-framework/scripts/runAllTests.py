import os
import sys
import subprocess

ls_output = subprocess.check_output("ls ../testCaseExecutables/", shell = True)
test_files = ls_output.split()

os.system("date >> ../temp/output.log")

for test_file_name in test_files:
    os.system("echo \"\" >> ../temp/output.log")
    subprocess.check_output("python -W ignore ../testCaseExecutables/" + test_file_name + " 2>> ../temp/output.log", shell=True)