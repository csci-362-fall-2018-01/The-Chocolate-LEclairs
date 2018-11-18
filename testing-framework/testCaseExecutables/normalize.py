import unittest
import codecs

import jarabe.util.normalize as normalize

class Normalize(unittest.TestCase):
    def test_normalize(self):
        for line in codecs.open("../testCases/normalize.txt", "r", "utf-8"):
            if not line.startswith("#"):
                before = line[:line.index(",")]
                after = line[line.index(",") + 1:-1]
                self.assertEquals(normalize.normalize_string(before), after)

if __name__ == '__main__':
    unittest.main()