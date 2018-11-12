## Test Gender Picker

import unittest
import jarabe.intro.genderpicker as genderpick

class testGenderPicker(unittest.TestCase):
    def testGender(self):
        person = genderpick.GenderPicker()
        inFile = open("../testCases/genderPicker.txt", "r")

        test = ""

        for line in inFile:
            if line == "male":
                person.set_gender("male")
            else:
                person.set_gender("female")

            test = person.get_gender()

            print(line + ": " + test == line) 

if __name__ == '__main__':
    unittest.main()
                

        
