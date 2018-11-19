import os
import unittest

import jarabe.model.buddy as buddy
import jarabe.model.friends as friend

class TestGiveNewFriend(unittest.TestCase):
    # Read in the inputs from the text file
    def setUp(self):
        self._buddyName = ""
        self._buddyKey = ""

        f = open("../testCases/new_friend.txt", "r")
        for line in f.readlines():
            if not line.startswith("#"):
                if self._buddyName == "":
                    self._buddyName = line.rstrip()
                else:
                    self._buddyKey = line.rstrip()

    # test initializing the Friend object
    def test_get_model(self):
        try:
            friendModel = friend.get_model()
            self.assertIsNotNone(friendModel)
        except:
            self.fail("unable to get friend model")

    # test adding a new friend
    def test_add_friend(self):
        try:
            newBuddy = buddy.BaseBuddyModel()
            newBuddy.set_nick(self._buddyName)
            newBuddy.set_key(self._buddyKey)
            friend.get_model().add_friend(newBuddy)
            pass
        except:
            self.fail("unable to add buddy")
    
    # after adding a friend, make sure that the friend can be found
    def test_has_friend(self):
        try:
            newBuddy = buddy.BaseBuddyModel()
            newBuddy.set_nick(self._buddyName)
            newBuddy.set_key(self._buddyKey)
            friend.get_model().add_friend(newBuddy)

            hasFriend = friend.get_model().has_buddy(newBuddy)
            self.assertTrue(hasFriend)
        except:
            self.fail("unable to check for buddy")

if __name__ == "__main__":
    unittest.main()