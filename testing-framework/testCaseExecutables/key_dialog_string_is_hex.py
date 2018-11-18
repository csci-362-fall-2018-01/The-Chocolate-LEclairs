import unittest
import os
import jarabe.desktop.keydialog as key

class TestStringIsHex(unittest.TestCase):
    def test_add_object(self):
        for line in open("../testCases/key_dialog_string_is_hex.txt"):
	    line = line.strip()
            if not line.startswith("#") and not line == "":
                self.assertEquals(key.string_is_hex(line[:line.index(",")]), line[line.index(",") + 1:] == "True")

if __name__ == '__main__':
    unittest.main()
