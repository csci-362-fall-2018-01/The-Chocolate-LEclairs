import unittest
import subprocess

import jarabe.model.session as session

class TestSession(unittest.TestCase):
    def test_have_systemd(self):
        for line in open("../testCases/session.txt"):
            line = line.strip()
            if not line == "#" and not line == "":
                self.assertEquals(session.have_systemd(), subprocess.check_output("ls /run/systemd/ | grep seats", shell=True) == "seats\n")

    def test_get_session_manager(self):
        for line in open("../testCases/session.txt"):
            line = line.strip()
            if not line == "#" and not line == "":
                try:
                    session.get_session_manager()
                    self.assertEquals(1, 1)
                except:
                    self.fail()

if __name__ == '__main__':
    unittest.main()