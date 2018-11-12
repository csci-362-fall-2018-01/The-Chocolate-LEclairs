import os
import subprocess

ls_output = subprocess.check_output("ls ../testCaseExecutables/", shell = True)
test_files = ls_output.split()

for test_file_name in test_files:
    output = subprocess.check_output("python ../testCaseExecutables/" + test_file_name, shell=True)
    print(output)