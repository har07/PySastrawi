import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Stemmer import Stemmer

class Test_StemmerTest(unittest.TestCase):
    def setUp(self):
        self.dictionary = ArrayDictionary(
            [
                'hancur', 'benar', 'apa', 'siapa', 'jubah', 'baju', 'beli',
                'celana', 'hantu', 'jual', 'buku', 'milik', 'kulit', 'sakit', 'kasih', 'buang', 'suap',
                'nilai', 'beri', 'rambut', 'adu', 'suara', 'daerah', 'ajar', 'kerja', 'ternak',
                'asing', 'raup', 'gerak', 'puruk', 'terbang', 'lipat', 'ringkas', 'warna', 'yakin',
                'bangun', 'fitnah', 'vonis',
                'baru', 'ajar',
                'tangkap', 'kupas',
                'minum', 'pukul',
                'cinta', 'dua', 'dahulu', 'jauh', 'jarah', 'ziarah',
                'nuklir', 'nasihat', 'gila', 'hajar', 'qasar', 'udara',
                'populer', 'warna', 'yoga', 'adil', 'rumah', 'muka', 'labuh', 'tarung',
                'tebar', 'indah', 'daya', 'untung', 'sepuluh', 'ekonomi', 'makmur', 'telah', 'serta',
                'percaya', 'pengaruh', 'kritik', 'seko', 'sekolah', 'tahan', 'capa', 'capai',
                'mula', 'mulai', 'petan', 'tani', 'aba', 'abai', 'balas', 'balik',
                'peran', 'medan', 'syukur', 'syarat', 'bom', 'promosi', 'proteksi', 'prediksi', 'kaji',
                'sembunyi', 'langgan', 'laku', 'baik', 'terang', 'iman', 'bisik', 'taat', 'puas', 'makan',
                'nyala', 'nyanyi', 'nyata', 'nyawa', 'rata', 'lembut', 'ligas',
                'budaya', 'karya', 'ideal', 'final',
                # sastrawi additional rules
                'taat', 'tiru', 'sepak', 'kuasa', 'malaikat', 'nikmat', 'stabil', 'transkripsi',
                'lewat', 'nganga', 'allah',
            ]
        )
        self.stemmer = Stemmer(self.dictionary)
        return super(Test_StemmerTest, self).setUp()

    def try_stem(self, word, stem):
        self.assertEquals(stem, self.stemmer.stem(word))

    def get_test_data(self):
        data = []

        # don't stem short words
        data.append(['mei', 'mei'])
        data.append(['bui', 'bui'])

        # lookup up the dictionary, to prevent overstemming
        # don't stem nilai to nila
        data.append(['nilai', 'nilai'])

        # lah|kah|tah|pun
        data.append(['hancurlah', 'hancur'])
        data.append(['benarkah', 'benar'])
        data.append(['apatah', 'apa'])
        data.append(['siapapun', 'siapa'])

        # ku|mu|nya
        data.append(['jubahku', 'jubah'])
        data.append(['bajumu', 'baju'])
        data.append(['celananya', 'celana'])

        # i|kan|an
        data.append(['hantui', 'hantu'])
        data.append(['belikan', 'beli'])
        data.append(['jualan', 'jual'])

        # combination of suffixes
        data.append(['bukumukah', 'buku']) #gagal karena -ku dianggap suffix dan dihilangkan
        data.append(['miliknyalah', 'milik'])
        data.append(['kulitkupun', 'kulit']) #gagal karena -ku dianggap suffix dan dihilangkan
        data.append(['berikanku', 'beri'])
        data.append(['sakitimu', 'sakit'])
        data.append(['beriannya', 'beri'])
        data.append(['kasihilah', 'kasih'])

        # plain prefix
        data.append(['dibuang', 'buang'])
        data.append(['kesakitan', 'sakit'])
        data.append(['sesuap', 'suap'])

        #data.append(['teriakanmu', 'teriak']) # wtf? kok jadi ria?
        #teriakanmu -> te-ria-kan-mu

        # template formulas for derivation prefix rules (disambiguation) #

        # rule 1a : berV -> ber-V
        data.append(['beradu', 'adu'])

        # rule 1b : berV -> be-rV
        data.append(['berambut', 'rambut'])

        # rule 2 : berCAP -> ber-CAP
        data.append(['bersuara', 'suara'])

        # rule 3 : berCAerV -> ber-CAerV where C != 'r'
        data.append(['berdaerah', 'daerah'])

        # rule 4 : belajar -> bel-ajar
        data.append(['belajar', 'ajar'])

        # rule 5 : beC1erC2 -> be-C1erC2 where C1 != {'r'|'l'}
        data.append(['bekerja', 'kerja'])
        data.append(['beternak', 'ternak'])

        # rule 6a : terV -> ter-V
        data.append(['terasing', 'asing'])

        # rule 6b : terV -> te-rV
        data.append(['teraup', 'raup'])

        # rule 7 : terCerV -> ter-CerV where C != 'r'
        data.append(['tergerak', 'gerak'])

        # rule 8 : terCP -> ter-CP where C != 'r' and P != 'er'
        data.append(['terpuruk', 'puruk'])

        # rule 9 : teC1erC2 -> te-C1erC2 where C1 != 'r'
        data.append(['teterbang', 'terbang'])

        # rule 10 : me{l|r|w|y}V -> me-{l|r|w|y}V
        data.append(['melipat', 'lipat'])
        data.append(['meringkas', 'ringkas'])
        data.append(['mewarnai', 'warna'])
        data.append(['meyakinkan', 'yakin'])

        # rule 11 : mem{b|f|v} -> mem-{b|f|v}
        data.append(['membangun', 'bangun'])
        data.append(['memfitnah', 'fitnah'])
        data.append(['memvonis', 'vonis'])

        # rule 12 : mempe{r|l} -> mem-pe
        data.append(['memperbarui', 'baru'])
        data.append(['mempelajari', 'ajar'])

        # rule 13a : mem{rV|V} -> mem{rV|V}
        data.append(['meminum', 'minum'])

        # rule 13b : mem{rV|V} -> me-p{rV|V}
        data.append(['memukul', 'pukul'])

        # rule 14 : men{c|d|j|z} -> men-{c|d|j|z}
        data.append(['mencinta', 'cinta'])
        data.append(['mendua', 'dua'])
        data.append(['menjauh', 'jauh'])
        data.append(['menziarah', 'ziarah'])

        # rule 15a : men{V} -> me-n{V}
        data.append(['menuklir', 'nuklir'])

        # rule 15b : men{V} -> me-t{V}
        data.append(['menangkap', 'tangkap'])

        # rule 16 : meng{g|h|q} -> meng-{g|h|q}
        data.append(['menggila', 'gila'])
        data.append(['menghajar', 'hajar'])
        data.append(['mengqasar', 'qasar'])

        # rule 17a : mengV -> meng-V
        data.append(['mengudara', 'udara'])

        # rule 17b : mengV -> meng-kV
        data.append(['mengupas', 'kupas'])

        # rule 18 : menyV -> meny-sV
        data.append(['menyuarakan', 'suara'])

        # rule 19 : mempV -> mem-pV where V != 'e'
        data.append(['mempopulerkan', 'populer'])

        # rule 20 : pe{w|y}V -> pe-{w|y}V
        data.append(['pewarna', 'warna'])
        data.append(['peyoga', 'yoga'])

        # rule 21a : perV -> per-V
        data.append(['peradilan', 'adil'])

        # rule 21b : perV -> pe-rV
        data.append(['perumahan', 'rumah'])

        # rule 22 is missing in the document?

        # rule 23 : perCAP -> per-CAP where C != 'r' and P != 'er'
        data.append(['permuka', 'muka'])

        # rule 24 : perCAerV -> per-CAerV where C != 'r'
        data.append(['perdaerah', 'daerah'])

        # rule 25 : pem{b|f|v} -> pem-{b|f|v}
        data.append(['pembangun', 'bangun'])
        data.append(['pemfitnah', 'fitnah'])
        data.append(['pemvonis', 'vonis'])

        # rule 26a : pem{rV|V} -> pe-m{rV|V}
        data.append(['peminum', 'minum'])

        # rule 26b : pem{rV|V} -> pe-p{rV|V}
        data.append(['pemukul', 'pukul'])

        # rule 27 : men{c|d|j|z} -> men-{c|d|j|z}
        data.append(['pencinta', 'cinta'])
        data.append(['pendahulu', 'dahulu'])
        data.append(['penjarah', 'jarah'])
        data.append(['penziarah', 'ziarah'])

        # rule 28a : pen{V} -> pe-n{V}
        data.append(['penasihat', 'nasihat'])

        # rule 28b : pen{V} -> pe-t{V}
        data.append(['penangkap', 'tangkap'])

        # rule 29 : peng{g|h|q} -> peng-{g|h|q}
        data.append(['penggila', 'gila'])
        data.append(['penghajar', 'hajar'])
        data.append(['pengqasar', 'qasar'])

        # rule 30a : pengV -> peng-V
        data.append(['pengudara', 'udara'])

        # rule 30b : pengV -> peng-kV
        data.append(['pengupas', 'kupas'])

        # rule 31 : penyV -> peny-sV
        data.append(['penyuara', 'suara'])

        # rule 32 : pelV -> pe-lV except pelajar -> ajar
        data.append(['pelajar', 'ajar'])
        data.append(['pelabuhan', 'labuh'])

        # rule 33 : peCerV -> per-erV where C != {r|w|y|l|m|n}
        # TODO : find the examples

        # rule 34 : peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
        data.append(['petarung', 'tarung'])

        # CS additional rules

        # rule 35 : terC1erC2 -> ter-C1erC2 where C1 != 'r'
        data.append(['terpercaya', 'percaya'])

        # rule 36 : peC1erC2 -> pe-C1erC2 where C1 != {r|w|y|l|m|n}
        data.append(['pekerja', 'kerja'])
        data.append(['peserta', 'serta'])

        # CS modify rule 12
        data.append(['mempengaruhi', 'pengaruh'])

        # CS modify rule 16
        data.append(['mengkritik', 'kritik'])

        # CS adjusting rule precedence
        data.append(['bersekolah', 'sekolah']) #gagal sekolah -> seko why?
        data.append(['bertahan', 'tahan'])
        data.append(['mencapai', 'capai']) #gagal mencapai -> capa
        data.append(['dimulai', 'mulai'])
        data.append(['petani', 'tani']) #gagal petani -> petan
        data.append(['terabai', 'abai']) #gagal terabai -> aba

        # ECS
        data.append(['mensyaratkan', 'syarat'])
        data.append(['mensyukuri', 'syukur'])
        data.append(['mengebom', 'bom'])
        data.append(['mempromosikan', 'promosi'])
        data.append(['memproteksi', 'proteksi'])
        data.append(['memprediksi', 'prediksi'])
        data.append(['pengkajian', 'kaji'])
        data.append(['pengebom', 'bom'])

        # ECS loop pengembalian akhiran
        data.append(['bersembunyi', 'sembunyi'])
        data.append(['bersembunyilah', 'sembunyi'])
        data.append(['pelanggan', 'langgan'])
        data.append(['pelaku', 'laku'])
        data.append(['pelangganmukah', 'langgan'])
        data.append(['pelakunyalah', 'laku'])

        data.append(['perbaikan', 'baik'])
        data.append(['kebaikannya', 'baik'])
        data.append(['bisikan', 'bisik'])
        data.append(['menerangi', 'terang'])
        data.append(['berimanlah', 'iman'])

        data.append(['memuaskan', 'puas'])
        data.append(['berpelanggan', 'langgan'])
        data.append(['bermakanan', 'makan'])

        # CC (Modified ECS)
        data.append(['menyala', 'nyala'])
        data.append(['menyanyikan', 'nyanyi'])
        data.append(['menyatakannya', 'nyata'])

        data.append(['penyanyi', 'nyanyi'])
        data.append(['penyawaan', 'nyawa'])

        # CC infix
        data.append(['rerata', 'rata'])
        data.append(['lelembut', 'lembut'])
        data.append(['lemigas', 'ligas'])
        data.append(['kinerja', 'kerja'])

        # plurals
        data.append(['buku-buku', 'buku'])
        data.append(['berbalas-balasan', 'balas'])
        data.append(['bolak-balik', 'bolak-balik'])

        # combination of prefix + suffix
        data.append(['bertebaran', 'tebar'])
        data.append(['terasingkan', 'asing'])
        data.append(['membangunkan', 'bangun'])
        data.append(['mencintai', 'cinta'])
        data.append(['menduakan', 'dua'])
        data.append(['menjauhi', 'jauh'])
        data.append(['menggilai', 'gila'])
        data.append(['pembangunan', 'bangun'])

        # return the word if not found in the dictionary
        data.append(['marwan', 'marwan'])
        data.append(['subarkah', 'subarkah'])

        # recursively remove prefix
        data.append(['memberdayakan', 'daya'])
        data.append(['persemakmuran', 'makmur'])
        data.append(['keberuntunganmu', 'untung'])
        data.append(['kesepersepuluhnya', 'sepuluh'])

        # test stem sentence
        data.append(['siapakah memberdayakan pembangunan', 'siapa daya bangun'])

        # issues
        data.append(['Perekonomian', 'ekonomi'])
        data.append(['menahan', 'tahan'])

        # test stem multiple sentences
        multipleSentence1 = 'Cinta telah bertebaran.Keduanya saling mencintai.';
        multipleSentence2 = "(Cinta telah bertebaran)\n\n\n\nKeduanya saling mencintai.";
        data.append([multipleSentence1, 'cinta telah tebar dua saling cinta'])
        data.append([multipleSentence2, 'cinta telah tebar dua saling cinta'])

        # failed on other method / algorithm but we should succeed
        data.append(['peranan', 'peran'])
        data.append(['memberikan', 'beri'])
        data.append(['medannya', 'medan'])

        # TODO:
        #data.append(['sebagai', 'bagai'])
        #data.append(['bagian', 'bagian'])
        #data.append(['berbadan', 'badan'])
        #data.append(['abdullah', 'abdullah'])

        # adopted foreign suffixes
        #data.append(['budayawan', 'budaya'])
        #data.append(['karyawati', 'karya'])
        data.append(['idealis', 'ideal'])
        data.append(['idealisme', 'ideal'])
        data.append(['finalisasi', 'final'])

        # sastrawi additional rules
        data.append(['penstabilan', 'stabil'])
        data.append(['pentranskripsi', 'transkripsi'])

        data.append(['mentaati', 'taat'])
        data.append(['meniru-nirukan', 'tiru'])
        data.append(['menyepak-nyepak', 'sepak'])

        data.append(['melewati', 'lewat'])
        data.append(['menganga', 'nganga'])

        data.append(['kupukul', 'pukul'])
        data.append(['kauhajar', 'hajar'])

        data.append(['kuasa-Mu', 'kuasa'])
        data.append(['malaikat-malaikat-Nya', 'malaikat'])
        data.append(['nikmat-Ku', 'nikmat'])
        data.append(['allah-lah', 'allah'])

        return data

    def test_All(self):
        data = self.get_test_data()
        for d in data:
            self.try_stem(d[0], d[1])
        

if __name__ == '__main__':
    unittest.main()
