from unittest import TestCase
from arrays_and_strings import StringQuestions


class TestStringQuestions(TestCase):
    def test1_hasRepeatCharacters(self):
        self.assertTrue(StringQuestions.hasRepeatCharacters("bolo"))

    def test2_hasRepeatCharacters(self):
        self.assertFalse(StringQuestions.hasRepeatCharacters("bola"))

    def test3_hasRepeatCharacters(self):
        self.assertFalse(StringQuestions.hasRepeatCharacters(""))

    def test1_hasRepeatCharactersSpace(self):
        self.assertTrue(StringQuestions.hasRepeatCharacters("bolo", space_efficient=True))

    def test2_hasRepeatCharactersSpace(self):
        self.assertFalse(StringQuestions.hasRepeatCharacters("bola", space_efficient=True))

    def test3_hasRepeatCharactersSpace(self):
        self.assertFalse(StringQuestions.hasRepeatCharacters("", space_efficient=True))