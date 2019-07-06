"""
This module contains all stemming rules.
"""

import re
from collections import namedtuple


def isPAS(word):
    """
    Check if Precedence Adjustment Specification is satisfied by word.

    Confix Stripping Rule Precedence Adjustment Specification.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval" page 78-79.
    @link  http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    regex_rules = [
        r'^be(.*)lah$',
        r'^be(.*)an$',
        r'^(me|di|pe|ter)(.*)i$']

    for rule in regex_rules:
        if re.match(rule, word):
            return True
    return False


def isIAPS(word):
    """
    Check if Invalid Affix Pair Specification is satisfied by word.

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 26
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    if re.match(r'^me(.*)kan$', word):
        return False

    if word == 'ketahui':
        return False

    invalid_affixes = [r'^ber(.*)i$',
                       r'^di(.*)an$',
                       r'^ke(.*)i$',
                       r'^ke(.*)an$',
                       r'^me(.*)an$',
                       r'^me(.*)an$',
                       r'^ter(.*)an$',
                       r'^per(.*)an$']

    for affix in invalid_affixes:
        if re.match(affix, word):
            return True
    return False


def DontStemShortWord(context):
    """
    Stop stemming process if word length is less than 4.
    """

    if len(context.current_word) <= 3:
        context.stop_process()


def RemoveInflectionalParticle(context):
    """
    Remove Inflectional particle (lah|kah|tah|pun).

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 60
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    result = re.sub(r'-*(lah|kah|tah|pun)$', '', context.current_word, 1)
    if result != context.current_word:
        removed_part = re.sub(result, '', context.current_word, 1)
        removal = Removal(context.current_word, result, removed_part, 'P')

        context.add_removal(removal)
        context.current_word = result


def RemoveInflectionalPossessivePronoun(context):
    """
    Remove inflectional possessive pronoun (ku|mu|nya|-ku|-mu|-nya).

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 60
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    result = re.sub(r'-*(ku|mu|nya)$', '', context.current_word, 1)
    if result != context.current_word:
        removed_part = re.sub(result, '', context.current_word, 1)
        removal = Removal(context.current_word, result, removed_part, 'PP')

        context.add_removal(removal)
        context.current_word = result


def RemoveDerivationalSuffix(context):
    """
    Remove derivational suffix.

    Original rule : i|kan|an
    Added the adopted foreign suffix rule : is|isme|isasi
    Added the adopted suffix rule : wan|wati

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 61
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    # unable to stem "some rare cases when the root words change after being
    # attached to these suffixes. For example, adding the suffix '-wan' to the
    # word 'sejarah' <history> results in the word 'sejarawan' <historian>"

    result = re.sub(r'(wan|wati|is|isme|isasi)$', '', context.current_word, 1)
    if result in context.dictionary:
        removed_part = re.sub(result, '', context.current_word, 1)
        removal = Removal(context.current_word, result, removed_part, 'DS')

        context.add_removal(removal)
        context.current_word = result
        return

    result = re.sub(r'(i|kan|an)$', '', context.current_word, 1)
    if result != context.current_word:
        removed_part = re.sub(result, '', context.current_word, 1)
        removal = Removal(context.current_word, result, removed_part, 'DS')

        context.add_removal(removal)
        context.current_word = result


def RemovePlainPrefix(context):
    """
    Remove plain prefix (di|ke|se).

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 61
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    result = re.sub(r'^(di|ke|se)', '', context.current_word, 1)
    if result != context.current_word:
        removed_part = re.sub(result, '', context.current_word, 1)
        removal = Removal(context.current_word, result, removed_part, 'DP')

        context.add_removal(removal)
        context.current_word = result


