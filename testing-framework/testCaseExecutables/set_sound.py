import os
import unittest

import jarabe.model.sound as sound

class TestSoundSettings(unittest.TestCase):
    def setUp(self):
        self._newVolume = 0
        self._newMuted = None

        f = open("../testCases/set_sound.txt", "r")
        for line in f.readlines():
            if not line.startswith("#"):
                if self._newVolume == 0:
                    self._newVolume = int(line.rstrip())
                else:
                    self._newMuted = bool(line.rstrip())

    def test_change_volume(self):
        manager = sound.PlaybackSound()
        manager.set_volume(self._newVolume)
        self.assertEquals(self._newVolume, manager.get_volume())

    def test_change_mute(self):
        manager = sound.PlaybackSound()
        manager.set_muted(self._newMuted)
        self.assertEquals(self._newMuted, manager.get_muted())

if __name__ == "__main__":
    unittest.main()
