import unittest
from Sastrawi.Stemmer.Context.Visitor.AbstractDisambiguatePrefixRule import AbstractDisambiguatePrefixRule
from Sastrawi.Stemmer.Context.Removal import Removal


class MockDisambiguator:
    def __init__(self, result):
        self.result = result

    def disambiguate(self, word):
        return self.result


class MockDictionary:
    def __init__(self, words=None):
        self.words = set(words or [])

    def contains(self, word):
        return word in self.words


class MockContext:
    def __init__(self, word, dictionary=None):
        self.current_word = word
        self.dictionary = dictionary or MockDictionary()
        self.removals = []

    def add_removal(self, removal):
        self.removals.append(removal)


class TestAbstractDisambiguatePrefixRule(unittest.TestCase):
    def test_disambiguate_matching_word_in_dict(self):
        rule = AbstractDisambiguatePrefixRule()
        rule.add_disambiguator(MockDisambiguator('jalan'))
        ctx = MockContext('berjalan', MockDictionary(['jalan']))
        rule.visit(ctx)
        self.assertEqual(1, len(ctx.removals))
        self.assertEqual('DP', ctx.removals[0].get_affix_type())
        self.assertEqual('jalan', ctx.current_word)

    def test_disambiguate_result_not_in_dict_uses_last_result(self):
        rule = AbstractDisambiguatePrefixRule()
        rule.add_disambiguator(MockDisambiguator('jalan'))
        ctx = MockContext('berjalan', MockDictionary(['beri']))
        rule.visit(ctx)
        self.assertEqual(1, len(ctx.removals))
        self.assertEqual('jalan', ctx.current_word)

    def test_disambiguate_none_result_does_nothing(self):
        rule = AbstractDisambiguatePrefixRule()
        rule.add_disambiguator(MockDisambiguator(None))
        ctx = MockContext('berjalan', MockDictionary(['jalan']))
        rule.visit(ctx)
        self.assertEqual(0, len(ctx.removals))
        self.assertEqual('berjalan', ctx.current_word)

    def test_add_disambiguators(self):
        rule = AbstractDisambiguatePrefixRule()
        rule.add_disambiguators([MockDisambiguator('a'), MockDisambiguator('b')])
        self.assertEqual(2, len(rule.disambiguators))

    def test_first_matching_word_in_dict_wins(self):
        rule = AbstractDisambiguatePrefixRule()
        rule.add_disambiguator(MockDisambiguator('result1'))
        rule.add_disambiguator(MockDisambiguator('result2'))
        ctx = MockContext('berjalan', MockDictionary(['result2']))
        rule.visit(ctx)
        self.assertEqual('result2', ctx.current_word)


if __name__ == '__main__':
    unittest.main()
