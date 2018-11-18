import os
import unittest

import jarabe.model.speech as speech

class TestSpeechManager(unittest.TestCase):
    def test_speech_manager(self):
        try:
            manager = speech.get_speech_manager()
            self.assertIsNotNone(manager)
        except:
            self.fail("speech manager could not be created")

if __name__ == "__main__":
    unittest.main()