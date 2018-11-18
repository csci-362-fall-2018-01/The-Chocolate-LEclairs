import os
import unittest

import jarabe.journal.expandedentry as entry

class TestJournalEntryComment(unittest.TestCase):
    def test_comment_entry(self):
        f = open("../testCases/journal_comment.txt")

        name = ""
        message = ""
        color = ""

        try:
            for line in f.readlines():
                if not line.startswith("#"):
                    if name == "":
                        name = line
                    elif message == "":
                        message = line
                    else:
                        color = line

                        commentView = entry.CommentsView()
                        commentView._add_row(name, message, "", color)
                    
                        pass
        except:
            self.fail("unable to add comment")

if __name__ == "__main__":
    unittest.main()