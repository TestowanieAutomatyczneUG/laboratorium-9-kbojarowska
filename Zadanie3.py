from unittest.mock import *
from unittest import TestCase, main

class Environment:
    def __init__(self):
        self.played = False

    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self):
        self.played = True

    def resetWav(self):
        self.played = False


class Checker:
    def __init__(self):
        self.environment = Environment()

    def reminder(self, file):
        time = self.environment.getTime()
        if time >= 17:
            self.environment.playWavFile(file)
            self.environment.wavWasPlayed()
        else:
            self.environment.resetWav()

class TestChecker(TestCase):
    def setUp(self):
        self.checker = Checker()

    def test_checker_play_after_17(self):
        file = 'file.wav'
        self.checker.environment.getTime = Mock('getTime')
        self.checker.environment.getTime.return_value = 20
        self.checker.reminder(file)
        self.assertEqual(self.checker.environment.played, True)

    def test_checker_do_not_play_before_17(self):
        file = 'file.wav'
        self.checker.environment.getTime = Mock('getTime')
        self.checker.environment.getTime.return_value = 8
        self.checker.reminder(file)
        self.assertEqual(self.checker.environment.played, False)

    def tearDown(self):
        self.test_checker = None


if __name__ == '__main__':
    main()