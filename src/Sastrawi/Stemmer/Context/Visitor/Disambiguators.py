import re
from Sastrawi.Stemmer.Context.Removal import Removal

class PrefixDisambiguator(object):
    def __init__(self, rule_list):
        self.rule_list = rule_list

    def visit(self, context):
        result = None

        for rule in self.rule_list:
            result = rule(context.current_word)
            if context.dictionary.contains(result):
                break

        if not result:
            return

        removedPart = re.sub(result, '', context.current_word, 1)
        removal = Removal(self, context.current_word, result, removedPart, 'DP')

        context.add_removal(removal)
        context.current_word = result


class DisambiguatorsPrefixRule():
    def rule1a(self, word):
        """Disambiguate Prefix Rule 1a
        Rule 1a : berV -> ber-V
        """
        matches = re.match(r'^ber([aiueo].*)$', word)
        if matches:
            return matches.group(1)
        return None

    def rule1b(self, word):
        """Disambiguate Prefix Rule 1b
        Rule 1b : berV -> be-rV
        """
        matches = re.match(r'^ber([aiueo].*)$', word)
        if matches:
            return 'r' + matches.group(1)
        return None

    def rule2(self, word):
        """Disambiguate Prefix Rule 2
        Rule 2 : berCAP -> ber-CAP where C != 'r' AND P != 'er'
        """
        matches = re.match(r'^ber([bcdfghjklmnpqrstvwxyz])([a-z])(.*)', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(3)):
                return None

            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule3(self, word):
        """Disambiguate Prefix Rule 3
        Rule 3 : berCAerV -> ber-CAerV where C != 'r'
        """
        matches = re.match(r'ber([bcdfghjklmnpqrstvwxyz])([a-z])er([aiueo])(.*)', word)
        if matches:
            if matches.group(1) == 'r':
                return None

            return matches.group(1) + matches.group(2) + 'er' + matches.group(3) + matches.group(4)
        return None

    def rule4(self, word):
        """Disambiguate Prefix Rule 4
        Rule 4 : belajar -> bel-ajar
        """
        if word == 'belajar':
            return 'ajar'
        return None

    def rule5(self, word):
        """Disambiguate Prefix Rule 5
        Rule 5 : beC1erC2 -> be-C1erC2 where C1 != 'r'
        """
        matches = re.match(r'be([bcdfghjklmnpqstvwxyz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule6a(self, word):
        """Disambiguate Prefix Rule 6a
        Rule 6a : terV -> ter-V
        """
        matches = re.match(r'^ter([aiueo].*)$', word)
        if matches:
            return matches.group(1)
        return None

    def rule6b(self, word):
        """Disambiguate Prefix Rule 6b
        Rule 6b : terV -> te-rV
        """
        matches = re.match(r'^ter([aiueo].*)$', word)
        if matches:
            return 'r' + matches.group(1)
        return None

    def rule7(self, word):
        """Disambiguate Prefix Rule 7
        Rule 7 : terCerv -> ter-CerV where C != 'r'
        """
        matches = re.match(r'^ter([bcdfghjklmnpqrstvwxyz])er([aiueo].*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return None
            return matches.group(1) + 'er' + matches.group(2)
        return None

    def rule8(self, word):
        """Disambiguate Prefix Rule 8
        Rule 8 : terCP -> ter-CP where C != 'r' and P != 'er'
        """
        matches = re.match(r'^ter([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if matches.group(1) == 'r' or re.match(r'^er(.*)$', matches.group(2)):
                return None
            return matches.group(1) + matches.group(2)
        return None

    def rule9(self, word):
        """Disambiguate Prefix Rule 9
        Rule 9 : te-C1erC2 -> te-C1erC2 where C1 != 'r'
        """
        matches = re.match(r'^te([bcdfghjklmnpqrstvwxyz])er([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return None
            return matches.group(1) + 'er' + matches.group(2) + matches.group(3)
        return None

    def rule10(self, word):
        """Disambiguate Prefix Rule 10
        Rule 10 : me{l|r|w|y}V -> me-{l|r|w|y}V
        """
        matches = re.match(r'^me([lrwy])([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule11(self, word):
        """Disambiguate Prefix Rule 11
        Rule 11 : mem{b|f|v} -> mem-{b|f|v}
        """
        matches = re.match(r'^mem([bfv])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule12(self, word):
        """Disambiguate Prefix Rule 12
        Nazief and Adriani Rule 12 : beC1erC2 -> be-C1erC2 where C1 != 'r'
        Modified by Jelita Asian's CS Rule 12 : mempe -> mem-pe to stem mempengaruhi
        """
        matches = re.match(r'^mempe(.*)$', word)
        if matches:
            return 'pe' + matches.group(1)
        return None

    def rule13a(self, word):
        """Disambiguate Prefix Rule 13a
        Rule 13a : mem{rV|V} -> me-m{rV|V}
        """
        matches = re.match(r'^mem([aiueo])(.*)$', word)
        if matches:
            return 'm' + matches.group(1) + matches.group(2)
        return None

    def rule13b(self, word):
        """Disambiguate Prefix Rule 13b
        Rule 13b : mem{rV|V} -> me-p{rV|V}
        """
        matches = re.match(r'^mem([aiueo])(.*)$', word)
        if matches:
            return 'p' + matches.group(1) + matches.group(2)
        return None

    def rule14(self, word):
        """Disambiguate Prefix Rule 14
        Rule 14 modified by Andy Librian : men{c|d|j|s|t|z} -> men-{c|d|j|s|t|z}
        in order to stem mentaati

        Rule 14 modified by ECS: men{c|d|j|s|z} -> men-{c|d|j|s|z}
        in order to stem mensyaratkan, mensyukuri

        Original CS Rule no 14 was : men{c|d|j|z} -> men-{c|d|j|z}
        """
        matches = re.match(r'^men([cdjstz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule15a(self, word):
        """Disambiguate Prefix Rule 15a
        Rule 15a : men{V} -> me-n{V}
        """
        matches = re.match(r'^men([aiueo])(.*)$', word)
        if matches:
            return 'n' + matches.group(1) + matches.group(2)
        return None

    def rule15b(self, word):
        """Disambiguate Prefix Rule 15b
        Rule 15b : men{V} -> me-t{V}
        """
        matches = re.match(r'^men([aiueo])(.*)$', word)
        if matches:
            return 't' + matches.group(1) + matches.group(2)
        return None

    def rule16(self, word):
        """Disambiguate Prefix Rule 16
        Original Nazief and Adriani's Rule 16 : meng{g|h|q} -> meng-{g|h|q}
        Modified Jelita Asian's CS Rule 16 : meng{g|h|q|k} -> meng-{g|h|q|k} to stem mengkritik
        """
        matches = re.match(r'^meng([g|h|q|k])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule17a(self, word):
        """Disambiguate Prefix Rule 17a
        Rule 17a : mengV -> meng-V
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule17b(self, word):
        """Disambiguate Prefix Rule 17b
        Rule 17b : mengV -> meng-kV
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return 'k' + matches.group(1) + matches.group(2)
        return None

    def rule17c(self, word):
        """Disambiguate Prefix Rule 17c
        Rule 17c : mengV -> meng-V- where V = 'e'
        """
        matches = re.match(r'^menge(.*)$', word)
        if matches:
            return matches.group(1)
        return None

    def rule17d(self, word):
        """Disambiguate Prefix Rule 17d
        Rule 17d : mengV -> me-ngV
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return 'ng' + matches.group(1) + matches.group(2)
        return None

    def rule18a(self, word):
        """Disambiguate Prefix Rule 18a
        Rule 18a : menyV -> me-nyV to stem menyala -> nyala
        """
        matches = re.match(r'^meny([aiueo])(.*)$', word)
        if matches:
            return 'ny' + matches.group(1) + matches.group(2)
        return None

    def rule18b(self, word):
        """Disambiguate Prefix Rule 18b
        Original Rule 18 : menyV -> meny-sV
        Modified by CC (shifted into 18b, see also 18a)
        """
        matches = re.match(r'^meny([aiueo])(.*)$', word)
        if matches:
            return 's' + matches.group(1) + matches.group(2)
        return None

    def rule19(self, word):
        """Disambiguate Prefix Rule 19
        Original Rule 19 : mempV -> mem-pV where V != 'e'
        Modified Rule 19 by ECS : mempA -> mem-pA where A != 'e' in order to stem memproteksi
        """
        matches = re.match(r'^memp([abcdfghijklmopqrstuvwxyz])(.*)$', word)
        if matches:
            return 'p' + matches.group(1) + matches.group(2)
        return None

    def rule20(self, word):
        """Disambiguate Prefix Rule 20
        Rule 20 : pe{w|y}V -> pe-{w|y}V
        """
        matches = re.match(r'^pe([wy])([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule21a(self, word):
        """Disambiguate Prefix Rule 21a
        Rule 21a : perV -> per-V
        """
        matches = re.match(r'^per([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule21b(self, word):
        """Disambiguate Prefix Rule 21b
        Rule 21b : perV -> pe-rV
        """
        matches = re.match(r'^pe(r[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule23(self, word):
        """Disambiguate Prefix Rule 23
        Rule 23 : perCAP -> per-CAP where C != 'r' AND P != 'er'
        """
        matches = re.match(r'^per([bcdfghjklmnpqrstvwxyz])([a-z])(.*)$', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(3)):
                return None
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule24(self, word):
        """Disambiguate Prefix Rule 24
        Rule 24 : perCAerV -> per-CAerV where C != 'r'
        """
        matches = re.match(r'^per([bcdfghjklmnpqrstvwxyz])([a-z])er([aiueo])(.*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return None
            return matches.group(1) + matches.group(2) + 'er' + matches.group(3) + matches.group(4)
        return None

    def rule25(self, word):
        """Disambiguate Prefix Rule 25
        Rule 25 : pem{b|f|v} -> pem-{b|f|v}
        """
        matches = re.match(r'^pem([bfv])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule26a(self, word):
        """Disambiguate Prefix Rule 26a
        Rule 26a : pem{rV|V} -> pe-m{rV|V}
        """
        matches = re.match(r'^pem([aiueo])(.*)$', word)
        if matches:
            return 'm' + matches.group(1) + matches.group(2)
        return None

    def rule26b(self, word):
        """Disambiguate Prefix Rule 26b
        Rule 26b : pem{rV|V} -> pe-p{rV|V}
        """
        matches = re.match(r'^pem([aiueo])(.*)$', word)
        if matches:
            return 'p' + matches.group(1) + matches.group(2)
        return None

    def rule27(self, word):
        """Disambiguate Prefix Rule 27
        Rule 27 modified by Prasasto Adi : pen{c|d|j|s|t|z} -> pen-{c|d|j|s|t|z}
        in order to stem penstabilan, pentranskripsi

        Original CS Rule 27 was : pen{c|d|j|z} -> pen-{c|d|j|z}
        """
        matches = re.match(r'^pen([cdjstz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule28a(self, word):
        """Disambiguate Prefix Rule 28a
        Rule 28a : pen{V} -> pe-n{V}
        """
        matches = re.match(r'^pen([aiueo])(.*)$', word)
        if matches:
            return 'n' + matches.group(1) + matches.group(2)
        return None

    def rule28b(self, word):
        """Disambiguate Prefix Rule 28b
        Rule 28b : pen{V} -> pe-t{V}
        """
        matches = re.match(r'^pen([aiueo])(.*)$', word)
        if matches:
            return 't' + matches.group(1) + matches.group(2)
        return None

    def rule29(self, word):
        """Disambiguate Prefix Rule 29
        Original Rule 29 : peng{g|h|q} -> peng-{g|h|q}
        Modified Rule 29 by ECS : pengC -> peng-C
        """
        matches = re.match(r'^peng([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule30a(self, word):
        """Disambiguate Prefix Rule 30a
        Rule 30a : pengV -> peng-V
        """
        matches = re.match(r'^peng([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule30b(self, word):
        """Disambiguate Prefix Rule 30b
        Rule 30a : pengV -> peng-kV
        """
        matches = re.match(r'^peng([aiueo])(.*)$', word)
        if matches:
            return 'k' + matches.group(1) + matches.group(2)
        return None

    def rule30c(self, word):
        """Disambiguate Prefix Rule 30c
        Rule 30a : pengV -> pengV- where V = 'e'
        """
        matches = re.match(r'^penge(.*)$', word)
        if matches:
            return matches.group(1)
        return None

    def rule31a(self, word):
        """Disambiguate Prefix Rule 31a
        Rule 31a : penyV -> pe-nyV
        """
        matches = re.match(r'^peny([aiueo])(.*)$', word)
        if matches:
            return 'ny' + matches.group(1) + matches.group(2)
        return None

    def rule31b(self, word):
        """Disambiguate Prefix Rule 31b
        Original Rule 31 : penyV -> peny-sV
        Modified by CC, shifted to 31b
        """
        matches = re.match(r'^peny([aiueo])(.*)$', word)
        if matches:
            return 's' + matches.group(1) + matches.group(2)
        return None

    def rule32(self, word):
        """Disambiguate Prefix Rule 32
        Rule 32 : pelV -> pe-lV except pelajar -> ajar
        """
        if word == 'pelajar':
            return 'ajar'
        matches = re.match(r'^pe(l[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
        return None

    def rule34(self, word):
        """Disambiguate Prefix Rule 34
        Rule 34 : peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
        """
        matches = re.match(r'^pe([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(2)):
                return None
            return matches.group(1) + matches.group(2)
        return None

    def rule35(self, word):
        """Disambiguate Prefix Rule 35
        Rule 35 : terC1erC2 -> ter-C1erC2 where C1 != {r}
        """
        matches = re.match(r'^ter([bcdfghjkpqstvxz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule36(self, word):
        """Disambiguate Prefix Rule 36
        Rule 36 : peC1erC2 -> pe-C1erC2 where C1 != {r|w|y|l|m|n}
        """
        matches = re.match(r'^pe([bcdfghjkpqstvxz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule37a(self, word):
        """Disambiguate Prefix Rule 37a (CC infix rules)
        Rule 37a : CerV -> CerV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(er[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule37b(self, word):
        """Disambiguate Prefix Rule 37b (CC infix rules)
        Rule 37b : CerV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])er([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule38a(self, word):
        """Disambiguate Prefix Rule 38a (CC infix rules)
        Rule 38a : CelV -> CelV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(el[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule38b(self, word):
        """Disambiguate Prefix Rule 38b (CC infix rules)
        Rule 38b : CelV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])el([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule39a(self, word):
        """Disambiguate Prefix Rule 39a (CC infix rules)
        Rule 39a : CemV -> CemV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(em[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule39b(self, word):
        """Disambiguate Prefix Rule 39b (CC infix rules)
        Rule 39b : CemV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])em([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule40a(self, word):
        """Disambiguate Prefix Rule 40a (CC infix rules)
        Rule 40a : CinV -> CinV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(in[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule40b(self, word):
        """Disambiguate Prefix Rule 40b (CC infix rules)
        Rule 40b : CinV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])in([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
        return None

    def rule41(self, word):
        """Disambiguate Prefix Rule 41
        Rule 41 : kuA -> ku-A
        """
        matches = re.match(r'^ku(.*)$', word)
        if matches:
            return matches.group(1)
        return None

    def rule42(self, word):
        """Disambiguate Prefix Rule 42
        Rule 42 : kauA -> kau-A
        """
        matches = re.match(r'^kau(.*)$', word)
        if matches:
            return matches.group(1)
        return None
