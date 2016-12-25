from unittest import TestCase
from arrays_and_strings import StringQuestions


class TestStringQuestions(TestCase):
    def test1_hasRepeatCharacters(self):
        self.assertTrue(StringQuestions.hasRepeatCharacters("bolo"))

    def test2_hasRepeatCharacters(self):
        self.assertFalse(StringQuestions.hasRepeatCharacters("bola"))

    def test3_hasRepeatCharacters(self):
        self.assertFalse(StringQuestions.hasRepeatCharacters(""))