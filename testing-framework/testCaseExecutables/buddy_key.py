import unittest
import os
import jarabe.model.buddy as bud

class TestChangingNickname(unittest.TestCase):
    os.system("echo \"Testing Buddy Key Change with Valid Input\" >> ../temp/output.log")

    def test_nick_change(self):
        for line in open("../testCases/buddy_key.txt"):
            if not line.startswith("#"):
                me = bud.BaseBuddyModel()
                me.set_key(line)
                self.assertEquals(line, me.get_key())

if __name__ == '__main__':
	unittest.main()
