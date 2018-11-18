import os
import time
import random
import unittest

import jarabe.desktop.schoolserver as server

class TestSerialGenerator(unittest.TestCase):
    def test_serial_number_gen(self):
        f = open("../testCases/serial_number.txt", "r")

        seed = 0
        key = ""
        for line in f.readlines():
            if not line.startswith("#"):
                if seed == 0:
                    seed = int(line.rstrip())
                else:
                    key = line.rstrip()
                    unix_time = str(int(time.time()))[-8:]

                    random.seed(seed)
                    gen_key = server._generate_serial_number()

                    self.assertEquals(gen_key, key + unix_time)

if __name__ == "__main__":
    unittest.main()
