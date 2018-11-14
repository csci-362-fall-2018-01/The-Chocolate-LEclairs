import os
import sys
import datetime
import subprocess

# Open the log file and gather lines for the previous test run
f = open("../temp/output.log")
lines = []
for line in f.readlines():
    if not line.startswith("\n"):
        if "^^^" in line:
            break
        lines.append(line.rstrip())

f.close()

# Create report file named based on time
filename = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M.html")
os.system("touch ../reports/" + filename)

report = open("../reports/" + filename, "w+")

# Create heading
report.write(
    "<!DOCTYPE html>\n"
    "<html>\n"
    "<head>\n"
    "\t<title>TCL - Test Report</title>\n"
    "</head>\n\n"
    "<body>\n"
    "\t<h1>The Chocolate LEclairs</h1>\n"
    "\tTeam Members: Blaine Billings, Alex Skiff, Chase Myers, Justin Willis, Carson Barber\n\t<br><br>\n"
    "\t<h2>Test Report</h2>\n"
    "\tGenerated: " + lines[0] + "\n\n"
)

# Gather input and output data to report
dateLine = True
for line in lines:
    if dateLine == True:
        dateLine = False
        continue

    if line.startswith("Testing "):
        report.write("<br><br>\n\n")
        cur_file = line[8:line.find(".py...")]

        cur_lines = open("../testCases/" + cur_file + ".txt").readlines()
        firstInput = True
        testCaseName = True

        for c_line in cur_lines:
            if c_line.startswith("#"):
                if testCaseName == True:
                    testCaseName = False
                    report.write(
                        "\t<h2>" + c_line[2:len(c_line)-1].rstrip() + "</h2>\n"
                    )
                else:
                    report.write(
                        "\t" + c_line[2:len(c_line)-1].rstrip() + "<br>\n"
                    )
            else:
                if firstInput == True:
                    report.write(
                     "\n\tTest Case Inputs:<br>\n"
                    )
                    firstInput = False
                report.write(
                    "\t     - " + c_line.rstrip() + "<br>\n"
                )
        report.write(
            "\n\t<br>Test Results:<br>\n"
        )
    else:
        report.write(
            "\t<strong>     - " + line + "</strong>\n"
        )
    
# Create html closing
report.write(
    "</body>\n"
    "</html>"
)

report.close()

# Open report
os.system("xdg-open ../reports/" + filename)
