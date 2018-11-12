import os
import subprocess

os.system("date >> ../temp/output.log")

test_file_name = raw_input()
os.system("echo \"\" >> ../temp/output.log")
subprocess.check_output("python -W ignore ../testCaseExecutables/" + test_file_name + " 2>> ../temp/output.log", shell=True)