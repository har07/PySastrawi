import unittest
from sastrawi import Stemmer

class Test_StemmerTest(unittest.TestCase):
    def setUp(self):
        words = {'hancur', 'benar', 'apa', 'siapa', 'jubah', 'baju', 'beli', 
            'celana', 'hantu', 'jual', 'buku', 'milik', 'kulit', 'sakit',
            'kasih', 'buang', 'suap', 'nilai', 'beri', 'rambut', 'adu', 'suara',
            'daerah', 'ajar', 'kerja', 'ternak', 'asing', 'raup', 'gerak',
            'puruk', 'terbang', 'lipat', 'ringkas', 'warna', 'yakin', 'bangun',
            'fitnah', 'vonis', 'baru', 'ajar', 'tangkap', 'kupas', 'minum',
            'pukul', 'cinta', 'dua', 'dahulu', 'jauh', 'jarah', 'ziarah',
            'nuklir', 'nasihat', 'gila', 'hajar', 'qasar', 'udara', 'populer',
            'warna', 'yoga', 'adil', 'rumah', 'muka', 'labuh', 'tarung',
            'tebar', 'indah', 'daya', 'untung', 'sepuluh', 'ekonomi', 'makmur',
            'telah', 'serta', 'percaya', 'pengaruh', 'kritik', 'seko',
            'sekolah', 'tahan', 'capa', 'capai', 'mula', 'mulai', 'petan',
            'tani', 'aba', 'abai', 'balas', 'balik', 'peran', 'medan', 'syukur',
            'syarat', 'bom', 'promosi', 'proteksi', 'prediksi', 'kaji',
            'sembunyi', 'langgan', 'laku', 'baik', 'terang', 'iman', 'bisik',
            'taat', 'puas', 'makan', 'nyala', 'nyanyi', 'nyata', 'nyawa',
            'rata', 'lembut', 'ligas', 'budaya', 'karya', 'ideal', 'final',
            # sastrawi additional rules
            'taat', 'tiru', 'sepak', 'kuasa', 'malaikat', 'nikmat', 'stabil',
            'transkripsi', 'lewat', 'nganga', 'allah'}

        self.stemmer_basic = Stemmer()
        self.stemmer_custom = Stemmer(rootwords=words,
                                      stopwords=('di', 'ke'))

        return super(Test_StemmerTest, self).setUp()

    def test_stemming_basic(self):
        """Try to stem from data dictionary."""

        data = [
            ['kebijakan', 'bijak'],
            ['karyawan', 'karya'],
            ['karyawati', 'karya'],
            ['kinerja', 'kerja'],
            ['mengandung', 'kandung'],
            ['memakan', 'makan'],
            ['asean', 'asean'],
            ['pemandu', 'pandu'],
            ['mengurangi', 'kurang'],
            ['pemerintah', 'perintah'],
            ['mengabulkan', 'kabul'],
            ['mengupas', 'kupas'],
            ['keterpurukan', 'puruk'],
            ['ditemukan', 'temu'],
            ['mengerti', 'erti'],
            ['kebon', 'kebon'],
            ['terdepan', 'depan'],
            ['mengikis', 'kikis'],
            ['kedudukan', 'duduk'],
            ['menekan', 'tekan'],
            ['perusakan', 'rusa'], # overstemming, it's better than perusa
            ['ditemui', 'temu'],
            ['di', 'di'],
            ['mengalahkan', 'kalah'],
            ['melewati', 'lewat'],
            ['bernafas', 'nafas'],
            ['meniru-niru', 'tiru'],
            ['memanggil-manggil', 'panggil'],
            ['menyebut-nyebut', 'sebut'],
            ['menganga', 'nganga'],
            ['besaran', 'besar'],
            ['terhenyak', 'henyak'],
            ['mengokohkan', 'kokoh'],
            ['melainkan', 'lain'],
            ['kuasa-Mu', 'kuasa'],
            ['malaikat-malaikat-Nya', 'malaikat'],
            ['nikmat-Ku', 'nikmat']
        ]

        for item in data:
            self.assertEqual(self.stemmer_basic.stem(item[0]), item[1])

    def test_stemming_custom(self):
        """Try to stem from custom dictionary."""

        data = [
            # don't stem short words
            ['di', 'di'],
            ['mei', 'mei'],
            ['bui', 'bui'],

            # lookup up the dictionary, to prevent overstemming
            # don't stem nilai to nila
            ['nilai', 'nilai'],

            # lah|kah|tah|pun
            ['hancurlah', 'hancur'],
            ['benarkah', 'benar'],
            ['apatah', 'apa'],
            ['siapapun', 'siapa'],

            # ku|mu|nya
            ['jubahku', 'jubah'],
            ['bajumu', 'baju'],
            ['celananya', 'celana'],

            # i|kan|an
            ['hantui', 'hantu'],
            ['belikan', 'beli'],
            ['jualan', 'jual'],

            # combination of suffixes
            ['bukumukah', 'buku'],
            ['miliknyalah', 'milik'],
            ['kulitkupun', 'kulit'],
            ['berikanku', 'beri'],
            ['sakitimu', 'sakit'],
            ['beriannya', 'beri'],
            ['kasihilah', 'kasih'],

            # plain prefix
            ['dibuang', 'buang'],
            ['kesakitan', 'sakit'],
            ['sesuap', 'suap'],

            # ['teriakanmu', 'teriak'], # wtf? kok jadi ria?
            # teriakanmu -> te-ria-kan-mu

            # template formulas for derivation prefix rules (disambiguation) #

            # rule 1a : berV -> ber-V
            ['beradu', 'adu'],

            # rule 1b : berV -> be-rV
            ['berambut', 'rambut'],

            # rule 2 : berCAP -> ber-CAP
            ['bersuara', 'suara'],

            # rule 3 : berCAerV -> ber-CAerV where C != 'r'
            ['berdaerah', 'daerah'],

            # rule 4 : belajar -> bel-ajar
            ['belajar', 'ajar'],

            # rule 5 : beC1erC2 -> be-C1erC2 where C1 != {'r'|'l'}
            ['bekerja', 'kerja'],
            ['beternak', 'ternak'],

            # rule 6a : terV -> ter-V
            ['terasing', 'asing'],

            # rule 6b : terV -> te-rV
            ['teraup', 'raup'],

            # rule 7 : terCerV -> ter-CerV where C != 'r'
            ['tergerak', 'gerak'],

            # rule 8 : terCP -> ter-CP where C != 'r' and P != 'er'
            ['terpuruk', 'puruk'],

            # rule 9 : teC1erC2 -> te-C1erC2 where C1 != 'r'
            ['teterbang', 'terbang'],

            # rule 10 : me{l|r|w|y}V -> me-{l|r|w|y}V
            ['melipat', 'lipat'],
            ['meringkas', 'ringkas'],
            ['mewarnai', 'warna'],
            ['meyakinkan', 'yakin'],

            # rule 11 : mem{b|f|v} -> mem-{b|f|v}
            ['membangun', 'bangun'],
            ['memfitnah', 'fitnah'],
            ['memvonis', 'vonis'],

            # rule 12 : mempe{r|l} -> mem-pe
            ['memperbarui', 'baru'],
            ['mempelajari', 'ajar'],

            # rule 13a : mem{rV|V} -> mem{rV|V}
            ['meminum', 'minum'],

            # rule 13b : mem{rV|V} -> me-p{rV|V}
            ['memukul', 'pukul'],

            # rule 14 : men{c|d|j|z} -> men-{c|d|j|z}
            ['mencinta', 'cinta'],
            ['mendua', 'dua'],
            ['menjauh', 'jauh'],
            ['menziarah', 'ziarah'],

            # rule 15a : men{V} -> me-n{V}
            ['menuklir', 'nuklir'],

            # rule 15b : men{V} -> me-t{V}
            ['menangkap', 'tangkap'],

            # rule 16 : meng{g|h|q} -> meng-{g|h|q}
            ['menggila', 'gila'],
            ['menghajar', 'hajar'],
            ['mengqasar', 'qasar'],

            # rule 17a : mengV -> meng-V
            ['mengudara', 'udara'],

            # rule 17b : mengV -> meng-kV
            ['mengupas', 'kupas'],

            # rule 18 : menyV -> meny-sV
            ['menyuarakan', 'suara'],

            # rule 19 : mempV -> mem-pV where V != 'e'
            ['mempopulerkan', 'populer'],

            # rule 20 : pe{w|y}V -> pe-{w|y}V
            ['pewarna', 'warna'],
            ['peyoga', 'yoga'],

            # rule 21a : perV -> per-V
            ['peradilan', 'adil'],

            # rule 21b : perV -> pe-rV
            ['perumahan', 'rumah'],

            # rule 22 is missing in the document.

            # rule 23 : perCAP -> per-CAP where C != 'r' and P != 'er'
            ['permuka', 'muka'],

            # rule 24 : perCAerV -> per-CAerV where C != 'r'
            ['perdaerah', 'daerah'],

            # rule 25 : pem{b|f|v} -> pem-{b|f|v}
            ['pembangun', 'bangun'],
            ['pemfitnah', 'fitnah'],
            ['pemvonis', 'vonis'],

            # rule 26a : pem{rV|V} -> pe-m{rV|V}
            ['peminum', 'minum'],

            # rule 26b : pem{rV|V} -> pe-p{rV|V}
            ['pemukul', 'pukul'],

            # rule 27 : men{c|d|j|z} -> men-{c|d|j|z}
            ['pencinta', 'cinta'],
            ['pendahulu', 'dahulu'],
            ['penjarah', 'jarah'],
            ['penziarah', 'ziarah'],

            # rule 28a : pen{V} -> pe-n{V}
            ['penasihat', 'nasihat'],

            # rule 28b : pen{V} -> pe-t{V}
            ['penangkap', 'tangkap'],

            # rule 29 : peng{g|h|q} -> peng-{g|h|q}
            ['penggila', 'gila'],
            ['penghajar', 'hajar'],
            ['pengqasar', 'qasar'],

            # rule 30a : pengV -> peng-V
            ['pengudara', 'udara'],

            # rule 30b : pengV -> peng-kV
            ['pengupas', 'kupas'],

            # rule 31 : penyV -> peny-sV
            ['penyuara', 'suara'],

            # rule 32 : pelV -> pe-lV except pelajar -> ajar
            ['pelajar', 'ajar'],
            ['pelabuhan', 'labuh'],

            # rule 33 : peCerV -> per-erV where C != {r|w|y|l|m|n}
            # TODO : find the examples

            # rule 34 : peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
            ['petarung', 'tarung'],

            # CS additional rules

            # rule 35 : terC1erC2 -> ter-C1erC2 where C1 != 'r'
            ['terpercaya', 'percaya'],

            # rule 36 : peC1erC2 -> pe-C1erC2 where C1 != {r|w|y|l|m|n}
            ['pekerja', 'kerja'],
            ['peserta', 'serta'],

            # CS modify rule 12
            ['mempengaruhi', 'pengaruh'],

            # CS modify rule 16
            ['mengkritik', 'kritik'],

            # CS adjusting rule precedence
            ['bersekolah', 'sekolah'],
            ['bertahan', 'tahan'],
            ['mencapai', 'capai'],
            ['dimulai', 'mulai'],
            ['petani', 'tani'],
            ['terabai', 'abai'],

            # ECS
            ['mensyaratkan', 'syarat'],
            ['mensyukuri', 'syukur'],
            ['mengebom', 'bom'],
            ['mempromosikan', 'promosi'],
            ['memproteksi', 'proteksi'],
            ['memprediksi', 'prediksi'],
            ['pengkajian', 'kaji'],
            ['pengebom', 'bom'],

            # ECS loop pengembalian akhiran
            ['bersembunyi', 'sembunyi'],
            ['bersembunyilah', 'sembunyi'],
            ['pelanggan', 'langgan'],
            ['pelaku', 'laku'],
            ['pelangganmukah', 'langgan'],
            ['pelakunyalah', 'laku'],

            ['perbaikan', 'baik'],
            ['kebaikannya', 'baik'],
            ['bisikan', 'bisik'],
            ['menerangi', 'terang'],
            ['berimanlah', 'iman'],

            ['memuaskan', 'puas'],
            ['berpelanggan', 'langgan'],
            ['bermakanan', 'makan'],

            # CC (Modified ECS)
            ['menyala', 'nyala'],
            ['menyanyikan', 'nyanyi'],
            ['menyatakannya', 'nyata'],

            ['penyanyi', 'nyanyi'],
            ['penyawaan', 'nyawa'],

            # CC infix
            ['rerata', 'rata'],
            ['lelembut', 'lembut'],
            ['lemigas', 'ligas'],
            ['kinerja', 'kerja'],

            # plurals
            ['buku-buku', 'buku'],
            ['berbalas-balasan', 'balas'],
            ['bolak-balik', 'bolak-balik'],

            # combination of prefix + suffix
            ['bertebaran', 'tebar'],
            ['terasingkan', 'asing'],
            ['membangunkan', 'bangun'],
            ['mencintai', 'cinta'],
            ['menduakan', 'dua'],
            ['menjauhi', 'jauh'],
            ['menggilai', 'gila'],
            ['pembangunan', 'bangun'],

            # return the word if not found in the dictionary
            ['marwan', 'marwan'],
            ['subarkah', 'subarkah'],

            # recursively remove prefix
            ['memberdayakan', 'daya'],
            ['persemakmuran', 'makmur'],
            ['keberuntunganmu', 'untung'],
            ['kesepersepuluhnya', 'sepuluh'],

            # test stem sentence
            ['siapakah memberdayakan pembangunan', 'siapa daya bangun'],

            # issues
            ['Perekonomian', 'ekonomi'],
            ['menahan', 'tahan'],

            # test stem multiple sentences
            ['Cinta telah bertebaran.Keduanya saling mencintai.',
             'cinta telah tebar dua saling cinta'],
            ['(Cinta telah bertebaran)\n\n\n\nKeduanya saling mencintai.',
             'cinta telah tebar dua saling cinta'],

            # failed on other method / algorithm but we should succeed
            ['peranan', 'peran'],
            ['memberikan', 'beri'],
            ['medannya', 'medan'],

            # TODO:
            #    ['sebagai', 'bagai'],
            #    ['bagian', 'bagian'],
            #    ['berbadan', 'badan'],
            #    ['abdullah', 'abdullah'],

            # adopted foreign suffixes
            ['budayawan', 'budaya'],
            ['karyawati', 'karya'],
            ['idealis', 'ideal'],
            ['idealisme', 'ideal'],
            ['finalisasi', 'final'],

            # sastrawi additional rules
            ['penstabilan', 'stabil'],
            ['pentranskripsi', 'transkripsi'],

            ['mentaati', 'taat'],
            ['meniru-nirukan', 'tiru'],
            ['menyepak-nyepak', 'sepak'],

            ['melewati', 'lewat'],
            ['menganga', 'nganga'],

            ['kupukul', 'pukul'],
            ['kauhajar', 'hajar'],

            ['kuasa-Mu', 'kuasa'],
            ['malaikat-malaikat-Nya', 'malaikat'],
            ['nikmat-Ku', 'nikmat'],
            ['allah-lah', 'allah']
        ]

        for item in data:
            self.assertEqual(self.stemmer_custom.stem(item[0]), item[1])

    def test_remove_stopword(self):
        f = self.stemmer_custom.remove_stopword
        self.assertEqual(f('pergi ke sekolah'), 'pergi sekolah')
        self.assertEqual(f('makan di rumah'), 'makan rumah')


if __name__ == '__main__':
    unittest.main()
