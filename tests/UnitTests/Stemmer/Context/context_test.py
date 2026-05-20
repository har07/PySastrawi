import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Context.Context import Context
from Sastrawi.Stemmer.Context.Visitor.VisitorProvider import VisitorProvider


class TestContext(unittest.TestCase):
    def setUp(self):
        self.visitor_provider = VisitorProvider()

    def _make_context(self, word, dictionary):
        return Context(word, dictionary, self.visitor_provider)

    def test_word_in_dictionary_returns_immediately(self):
        """Step 1: if word in dictionary, it stays unchanged."""
        dictionary = ArrayDictionary(['makan'])
        ctx = self._make_context('makan', dictionary)
        ctx.execute()
        self.assertEqual('makan', ctx.result)

    def test_short_word_not_in_dict_returns_original(self):
        """Words <=3 chars that aren't in the dictionary return as-is."""
        dictionary = ArrayDictionary([])
        ctx = self._make_context('mei', dictionary)
        ctx.execute()
        self.assertEqual('mei', ctx.result)

    def test_inflectional_particle_removal(self):
        """hancurlah -> hancur"""
        dictionary = ArrayDictionary(['hancur'])
        ctx = self._make_context('hancurlah', dictionary)
        ctx.execute()
        self.assertEqual('hancur', ctx.result)

    def test_possessive_pronoun_removal(self):
        """jubahku -> jubah"""
        dictionary = ArrayDictionary(['jubah'])
        ctx = self._make_context('jubahku', dictionary)
        ctx.execute()
        self.assertEqual('jubah', ctx.result)

    def test_derivational_suffix_removal(self):
        """belikan -> beli"""
        dictionary = ArrayDictionary(['beli'])
        ctx = self._make_context('belikan', dictionary)
        ctx.execute()
        self.assertEqual('beli', ctx.result)

    def test_plain_prefix_di_removal(self):
        """dibuang -> buang"""
        dictionary = ArrayDictionary(['buang'])
        ctx = self._make_context('dibuang', dictionary)
        ctx.execute()
        self.assertEqual('buang', ctx.result)

    def test_ber_prefix_rule_1b(self):
        """berambut -> rambut (Rule 1b: berV -> be-rV)"""
        dictionary = ArrayDictionary(['rambut'])
        ctx = self._make_context('berambut', dictionary)
        ctx.execute()
        self.assertEqual('rambut', ctx.result)

    def test_meng_prefix_rule_16(self):
        """menggila -> gila"""
        dictionary = ArrayDictionary(['gila'])
        ctx = self._make_context('menggila', dictionary)
        ctx.execute()
        self.assertEqual('gila', ctx.result)

    def test_meng_prefix_rule_17b(self):
        """mengupas -> kupas"""
        dictionary = ArrayDictionary(['kupas'])
        ctx = self._make_context('mengupas', dictionary)
        ctx.execute()
        self.assertEqual('kupas', ctx.result)

    def test_meny_prefix_rule_18(self):
        """menyuarakan -> suara"""
        dictionary = ArrayDictionary(['suara'])
        ctx = self._make_context('menyuarakan', dictionary)
        ctx.execute()
        self.assertEqual('suara', ctx.result)

    def test_mem_prefix_rule_11(self):
        """membangun -> bangun"""
        dictionary = ArrayDictionary(['bangun'])
        ctx = self._make_context('membangun', dictionary)
        ctx.execute()
        self.assertEqual('bangun', ctx.result)

    def test_per_prefix_rule_21(self):
        """perumahan -> rumah"""
        dictionary = ArrayDictionary(['rumah'])
        ctx = self._make_context('perumahan', dictionary)
        ctx.execute()
        self.assertEqual('rumah', ctx.result)

    def test_pem_prefix_rule_26(self):
        """peminum -> minum"""
        dictionary = ArrayDictionary(['minum'])
        ctx = self._make_context('peminum', dictionary)
        ctx.execute()
        self.assertEqual('minum', ctx.result)

    def test_ter_prefix_rule_6b(self):
        """teraup -> raup (Rule 6b: terV -> te-rV)"""
        dictionary = ArrayDictionary(['raup'])
        ctx = self._make_context('teraup', dictionary)
        ctx.execute()
        self.assertEqual('raup', ctx.result)

    def test_not_found_returns_original(self):
        """If no stemming succeeds, return the original word."""
        dictionary = ArrayDictionary([])
        ctx = self._make_context('xyzabc', dictionary)
        ctx.execute()
        self.assertEqual('xyzabc', ctx.result)

    def test_recursive_prefix_removal(self):
        """memberdayakan -> daya (multi-layer prefix removal)"""
        dictionary = ArrayDictionary(['daya'])
        ctx = self._make_context('memberdayakan', dictionary)
        ctx.execute()
        self.assertEqual('daya', ctx.result)

    def test_removals_accumulate(self):
        """Removals list should be populated during stemming."""
        dictionary = ArrayDictionary(['hancur'])
        ctx = self._make_context('hancurlah', dictionary)
        ctx.execute()
        self.assertGreater(len(ctx.removals), 0)

    def test_is_suffix_removal(self):
        from Sastrawi.Stemmer.Context.Removal import Removal
        dictionary = ArrayDictionary([])
        ctx = self._make_context('test', dictionary)
        removal = Removal(None, 'test', 'result', 'removed', 'DS')
        self.assertTrue(ctx.is_suffix_removal(removal))


if __name__ == '__main__':
    unittest.main()
