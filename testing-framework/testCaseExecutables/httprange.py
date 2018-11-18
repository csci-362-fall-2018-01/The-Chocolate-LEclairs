import unittest

import jarabe.util.httprange as httprange

class TestHTTPRange(unittest.TestCase):
    def test_open(self):
        for line in open("../testCases/httprange.txt"):
            if not line.startswith("#"):
                url = line[:line.index(",")]
                try:
                    hr = httprange.open(url)
                    self.assertEquals(1, 1)
                except:
                    self.fail()

    def test_size(self):
        for line in open("../testCases/httprange.txt"):
            if not line.startswith("#"):
                url = line[:line.index(",")]
                size = line[line.index(",") + 1:-1]
                try:
                    hr = httprange.open(url)
                    self.assertEquals(int(hr.size()), int(size))
                except:
                    self.fail()

if __name__ == '__main__':
    unittest.main()