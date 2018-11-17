import unittest
import os
import cpsection.aboutme.model as about

class TestChangingNickname(unittest.TestCase):
    def test_nick_set(self):
        for line in open("../testCases/aboutme_nickname.txt"):
            if not line.startswith("#"):
                me = about.BaseBuddyModel()
                nick = line
                me.set_nick(line)
                self.assertEquals(line, me.get_nick())

if __name__ == '__main__':
    unittest.main()