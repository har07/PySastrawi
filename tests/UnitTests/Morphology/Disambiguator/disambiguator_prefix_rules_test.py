import unittest
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule1 import DisambiguatorPrefixRule1a, DisambiguatorPrefixRule1b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule2 import DisambiguatorPrefixRule2
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule3 import DisambiguatorPrefixRule3
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule4 import DisambiguatorPrefixRule4
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule5 import DisambiguatorPrefixRule5
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule6 import DisambiguatorPrefixRule6a, DisambiguatorPrefixRule6b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule7 import DisambiguatorPrefixRule7
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule8 import DisambiguatorPrefixRule8
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule9 import DisambiguatorPrefixRule9
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule10 import DisambiguatorPrefixRule10
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule11 import DisambiguatorPrefixRule11
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule12 import DisambiguatorPrefixRule12
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule13 import DisambiguatorPrefixRule13a, DisambiguatorPrefixRule13b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule14 import DisambiguatorPrefixRule14
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule15 import DisambiguatorPrefixRule15a, DisambiguatorPrefixRule15b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule16 import DisambiguatorPrefixRule16
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule17 import DisambiguatorPrefixRule17a, DisambiguatorPrefixRule17b, DisambiguatorPrefixRule17c, DisambiguatorPrefixRule17d
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule18 import DisambiguatorPrefixRule18a, DisambiguatorPrefixRule18b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule19 import DisambiguatorPrefixRule19
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule20 import DisambiguatorPrefixRule20
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule21 import DisambiguatorPrefixRule21a, DisambiguatorPrefixRule21b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule23 import DisambiguatorPrefixRule23
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule24 import DisambiguatorPrefixRule24
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule25 import DisambiguatorPrefixRule25
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule26 import DisambiguatorPrefixRule26a, DisambiguatorPrefixRule26b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule27 import DisambiguatorPrefixRule27
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule28 import DisambiguatorPrefixRule28a, DisambiguatorPrefixRule28b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule29 import DisambiguatorPrefixRule29
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule30 import DisambiguatorPrefixRule30a, DisambiguatorPrefixRule30b, DisambiguatorPrefixRule30c
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule31 import DisambiguatorPrefixRule31a, DisambiguatorPrefixRule31b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule32 import DisambiguatorPrefixRule32
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule34 import DisambiguatorPrefixRule34
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule35 import DisambiguatorPrefixRule35
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule36 import DisambiguatorPrefixRule36
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule37 import DisambiguatorPrefixRule37a, DisambiguatorPrefixRule37b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule38 import DisambiguatorPrefixRule38a, DisambiguatorPrefixRule38b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule39 import DisambiguatorPrefixRule39a, DisambiguatorPrefixRule39b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule40 import DisambiguatorPrefixRule40a, DisambiguatorPrefixRule40b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule41 import DisambiguatorPrefixRule41
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule42 import DisambiguatorPrefixRule42


