import subprocess

test_file_name = raw_input()
output = subprocess.check_output("python ../testCaseExecutables/" + test_file_name, shell=True)
print(output)