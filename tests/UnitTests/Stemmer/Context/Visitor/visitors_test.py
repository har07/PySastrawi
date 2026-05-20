import unittest
from Sastrawi.Stemmer.Context.Visitor.RemoveInflectionalParticle import RemoveInflectionalParticle
from Sastrawi.Stemmer.Context.Visitor.RemoveInflectionalPossessivePronoun import RemoveInflectionalPossessivePronoun
from Sastrawi.Stemmer.Context.Visitor.RemoveDerivationalSuffix import RemoveDerivationalSuffix
from Sastrawi.Stemmer.Context.Visitor.RemovePlainPrefix import RemovePlainPrefix


class MockContext:
    def __init__(self, word):
        self.current_word = word
        self.original_word = word
        self.process_is_stopped = False
        self.removals = []
        self.result = ''

    def add_removal(self, removal):
        self.removals.append(removal)

    def stopProcess(self):
        self.process_is_stopped = True


class TestRemoveInflectionalParticle(unittest.TestCase):
    def setUp(self):
        self.visitor = RemoveInflectionalParticle()

    def test_remove_lah(self):
        self.assertEqual('hancur', self.visitor.remove('hancurlah'))

    def test_remove_kah(self):
        self.assertEqual('benar', self.visitor.remove('benarkah'))

    def test_remove_tah(self):
        self.assertEqual('apa', self.visitor.remove('apatah'))

    def test_remove_pun(self):
        self.assertEqual('siapa', self.visitor.remove('siapapun'))

    def test_no_particle(self):
        self.assertEqual('kata', self.visitor.remove('kata'))

    def test_not_at_end(self):
        self.assertEqual('lahkan', self.visitor.remove('lahkan'))

    def test_visit_adds_removal(self):
        ctx = MockContext('hancurlah')
        self.visitor.visit(ctx)
        self.assertEqual(1, len(ctx.removals))
        self.assertEqual('P', ctx.removals[0].get_affix_type())
        self.assertEqual('hancur', ctx.current_word)

    def test_visit_no_change(self):
        ctx = MockContext('hancur')
        self.visitor.visit(ctx)
        self.assertEqual(0, len(ctx.removals))


class TestRemoveInflectionalPossessivePronoun(unittest.TestCase):
    def setUp(self):
        self.visitor = RemoveInflectionalPossessivePronoun()

    def test_remove_ku(self):
        self.assertEqual('jubah', self.visitor.remove('jubahku'))

    def test_remove_mu(self):
        self.assertEqual('baju', self.visitor.remove('bajumu'))

    def test_remove_nya(self):
        self.assertEqual('celana', self.visitor.remove('celananya'))

    def test_remove_with_dash_ku(self):
        self.assertEqual('nikmat-Ku', self.visitor.remove('nikmat-Ku'))

    def test_no_pronoun(self):
        self.assertEqual('kata', self.visitor.remove('kata'))

    def test_visit_adds_removal(self):
        ctx = MockContext('jubahku')
        self.visitor.visit(ctx)
        self.assertEqual(1, len(ctx.removals))
        self.assertEqual('PP', ctx.removals[0].get_affix_type())
        self.assertEqual('jubah', ctx.current_word)


class TestRemoveDerivationalSuffix(unittest.TestCase):
    def setUp(self):
        self.visitor = RemoveDerivationalSuffix()

    def test_remove_i(self):
        self.assertEqual('hantu', self.visitor.remove('hantui'))

    def test_remove_kan(self):
        self.assertEqual('beli', self.visitor.remove('belikan'))

    def test_remove_an(self):
        self.assertEqual('jual', self.visitor.remove('jualan'))

    def test_remove_is(self):
        self.assertEqual('ideal', self.visitor.remove('idealis'))

    def test_remove_isme(self):
        self.assertEqual('ideal', self.visitor.remove('idealisme'))

    def test_remove_isasi(self):
        self.assertEqual('final', self.visitor.remove('finalisasi'))

    def test_remove_isasi_prefers_longest_match(self):
        self.assertEqual('final', self.visitor.remove('finalisasi'))

    def test_no_suffix(self):
        self.assertEqual('kata', self.visitor.remove('kata'))

    def test_visit_adds_removal(self):
        ctx = MockContext('belikan')
        self.visitor.visit(ctx)
        self.assertEqual(1, len(ctx.removals))
        self.assertEqual('DS', ctx.removals[0].get_affix_type())
        self.assertEqual('beli', ctx.current_word)


class TestRemovePlainPrefix(unittest.TestCase):
    def setUp(self):
        self.visitor = RemovePlainPrefix()

    def test_remove_di(self):
        self.assertEqual('buang', self.visitor.remove('dibuang'))

    def test_remove_ke(self):
        self.assertEqual('sakitan', self.visitor.remove('kesakitan'))

    def test_remove_se(self):
        self.assertEqual('suap', self.visitor.remove('sesuap'))

    def test_no_prefix(self):
        self.assertEqual('makan', self.visitor.remove('makan'))

    def test_prefix_not_at_start(self):
        self.assertEqual('di', self.visitor.remove('sedi'))

    def test_visit_adds_removal(self):
        ctx = MockContext('dibuang')
        self.visitor.visit(ctx)
        self.assertEqual(1, len(ctx.removals))
        self.assertEqual('DP', ctx.removals[0].get_affix_type())
        self.assertEqual('buang', ctx.current_word)


if __name__ == '__main__':
    unittest.main()
