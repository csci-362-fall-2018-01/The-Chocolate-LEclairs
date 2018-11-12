import unittest

import time
import datetime
import jarabe.intro.agepicker as agepick

class TestAgeCalculation(unittest.TestCase):
	def test_age_calc(self):
		date = ""
		age = ""
		count = 0

		for line in open("../testCases/age_calculator_invalid.txt"):
			l = line.strip()
			if not l.startswith("#"):
				if count == 0:
					date = l.rstrip()
					count = 1
				elif count == 1:
					age = l.rstrip()
					count = 0
					unix = time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())
					out = agepick.calculate_age(unix)
					self.assertNotEqual(int(age), out)

if __name__ == '__main__':
	unittest.main()
