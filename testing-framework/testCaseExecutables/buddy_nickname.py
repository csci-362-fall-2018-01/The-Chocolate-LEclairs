import unittest

import jarabe.model.buddy as bud

class TestChangingNickname(unittest.TestCase):
    def test_nick_change(self):
        for line in open("../testCases/buddy_nickname.txt"):
            if not line.startswith("#"):
                me = bud.BaseBuddyModel()
                me.set_nick(line)
                self.assertEquals(line, me.get_nick())

if __name__ == '__main__':
	unittest.main()
