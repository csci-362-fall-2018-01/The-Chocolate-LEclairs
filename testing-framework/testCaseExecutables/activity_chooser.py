import unittest
import jarabe.desktop.activitychooser as activity
import time
import datetime
import os

class TestActivityChooser(unittest.TestCase):
    def test_activity_chooser(self):
        input_file = open("../testCases/activity_chooser.txt", "r")

        title = ""
        for line in input_file:
            if not line.startswith("#"):
                title = line.rstrip()

                chooser = activity.ActivityChooser()
                chooser.set_title(title)

                self.assertIsNotNone(chooser)		

if __name__ == '__main__':
	unittest.main()
