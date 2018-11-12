# The-Chocolate-LEclairs
- Blaine Billings, Alex Skiff, Chase Myers, Justin Willis, Carson Barder

# Testing Framework Architecture
```
/testing-framework
	/sugar
		sugarlabs source files
	/scripts
		runAllTests.py
		runTest.py
	/testCases
		testCase1.txt
		testCase2.txt
		...
	/testCasesExecutables
		testCase1.py
		testCase2.py
		...
	/temp
		Output.log
	/docs
		README.md
	/reports
		testReport.html
```

# Test Case Format
Example test cases can be found in the testCases folder of the testing-framework.<br><br>
```
'#' represents a comment
each line that is not a comment should be treated as one parameter into the test case.
output from the test cases will be sent to output.log in /temp/ if run by the runAllTests.py script file
```