import unittest
import os
import jarabe.model.buddy as bud

class TestChangingNickname(unittest.TestCase):
    os.system("echo \"Testing Buddy Color Change with Valid Input\" >> ../temp/output.log")

    def test_nick_change(self):
        for line in open("../testCases/buddy_color.txt"):
            if not line.startswith("#"):
                me = bud.BaseBuddyModel()
                me.set_color(line)
                self.assertEquals(line, me.get_color())

if __name__ == '__main__':
	unittest.main()
