from unittest import TestCase
from .string_questions import StringQuestions


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

    def test1_checkPermutations(self):
        self.assertTrue(StringQuestions.checkPermutation("bob", "bbo"))

    def test2_checkPermutations(self):
        self.assertFalse(StringQuestions.checkPermutation("obb", "oob"))

    def test3_checkPermutations(self):
        self.assertFalse(StringQuestions.checkPermutation("bob", "bobs"))

    def test1_urlify(self):
        self.assertEqual(StringQuestions.urlify(['b', ' ', 'b', ' ', ' '], 5),
                         ['b', '%', '2', '0', 'b'])

    def test2_urlify(self):
        self.assertEqual(StringQuestions.urlify(['b', ' ', ' ', 'b', ' ', ' ', ' ', ' '], 8),
                         ['b', '%', '2', '0', '%', '2', '0', 'b'])
