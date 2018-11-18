import unittest
import os
import jarabe.desktop.keydialog as key

class TestStringIsAscii(unittest.TestCase):
    def test_string_is_ascii(self):
        for line in open("../testCases/key_dialog_string_is_hex.txt"):
	    line = line.strip()
            if not line.startswith("#") and not line == "":
		try:
                    self.assertEquals(key.string_is_ascii(line[:line.index(",")]), line[line.index(",") + 1:] == "True")
		except:
		    self.assertEquals(False, line[line.index(",") + 1:] == "True")

if __name__ == '__main__':
    unittest.main()
