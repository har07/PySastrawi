import unittest
from Sastrawi.Stemmer.Context.Visitor.DontStemShortWord import DontStemShortWord


class MockContext:
    def __init__(self):
        self.current_word = ''
        self.stopped = False

    def stopProcess(self):
        self.stopped = True


class TestDontStemShortWord(unittest.TestCase):
    def setUp(self):
        self.visitor = DontStemShortWord()

    def test_is_short_word_three_chars(self):
        self.assertTrue(self.visitor.is_short_word('abc'))

    def test_is_short_word_two_chars(self):
        self.assertTrue(self.visitor.is_short_word('ab'))

    def test_is_short_word_one_char(self):
        self.assertTrue(self.visitor.is_short_word('a'))

    def test_is_not_short_word_four_chars(self):
        self.assertFalse(self.visitor.is_short_word('abcd'))

    def test_visit_stops_for_short_word(self):
        ctx = MockContext()
        ctx.current_word = 'abc'
        self.visitor.visit(ctx)
        self.assertTrue(ctx.stopped)

    def test_visit_does_not_stop_for_long_word(self):
        ctx = MockContext()
        ctx.current_word = 'abcd'
        self.visitor.visit(ctx)
        self.assertFalse(ctx.stopped)


if __name__ == '__main__':
    unittest.main()