class TestDisambiguatorPrefixRules(unittest.TestCase):
    def assertDisambiguates(self, rule, word, expected):
        result = rule.disambiguate(word)
        self.assertEqual(expected, result,
                         f'{rule.__class__.__name__}.disambiguate({word!r}) '
                         f'expected {expected!r} but got {result!r}')

    def assertNoMatch(self, rule, word):
        result = rule.disambiguate(word)
        self.assertIsNone(result,
                          f'{rule.__class__.__name__}.disambiguate({word!r}) '
                          f'should return None but got {result!r}')

    # Rule 1a: berV -> ber-V
    def test_rule1a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule1a(), 'beradu', 'adu')
        self.assertNoMatch(DisambiguatorPrefixRule1a(), 'berlari')

    # Rule 1b: berV -> be-rV
    def test_rule1b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule1b(), 'berambut', 'rambut')
        self.assertDisambiguates(DisambiguatorPrefixRule1b(), 'berakit', 'rakit')

    # Rule 2: berCAP -> ber-CAP
    def test_rule2(self):
        self.assertDisambiguates(DisambiguatorPrefixRule2(), 'bersuara', 'suara')
        self.assertNoMatch(DisambiguatorPrefixRule2(), 'beriak')

    # Rule 3: berCAerV -> ber-CAerV where C != 'r'
    def test_rule3(self):
        self.assertDisambiguates(DisambiguatorPrefixRule3(), 'berdaerah', 'daerah')
        self.assertNoMatch(DisambiguatorPrefixRule3(), 'bersuara')

    # Rule 4: belajar -> ajar
    def test_rule4(self):
        self.assertDisambiguates(DisambiguatorPrefixRule4(), 'belajar', 'ajar')
        self.assertNoMatch(DisambiguatorPrefixRule4(), 'belukar')

    # Rule 5: beC1erC2 -> be-C1erC2 where C1 != {'r'|'l'}
    def test_rule5(self):
        self.assertDisambiguates(DisambiguatorPrefixRule5(), 'bekerja', 'kerja')
        self.assertDisambiguates(DisambiguatorPrefixRule5(), 'beternak', 'ternak')
        self.assertNoMatch(DisambiguatorPrefixRule5(), 'belerang')

    # Rule 6a: terV -> ter-V
    def test_rule6a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule6a(), 'terasing', 'asing')
        self.assertNoMatch(DisambiguatorPrefixRule6a(), 'tertawa')

    # Rule 6b: terV -> te-rV
    def test_rule6b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule6b(), 'teraup', 'raup')

    # Rule 7: terCerV -> ter-CerV where C != 'r'
    def test_rule7(self):
        self.assertDisambiguates(DisambiguatorPrefixRule7(), 'tergerak', 'gerak')
        self.assertNoMatch(DisambiguatorPrefixRule7(), 'tertua')

    # Rule 8: terCP -> ter-CP where C != 'r' and P != 'er'
    def test_rule8(self):
        self.assertDisambiguates(DisambiguatorPrefixRule8(), 'terpuruk', 'puruk')
        self.assertDisambiguates(DisambiguatorPrefixRule8(), 'termasuk', 'masuk')

    # Rule 9: teC1erC2 -> te-C1erC2 where C1 != 'r'
    def test_rule9(self):
        self.assertDisambiguates(DisambiguatorPrefixRule9(), 'teterbang', 'terbang')
        self.assertNoMatch(DisambiguatorPrefixRule9(), 'terlerai')

    # Rule 10: me{l|r|w|y}V -> me-{l|r|w|y}V
    def test_rule10(self):
        self.assertDisambiguates(DisambiguatorPrefixRule10(), 'melipat', 'lipat')
        self.assertDisambiguates(DisambiguatorPrefixRule10(), 'meringkas', 'ringkas')
        self.assertDisambiguates(DisambiguatorPrefixRule10(), 'mewarnai', 'warnai')
        self.assertDisambiguates(DisambiguatorPrefixRule10(), 'meyakinkan', 'yakinkan')
        self.assertNoMatch(DisambiguatorPrefixRule10(), 'membangun')

    # Rule 11: mem{b|f|v} -> mem-{b|f|v}
    def test_rule11(self):
        self.assertDisambiguates(DisambiguatorPrefixRule11(), 'membangun', 'bangun')
        self.assertDisambiguates(DisambiguatorPrefixRule11(), 'memfitnah', 'fitnah')
        self.assertDisambiguates(DisambiguatorPrefixRule11(), 'memvonis', 'vonis')

    # Rule 12: mempe{r|l} -> mem-pe
    def test_rule12(self):
        self.assertDisambiguates(DisambiguatorPrefixRule12(), 'memperbarui', 'perbarui')
        self.assertDisambiguates(DisambiguatorPrefixRule12(), 'mempelajari', 'pelajari')

    # Rule 13a: mem{rV|V} -> mem{rV|V}
    def test_rule13a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule13a(), 'meminum', 'minum')

    # Rule 13b: mem{rV|V} -> me-p{rV|V}
    def test_rule13b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule13b(), 'memukul', 'pukul')

    # Rule 14: men{c|d|j|z} -> men-{c|d|j|z}
    def test_rule14(self):
        self.assertDisambiguates(DisambiguatorPrefixRule14(), 'mencinta', 'cinta')
        self.assertDisambiguates(DisambiguatorPrefixRule14(), 'mendua', 'dua')
        self.assertDisambiguates(DisambiguatorPrefixRule14(), 'menjauh', 'jauh')
        self.assertDisambiguates(DisambiguatorPrefixRule14(), 'menziarah', 'ziarah')

    # Rule 15a: men{V} -> me-n{V}
    def test_rule15a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule15a(), 'menuklir', 'nuklir')

    # Rule 15b: men{V} -> me-t{V}
    def test_rule15b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule15b(), 'menangkap', 'tangkap')

    # Rule 16: meng{g|h|q|k} -> meng-{g|h|q|k}
    def test_rule16(self):
        self.assertDisambiguates(DisambiguatorPrefixRule16(), 'menggila', 'gila')
        self.assertDisambiguates(DisambiguatorPrefixRule16(), 'menghajar', 'hajar')
        self.assertDisambiguates(DisambiguatorPrefixRule16(), 'mengqasar', 'qasar')
        self.assertDisambiguates(DisambiguatorPrefixRule16(), 'mengkritik', 'kritik')

    # Rule 17a: mengV -> meng-V
    def test_rule17a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule17a(), 'mengudara', 'udara')

    # Rule 17b: mengV -> meng-kV
    def test_rule17b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule17b(), 'mengupas', 'kupas')

    # Rule 17c: mengV -> meng-V
    def test_rule17c(self):
        self.assertDisambiguates(DisambiguatorPrefixRule17c(), 'mengerat', 'rat')

    # Rule 17d: mengV -> meng-kV
    def test_rule17d(self):
        self.assertDisambiguates(DisambiguatorPrefixRule17d(), 'mengikat', 'ngikat')

    # Rule 18a: menyV -> meny-sV
    def test_rule18a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule18a(), 'menyuarakan', 'nyuarakan')

    # Rule 18b: menyV -> meny-sV
    def test_rule18b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule18b(), 'menyuarakan', 'suarakan')
        self.assertDisambiguates(DisambiguatorPrefixRule18b(), 'menyikat', 'sikat')

    # Rule 19: mempV -> mem-pV
    def test_rule19(self):
        self.assertDisambiguates(DisambiguatorPrefixRule19(), 'mempopulerkan', 'populerkan')
        self.assertNoMatch(DisambiguatorPrefixRule19(), 'mempelajari')

    # Rule 20: pe{w|y}V -> pe-{w|y}V
    def test_rule20(self):
        self.assertDisambiguates(DisambiguatorPrefixRule20(), 'pewarna', 'warna')
        self.assertDisambiguates(DisambiguatorPrefixRule20(), 'peyoga', 'yoga')

    # Rule 21a: perV -> per-V
    def test_rule21a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule21a(), 'peradilan', 'adilan')

    # Rule 21b: perV -> pe-rV
    def test_rule21b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule21b(), 'perumahan', 'rumahan')

    # Rule 23: perCAP -> per-CAP where C != 'r' and P != 'er'
    def test_rule23(self):
        self.assertDisambiguates(DisambiguatorPrefixRule23(), 'permuka', 'muka')

    # Rule 24: perCAerV -> per-CAerV where C != 'r'
    def test_rule24(self):
        self.assertDisambiguates(DisambiguatorPrefixRule24(), 'perdaerah', 'daerah')

    # Rule 25: pem{b|f|v} -> pem-{b|f|v}
    def test_rule25(self):
        self.assertDisambiguates(DisambiguatorPrefixRule25(), 'pembangun', 'bangun')
        self.assertDisambiguates(DisambiguatorPrefixRule25(), 'pemfitnah', 'fitnah')
        self.assertDisambiguates(DisambiguatorPrefixRule25(), 'pemvonis', 'vonis')

    # Rule 26a: pem{rV|V} -> pe-m{rV|V}
    def test_rule26a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule26a(), 'peminum', 'minum')

    # Rule 26b: pem{rV|V} -> pe-p{rV|V}
    def test_rule26b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule26b(), 'pemukul', 'pukul')

    # Rule 27: pen{c|d|j|z} -> pen-{c|d|j|z}
    def test_rule27(self):
        self.assertDisambiguates(DisambiguatorPrefixRule27(), 'pencinta', 'cinta')
        self.assertDisambiguates(DisambiguatorPrefixRule27(), 'pendahulu', 'dahulu')
        self.assertDisambiguates(DisambiguatorPrefixRule27(), 'penjarah', 'jarah')
        self.assertDisambiguates(DisambiguatorPrefixRule27(), 'penziarah', 'ziarah')

    # Rule 28a: pen{V} -> pe-n{V}
    def test_rule28a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule28a(), 'penasihat', 'nasihat')

    # Rule 28b: pen{V} -> pe-t{V}
    def test_rule28b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule28b(), 'penangkap', 'tangkap')

    # Rule 29: peng{g|h|q} -> peng-{g|h|q}
    def test_rule29(self):
        self.assertDisambiguates(DisambiguatorPrefixRule29(), 'penggila', 'gila')
        self.assertDisambiguates(DisambiguatorPrefixRule29(), 'penghajar', 'hajar')
        self.assertDisambiguates(DisambiguatorPrefixRule29(), 'pengqasar', 'qasar')

    # Rule 30a: pengV -> peng-V
    def test_rule30a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule30a(), 'pengudara', 'udara')

    # Rule 30b: pengV -> peng-kV
    def test_rule30b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule30b(), 'pengupas', 'kupas')

    # Rule 30c: pengV -> peng-V
    def test_rule30c(self):
        self.assertDisambiguates(DisambiguatorPrefixRule30c(), 'pengerat', 'rat')

    # Rule 31a: penyV -> peny-sV
    def test_rule31a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule31a(), 'penyuara', 'nyuara')

    # Rule 31b: penyV -> peny-sV
    def test_rule31b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule31b(), 'penyikat', 'sikat')

    # Rule 32: pelV -> pe-lV except pelajar -> ajar
    def test_rule32(self):
        self.assertDisambiguates(DisambiguatorPrefixRule32(), 'pelajar', 'ajar')
        self.assertDisambiguates(DisambiguatorPrefixRule32(), 'pelabuhan', 'labuhan')

    # Rule 34: peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
    def test_rule34(self):
        self.assertDisambiguates(DisambiguatorPrefixRule34(), 'petarung', 'tarung')

    # Rule 35: terC1erC2 -> ter-C1erC2 where C1 != 'r'
    def test_rule35(self):
        self.assertDisambiguates(DisambiguatorPrefixRule35(), 'terpercaya', 'percaya')

    # Rule 36: peC1erC2 -> pe-C1erC2
    def test_rule36(self):
        self.assertDisambiguates(DisambiguatorPrefixRule36(), 'pekerja', 'kerja')
        self.assertDisambiguates(DisambiguatorPrefixRule36(), 'peserta', 'serta')

    # Rule 37a: CerV -> CerV (infix -er-)
    def test_rule37a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule37a(), 'keramaian', 'keramaian')
        self.assertNoMatch(DisambiguatorPrefixRule37a(), 'kerja')

    # Rule 37b: CerV -> CV (infix -er- removal)
    def test_rule37b(self):
        self.assertNoMatch(DisambiguatorPrefixRule37b(), 'kerja')

    # Rule 38a: CelV -> CelV (infix -el-)
    def test_rule38a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule38a(), 'telunjuk', 'telunjuk')

    # Rule 38b: CelV -> CV (infix -el- removal)
    def test_rule38b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule38b(), 'telunjuk', 'tunjuk')

    # Rule 39a: CemV -> CemV (infix -em-)
    def test_rule39a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule39a(), 'kemilau', 'kemilau')

    # Rule 39b: CemV -> CV (infix -em- removal)
    def test_rule39b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule39b(), 'kemilau', 'kilau')

    # Rule 40a: CinV -> CinV (infix -in-)
    def test_rule40a(self):
        self.assertDisambiguates(DisambiguatorPrefixRule40a(), 'sinambung', 'sinambung')

    # Rule 40b: CinV -> CV (infix -in- removal)
    def test_rule40b(self):
        self.assertDisambiguates(DisambiguatorPrefixRule40b(), 'sinambung', 'sambung')

    # Rule 41: kuA -> ku-A and kauA -> kau-A
    def test_rule41(self):
        self.assertDisambiguates(DisambiguatorPrefixRule41(), 'kupukul', 'pukul')
        self.assertNoMatch(DisambiguatorPrefixRule41(), 'kauhajar')

    # Rule 42: kauA -> kau-A
    def test_rule42(self):
        self.assertDisambiguates(DisambiguatorPrefixRule42(), 'kautahan', 'tahan')
        self.assertNoMatch(DisambiguatorPrefixRule42(), 'menahan')


if __name__ == '__main__':
    unittest.main()
