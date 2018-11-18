import unittest

import jarabe.util.httprange as httprange

class TestHTTPRange(unittest.TestCase):
    def test_size(self):
        for line in open("../testCases/httprange.txt"):
            if not line.startswith("#"):
                url = line[:line.index(",")]
                size = line[line.index(",") + 1:-1]
                hr = httprange.open(url)
                self.assertEqual(int(hr.size()), int(size))

if __name__ == '__main__':
    unittest.main()