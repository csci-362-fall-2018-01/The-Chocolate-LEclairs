import unittest
import jarabe.intro.agepicker as agepick
import time
import datetime

class TestAgeCalculation(unittest.TestCase):
	def test_age_calc(self):
		input_file = open("../testCases/age_calculator.txt", "r")

		read_input = 0
		date = 0
		age = 0
		for line in input_file:
			if not line[:1] == "#" and read_input == 0:
				read_input = 1
			if line == "\n":
				read_input = 0
			if read_input == 1:
				date = time.mktime(datetime.datetime.strptime(line[:-1], "%d/%m/%Y").timetuple())
				read_input = 2
			elif read_input == 2:
				age = int(line[:-1])
				print(str(agepick.calculate_age(date)) + " (Calculated) == " + str(age) + " (Expected)")
				self.assertTrue(agepick.calculate_age(date) == age)
				read_input = 1				

if __name__ == '__main__':
	unittest.main()
