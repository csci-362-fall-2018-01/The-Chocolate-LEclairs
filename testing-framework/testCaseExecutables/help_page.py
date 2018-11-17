import unittest
import os

import jarabe.view.viewhelp as help

class TestAlerts(unittest.TestCase):
    def test_show_alert(self):
        social_help = help.get_social_help_server()
        self.assertNotEquals(social_help, None)

if __name__ == '__main__':
	unittest.main()