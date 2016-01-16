import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Stemmer import Stemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class Test_StemmerTest(unittest.TestCase):
    def setUp(self):
        stemmerFactory = StemmerFactory()
        self.stemmer = stemmerFactory.create_stemmer()
        return super(Test_StemmerTest, self).setUp()

    def get_test_data(self):
        data = []

        data.append(['kebijakan', 'bijak'])
        #//data.append(['karyawan', 'karya'])
        #//data.append(['karyawati', 'karya'])
        data.append(['kinerja', 'kerja'])
        data.append(['mengandung', 'kandung'])
        data.append(['memakan', 'makan'])
        data.append(['asean', 'asean'])
        data.append(['pemandu', 'pandu'])
        data.append(['mengurangi', 'kurang'])
        data.append(['pemerintah', 'perintah'])
        data.append(['mengabulkan', 'kabul'])
        data.append(['mengupas', 'kupas'])
        data.append(['keterpurukan', 'puruk'])
        data.append(['ditemukan', 'temu'])
        data.append(['mengerti', 'erti'])
        data.append(['kebon', 'kebon'])
        data.append(['terdepan', 'depan'])
        data.append(['mengikis', 'kikis'])
        data.append(['kedudukan', 'duduk'])
        data.append(['menekan', 'tekan'])
        data.append(['perusakan', 'rusa']) # overstemming, it's better than perusa
        data.append(['ditemui', 'temu'])
        data.append(['di', 'di'])
        data.append(['mengalahkan', 'kalah'])
        data.append(['melewati', 'lewat'])
        data.append(['bernafas', 'nafas'])
        data.append(['meniru-niru', 'tiru'])
        data.append(['memanggil-manggil', 'panggil'])
        data.append(['menyebut-nyebut', 'sebut'])
        data.append(['menganga', 'nganga'])
        data.append(['besaran', 'besar'])
        data.append(['terhenyak', 'henyak'])
        data.append(['mengokohkan', 'kokoh'])
        data.append(['melainkan', 'lain'])
        data.append(['kuasa-Mu', 'kuasa'])
        data.append(['malaikat-malaikat-Nya', 'malaikat'])
        data.append(['nikmat-Ku', 'nikmat'])

        return data

    def try_stem(self, word, stem):
        self.assertEquals(stem, self.stemmer.stem(word))

    def test_stem(self):
        data = self.get_test_data()
        for d in data:
            self.try_stem(d[0], d[1])

if __name__ == '__main__':
    unittest.main()
