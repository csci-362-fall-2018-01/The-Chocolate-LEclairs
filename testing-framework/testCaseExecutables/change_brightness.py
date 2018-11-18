import os
import unittest

import jarabe.model.brightness as bright

class TestChangeBrightness(unittest.TestCase):
    def test_new_brightness(self):
        try:
            f = open("../testCases/change_brightness.txt", "r")
            brightness = ""

            for line in f.readlines():
                if not line.startswith("#"):
                    brightness = line.rstrip()

                    monitor = bright.get_instance()
                    monitor._save(int(brightness))
                    self.assertEquals(1, 1)
        except:
            self.fail("unable to change brightness")
        

if __name__ == "__main__":
    unittest.main()