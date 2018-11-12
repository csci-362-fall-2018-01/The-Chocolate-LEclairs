import subprocess

test_file_name = raw_input()
subprocess.check_output("python -W ignore ../testCaseExecutables/" + test_file_name + " 2>> ../temp/output.log", shell=True)