import os
import unittest
import hashlib

import jarabe.desktop.keydialog as key

class StringToHexTestCase(unittest.TestCase):
    def test_string_to_hex(self):
        f = open("../testCases/key_hex_converter.txt", "r")
        
        my_string = ""
        my_hex = ""

        for line in f.readlines():
            if not line.startswith("#"):
                if my_string == "":
                    my_string = line.rstrip()
                else:
                    my_hex = line.rstrip()
                    converted = key.string_to_hex(my_string)
                    self.assertEquals(converted, my_hex)

                    my_string = ""
                    my_hex = ""

if __name__ == "__main__":
    unittest.main()