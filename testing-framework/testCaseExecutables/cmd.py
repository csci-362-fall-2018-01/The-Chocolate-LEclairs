import unittest
import sys
import os

import jarabe.controlpanel.cmd as cmd

class TestCMD(unittest.TestCase):
    def test_cmd_help(self):
        cmd_help_lines = [
            'Usage: sugar-control-panel [ option ] key [ args ... ] \n',
            '    Control for the sugar environment. \n',
            '    Options: \n',
            '    -h           show this help message and exit \n',
            '    -l           list all the available options \n',
            '    -h key       show information about this key \n',
            '    -g key       get the current value of the key \n',
            '    -s key       set the current value for the key \n',
            '    -c key       clear the current value for the key \n',
            '    \n'
        ]

        for line in open("../testCases/cmd.txt"):
            if not line.startswith("#"):
                sys.stdout = open("./temp.txt", "w")
                cmd.cmd_help()
                sys.stdout = sys.__stdout__
                count = 0
                for line in open("./temp.txt"):
                    if line == "" or line == "\n" or line == cmd_help_lines[count]:
                        self.assertEquals(1, 1)
                    else:
                        self.assertEquals(1, 2)
                    count += 1
                os.system("rm ./temp.txt")

    def test_note_restart(self):
        note_restart_lines = [
            'To apply your changes you have to restart Sugar.\n',
            'Hit ctrl+alt+erase on the keyboard to trigger a restart.\n'
        ]

        for line in open("../testCases/cmd.txt"):
            if not line.startswith("#"):
                sys.stdout = open("./temp.txt", "w")
                cmd.note_restart()
                sys.stdout = sys.__stdout__
                count = 0
                for line in open("./temp.txt"):
                    if line == "" or line == "\n" or line == note_restart_lines[count]:
                        self.assertEquals(1, 1)
                    else:
                        self.assertEquals(1, 2)
                    count += 1
                os.system("rm ./temp.txt")

if __name__ == '__main__':
    unittest.main()