class PrefixDisambiguator():
    """
    Wrapper for Disambiguate Prefix Rule.
    """

    def __init__(self, rules):
        self.rules = rules

    def visit(self, context):
        """
        Accept disambiguate prefix rule(s).
        """

        result = None

        for rule in self.rules:
            removed_part, result = rule(context.current_word)
            if result in context.dictionary:
                break

        if result is None:
            return None

        removal = Removal(context.current_word, result, removed_part, 'DP')

        context.add_removal(removal)
        context.current_word = result
        return None

    @staticmethod
    def rule01a(word):
        """
        Disambiguate Prefix Rule 1a
        Rule 1a : berV -> ber-V
        """
        matches = re.match(r'^ber([aiueo].*)$', word)
        if matches:
            return 'ber', matches.group(1)
        return None, None

    @staticmethod
    def rule01b(word):
        """
        Disambiguate Prefix Rule 1b
        Rule 1b : berV -> be-rV
        """
        matches = re.match(r'^ber([aiueo].*)$', word)
        if matches:
            return 'ber', 'r' + matches.group(1)
        return None, None

    @staticmethod
    def rule02(word):
        """
        Disambiguate Prefix Rule 2
        Rule 2 : berCAP -> ber-CAP where C != 'r' AND P != 'er'
        """
        matches = re.match(r'^ber([bcdfghjklmnpqrstvwxyz])([a-z])(.*)', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(3)):
                return None, None

            return 'ber', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule03(word):
        """
        Disambiguate Prefix Rule 3
        Rule 3 : berCAerV -> ber-CAerV where C != 'r'
        """
        matches = re.match(r'ber([bcdfghjklmnpqrstvwxyz])([a-z])er([aiueo])(.*)', word)
        if matches:
            if matches.group(1) == 'r':
                return None, None

            return 'ber', matches.group(1) + matches.group(2) + 'er' \
                          + matches.group(3) + matches.group(4)
        return None, None

    @staticmethod
    def rule04(word):
        """
        Disambiguate Prefix Rule 4
        Rule 4 : belajar  -> bel-ajar
                 belunjur -> bel-unjur
        """
        if word == 'belajar':
            return 'ber', 'ajar'
        if word == 'belunjur':
            return 'ber', 'unjur'
        return None, None

    @staticmethod
    def rule05(word):
        """
        Disambiguate Prefix Rule 5
        Rule 5 : beC1erC2 -> be-C1erC2 where C1 != 'r'
        """
        matches = re.match(r'be([bcdfghjklmnpqstvwxyz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return 'be', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule06a(word):
        """
        Disambiguate Prefix Rule 6a
        Rule 6a : terV -> ter-V
        """
        matches = re.match(r'^ter([aiueo].*)$', word)
        if matches:
            return 'ter', matches.group(1)
        return None, None

    @staticmethod
    def rule06b(word):
        """
        Disambiguate Prefix Rule 6b
        Rule 6b : terV -> te-rV
        """
        matches = re.match(r'^ter([aiueo].*)$', word)
        if matches:
            return 'ter', 'r' + matches.group(1)
        return None, None

    @staticmethod
    def rule07(word):
        """
        Disambiguate Prefix Rule 7
        Rule 7 : terCerv -> ter-CerV where C != 'r'
        """
        matches = re.match(r'^ter([bcdfghjklmnpqrstvwxyz])er([aiueo].*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return None
            return 'ter', matches.group(1) + 'er' + matches.group(2)
        return None, None

    @staticmethod
    def rule08(word):
        """
        Disambiguate Prefix Rule 8
        Rule 8 : terCP -> ter-CP where C != 'r' and P != 'er'
        """
        matches = re.match(r'^ter([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if matches.group(1) == 'r' or re.match(r'^er(.*)$', matches.group(2)):
                return None, None
            return 'ter', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule09(word):
        """
        Disambiguate Prefix Rule 9
        Rule 9 : te-C1erC2 -> te-C1erC2 where C1 != 'r'
        """
        matches = re.match(r'^te([bcdfghjklmnpqrstvwxyz])er([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return None
            return 'te', matches.group(1) + 'er' + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule10(word):
        """
        Disambiguate Prefix Rule 10
        Rule 10 : me{l|r|w|y}V -> me-{l|r|w|y}V
        """
        matches = re.match(r'^me([lrwy])([aiueo])(.*)$', word)
        if matches:
            return 'me', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule11(word):
        """
        Disambiguate Prefix Rule 11
        Rule 11 : mem{b|f|v} -> mem-{b|f|v}
        """
        matches = re.match(r'^mem([bfv])(.*)$', word)
        if matches:
            return 'me', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule12(word):
        """
        Disambiguate Prefix Rule 12
        Nazief and Adriani Rule 12 : beC1erC2 -> be-C1erC2 where C1 != 'r'
        Modified by Jelita Asian's CS Rule 12 : mempe -> mem-pe to stem mempengaruhi
        """
        matches = re.match(r'^mempe(.*)$', word)
        if matches:
            return 'me', 'pe' + matches.group(1)
        return None, None

    @staticmethod
    def rule13a(word):
        """
        Disambiguate Prefix Rule 13a
        Rule 13a : mem{rV|V} -> me-m{rV|V}
        """
        matches = re.match(r'^mem([aiueo])(.*)$', word)
        if matches:
            return 'me', 'm' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule13b(word):
        """
        Disambiguate Prefix Rule 13b
        Rule 13b : mem{rV|V} -> me-p{rV|V}
        """
        matches = re.match(r'^mem([aiueo])(.*)$', word)
        if matches:
            return 'me', 'p' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule14(word):
        """
        Disambiguate Prefix Rule 14
        Rule 14 modified by Andy Librian : men{c|d|j|s|t|z} -> men-{c|d|j|s|t|z}
        in order to stem mentaati

        Rule 14 modified by ECS: men{c|d|j|s|z} -> men-{c|d|j|s|z}
        in order to stem mensyaratkan, mensyukuri

        Original CS Rule no 14 was : men{c|d|j|z} -> men-{c|d|j|z}
        """
        matches = re.match(r'^men([cdjstz])(.*)$', word)
        if matches:
            return 'me', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule15a(word):
        """
        Disambiguate Prefix Rule 15a
        Rule 15a : men{V} -> me-n{V}
        """
        matches = re.match(r'^men([aiueo])(.*)$', word)
        if matches:
            return 'me', 'n' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule15b(word):
        """
        Disambiguate Prefix Rule 15b
        Rule 15b : men{V} -> me-t{V}
        """
        matches = re.match(r'^men([aiueo])(.*)$', word)
        if matches:
            return 'me', 't' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule16(word):
        """
        Disambiguate Prefix Rule 16
        Original Nazief and Adriani's Rule 16 : meng{g|h|q} -> meng-{g|h|q}
        Modified Jelita Asian's CS Rule 16 : meng{g|h|q|k} -> meng-{g|h|q|k} to stem mengkritik
        """
        matches = re.match(r'^meng([g|h|q|k])(.*)$', word)
        if matches:
            return 'me', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule17a(word):
        """
        Disambiguate Prefix Rule 17a
        Rule 17a : mengV -> meng-V
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return 'me', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule17b(word):
        """
        Disambiguate Prefix Rule 17b
        Rule 17b : mengV -> meng-kV
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return 'me', 'k' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule17c(word):
        """
        Disambiguate Prefix Rule 17c
        Rule 17c : mengV -> meng-V- where V = 'e'
        """
        matches = re.match(r'^menge(.*)$', word)
        if matches:
            return 'me', matches.group(1)
        return None, None

    @staticmethod
    def rule17d(word):
        """
        Disambiguate Prefix Rule 17d
        Rule 17d : mengV -> me-ngV
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return 'me', 'ng' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule18a(word):
        """
        Disambiguate Prefix Rule 18a
        Rule 18a : menyV -> me-nyV to stem menyala -> nyala
        """
        matches = re.match(r'^meny([aiueo])(.*)$', word)
        if matches:
            return 'me', 'ny' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule18b(word):
        """
        Disambiguate Prefix Rule 18b
        Original Rule 18 : menyV -> meny-sV
        Modified by CC (shifted into 18b, see also 18a)
        """
        matches = re.match(r'^meny([aiueo])(.*)$', word)
        if matches:
            return 'me', 's' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule19(word):
        """
        Disambiguate Prefix Rule 19
        Original Rule 19 : mempV -> mem-pV where V != 'e'
        Modified Rule 19 by ECS : mempA -> mem-pA where A != 'e' in order to stem memproteksi
        """
        matches = re.match(r'^memp([abcdfghijklmopqrstuvwxyz])(.*)$', word)
        if matches:
            return 'me', 'p' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule20(word):
        """
        Disambiguate Prefix Rule 20
        Rule 20 : pe{w|y}V -> pe-{w|y}V
        """
        matches = re.match(r'^pe([wy])([aiueo])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule21a(word):
        """
        Disambiguate Prefix Rule 21a
        Rule 21a : perV -> per-V
        """
        matches = re.match(r'^per([aiueo])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule21b(word):
        """
        Disambiguate Prefix Rule 21b
        Rule 21b : perV -> pe-rV
        """
        matches = re.match(r'^pe(r[aiueo])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule23(word):
        """
        Disambiguate Prefix Rule 23
        Rule 23 : perCAP -> per-CAP where C != 'r' AND P != 'er'
        """
        matches = re.match(r'^per([bcdfghjklmnpqrstvwxyz])([a-z])(.*)$', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(3)):
                return None, None
            return 'pe', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule24(word):
        """
        Disambiguate Prefix Rule 24
        Rule 24 : perCAerV -> per-CAerV where C != 'r'
        """
        matches = re.match(r'^per([bcdfghjklmnpqrstvwxyz])([a-z])er([aiueo])(.*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return None, None
            return 'pe', matches.group(1) + matches.group(2) + 'er' \
                         + matches.group(3) + matches.group(4)
        return None, None

    @staticmethod
    def rule25(word):
        """
        Disambiguate Prefix Rule 25
        Rule 25 : pem{b|f|v} -> pem-{b|f|v}
        """
        matches = re.match(r'^pem([bfv])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule26a(word):
        """
        Disambiguate Prefix Rule 26a
        Rule 26a : pem{rV|V} -> pe-m{rV|V}
        """
        matches = re.match(r'^pem([aiueo])(.*)$', word)
        if matches:
            return 'pe', 'm' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule26b(word):
        """
        Disambiguate Prefix Rule 26b
        Rule 26b : pem{rV|V} -> pe-p{rV|V}
        """
        matches = re.match(r'^pem([aiueo])(.*)$', word)
        if matches:
            return 'pe', 'p' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule27(word):
        """
        Disambiguate Prefix Rule 27
        Rule 27 modified by Prasasto Adi : pen{c|d|j|s|t|z} -> pen-{c|d|j|s|t|z}
        in order to stem penstabilan, pentranskripsi

        Original CS Rule 27 was : pen{c|d|j|z} -> pen-{c|d|j|z}
        """
        matches = re.match(r'^pen([cdjstz])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule28a(word):
        """
        Disambiguate Prefix Rule 28a
        Rule 28a : pen{V} -> pe-n{V}
        """
        matches = re.match(r'^pen([aiueo])(.*)$', word)
        if matches:
            return 'pe', 'n' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule28b(word):
        """
        Disambiguate Prefix Rule 28b
        Rule 28b : pen{V} -> pe-t{V}
        """
        matches = re.match(r'^pen([aiueo])(.*)$', word)
        if matches:
            return 'pe', 't' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule29(word):
        """
        Disambiguate Prefix Rule 29
        Original Rule 29 : peng{g|h|q} -> peng-{g|h|q}
        Modified Rule 29 by ECS : pengC -> peng-C
        """
        matches = re.match(r'^peng([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule30a(word):
        """
        Disambiguate Prefix Rule 30a
        Rule 30a : pengV -> peng-V
        """
        matches = re.match(r'^peng([aiueo])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule30b(word):
        """
        Disambiguate Prefix Rule 30b
        Rule 30a : pengV -> peng-kV
        """
        matches = re.match(r'^peng([aiueo])(.*)$', word)
        if matches:
            return 'pe', 'k' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule30c(word):
        """
        Disambiguate Prefix Rule 30c
        Rule 30a : pengV -> pengV- where V = 'e'
        """
        matches = re.match(r'^penge(.*)$', word)
        if matches:
            return 'pe', matches.group(1)
        return None, None

    @staticmethod
    def rule31a(word):
        """
        Disambiguate Prefix Rule 31a
        Rule 31a : penyV -> pe-nyV
        """
        matches = re.match(r'^peny([aiueo])(.*)$', word)
        if matches:
            return 'pe', 'ny' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule31b(word):
        """
        Disambiguate Prefix Rule 31b
        Original Rule 31 : penyV -> peny-sV
        Modified by CC, shifted to 31b
        """
        matches = re.match(r'^peny([aiueo])(.*)$', word)
        if matches:
            return 'pe', 's' + matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule32(word):
        """
        Disambiguate Prefix Rule 32
        Rule 32 : pelV -> pe-lV except pelajar -> ajar
        """
        if word == 'pelajar':
            return 'pe', 'ajar'
        matches = re.match(r'^pe(l[aiueo])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule34(word):
        """
        Disambiguate Prefix Rule 34
        Rule 34 : peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
        """
        matches = re.match(r'^pe([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(2)):
                return None, None
            return 'pe', matches.group(1) + matches.group(2)
        return None, None

    @staticmethod
    def rule35(word):
        """
        Disambiguate Prefix Rule 35
        Rule 35 : terC1erC2 -> ter-C1erC2 where C1 != {r}
        """
        matches = re.match(r'^ter([bcdfghjkpqstvxz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return 'ter', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule36(word):
        """
        Disambiguate Prefix Rule 36
        Rule 36 : peC1erC2 -> pe-C1erC2 where C1 != {r|w|y|l|m|n}
        """
        matches = re.match(r'^pe([bcdfghjkpqstvxz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return 'pe', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule37a(word):
        """
        Disambiguate Prefix Rule 37a (CC infix rules)
        Rule 37a : CerV -> CerV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(er[aiueo])(.*)$', word)
        if matches:
            return 'er', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule37b(word):
        """
        Disambiguate Prefix Rule 37b (CC infix rules)
        Rule 37b : CerV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])er([aiueo])(.*)$', word)
        if matches:
            return 'er', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule38a(word):
        """
        Disambiguate Prefix Rule 38a (CC infix rules)
        Rule 38a : CelV -> CelV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(el[aiueo])(.*)$', word)
        if matches:
            return 'el', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule38b(word):
        """
        Disambiguate Prefix Rule 38b (CC infix rules)
        Rule 38b : CelV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])el([aiueo])(.*)$', word)
        if matches:
            return 'el', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule39a(word):
        """
        Disambiguate Prefix Rule 39a (CC infix rules)
        Rule 39a : CemV -> CemV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(em[aiueo])(.*)$', word)
        if matches:
            return 'em', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule39b(word):
        """
        Disambiguate Prefix Rule 39b (CC infix rules)
        Rule 39b : CemV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])em([aiueo])(.*)$', word)
        if matches:
            return 'em', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule40a(word):
        """
        Disambiguate Prefix Rule 40a (CC infix rules)
        Rule 40a : CinV -> CinV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(in[aiueo])(.*)$', word)
        if matches:
            return 'in', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule40b(word):
        """
        Disambiguate Prefix Rule 40b (CC infix rules)
        Rule 40b : CinV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])in([aiueo])(.*)$', word)
        if matches:
            return 'in', matches.group(1) + matches.group(2) + matches.group(3)
        return None, None

    @staticmethod
    def rule41(word):
        """
        Disambiguate Prefix Rule 41
        Rule 41 : kuA -> ku-A
        """
        matches = re.match(r'^ku(.*)$', word)
        if matches:
            return 'ku', matches.group(1)
        return None, None

    @staticmethod
    def rule42(word):
        """
        Disambiguate Prefix Rule 42
        Rule 42 : kauA -> kau-A
        """
        matches = re.match(r'^kau(.*)$', word)
        if matches:
            return 'kau', matches.group(1)
        return None, None


Removal = namedtuple('Removal', 'subject result removedPart affixType')


_visitors = [DontStemShortWord]

# {lah|kah|tah|pun}, {ku|mu|nya}, {i|kan|an}
_suffix_visitors = [RemoveInflectionalParticle,
                    RemoveInflectionalPossessivePronoun,
                    RemoveDerivationalSuffix]

# {di|ke|se}
_prefix_visitors = [RemovePlainPrefix]

# Add all rules in rules_disambiguator to prefix_visitors
for _num in range(1, 43):

    # group rule(s) by its number
    _rules = [getattr(PrefixDisambiguator, rule) for rule in dir(PrefixDisambiguator)
              if str(_num).zfill(2) in rule]

    if _rules:
        _prefix_visitors.append(PrefixDisambiguator(_rules).visit)

VisitorProvider = namedtuple('VP', 'visitors suffix_visitors prefix_visitors')
VisitorProvider = VisitorProvider(_visitors, _suffix_visitors, _prefix_visitors)
