"""
This module contains classes for stemming purpose.
"""

import re
import os
import sastrawi.rules as Rules


class Stemmer():
    """
    Indonesian sentence stemmer.

    Nazief & Adriani, CS Stemmer, ECS Stemmer, Improved ECS.
    @link https://github.com/sastrawi/sastrawi/wiki/Resources
    """

    def __init__(self, rootwords=None, stopwords=None):

        current_dir = os.path.dirname(os.path.realpath(__file__))
        err_msg = '{} is missing. It seems that your installation is corrupted'

        if rootwords is None:
            try:
                filepath = '/data/rootwords.txt'
                with open(current_dir + filepath, 'r') as file:
                    words = file.read().split('\n')
                    self.rootwords = set(words)
            except FileNotFoundError:
                raise RuntimeError(err_msg.format(filepath)) from None
        else:
            self.rootwords = rootwords

        if stopwords is None:
            try:
                filepath = '/data/stopwords.txt'
                with open(current_dir + filepath, 'r') as file:
                    words = file.read().split('\n')
                    self.stopwords = set(words)
            except FileNotFoundError:
                raise RuntimeError(err_msg.format(filepath)) from None
        else:
            self.stopwords = stopwords

        self._cache = dict()

    def stem(self, text):
        """
        Stem a text string to its common stem form.
        """
        
        if type(text) != str:
            raise TypeError('text must be a string!')

        # normalize_text
        result = text.lower()  # lower the text even unicode given
        result = re.sub(r'[^a-z0-9 -]', ' ', result, flags=re.IGNORECASE|re.MULTILINE)
        result = re.sub(r'( +)', ' ', result, flags=re.IGNORECASE|re.MULTILINE)
        words = result.strip().split(' ')

        stems = list()

        for word in words:
            if word not in self._cache:
                self._cache[word] = self.context(word)[0]
            stems.append(self._cache[word])

        return ' '.join(stems)

    def remove_stopword(self, text):
        """
        Remove stop words from a text string.
        """

        if type(text) != str:
            raise TypeError('text must be a string!')

        words = text.lower().split(' ')
        stopped_words = [w for w in words if w not in self.stopwords]

        return ' '.join(stopped_words)

    def _is_plural(self, word):
        """
        Check if a word is in plural form.
        """

        # -ku|-mu|-nya
        # nikmat-Ku, etc
        matches = re.match(r'^(.*)-(ku|mu|nya|lah|kah|tah|pun)$', word)
        if matches:
            return matches.group(1).find('-') != -1
        return word.find('-') != -1

    def context(self, word):
        """
        Return simplified Context of the word.
        """

        if type(word) != str:
            raise TypeError('word must be a string!')

        if self._is_plural(word):
            return self._plural_context(word)
        return self._singular_context(word)

    def _plural_context(self, word):

        # check if word is singular
        matches = re.match(r'^(.*)-(.*)$', word)
        if not matches:
            return self._singular_context(word)

        words = [matches.group(1), matches.group(2)]

        # malaikat-malaikat-nya -> malaikat malaikat-nya
        suffix = words[1]
        suffixes = ['ku', 'mu', 'nya', 'lah', 'kah', 'tah', 'pun']
        matches = re.match(r'^(.*)-(.*)$', words[0])
        if suffix in suffixes and matches:
            words[0] = matches.group(1)
            words[1] = matches.group(2) + suffix

        # berbalas-balasan -> balas
        word1, removals1 = self._singular_context(words[0])
        word2, removals2 = self._singular_context(words[1])

        # meniru-nirukan -> tiru
        if not words[1] in self.rootwords and word2 == words[1]:
            word2, removals1 = self._singular_context('me' + words[1])

        if word1 == word2:
            removals = list(set(removals1 + removals2))
            return [word1, removals]

        return [word, list()]

    def _singular_context(self, word):
        t = Context(word, self.rootwords)
        removals = [(r.removedPart, r.affixType) for r in t.removals]
        return [t.result, removals]


class Context():
    """
    Stemming Context using Nazief and Adriani, CS, ECS, Improved ECS.
    """

    def __init__(self, original_word, dictionary):

        self.process_is_stopped = False
        self.original_word = original_word
        self.current_word = original_word
        self.result = ''
        self.dictionary = dictionary
        self.removals = []

        # step 1 - 5
        self._start_stemming_process()

        # step 6
        if self.current_word in self.dictionary:
            self.result = self.current_word
        else:
            self.result = self.original_word
            self.removals = []
        
    def stop_process(self):
        """
        Stop stemming process.
        """
        self.process_is_stopped = True

    def add_removal(self, removal):
        """
        Add Removal information to removals.
        """
        self.removals.append(removal)

    def _start_stemming_process(self):

        # step 1
        if self.current_word in self.dictionary:
            return

        self.accept_visitors(Rules.VisitorProvider.visitors)
        if self.process_is_stopped:
            return

        # Confix Stripping
        # Try to remove prefix before suffix if the specification is met
        if Rules.isPAS(self.original_word):
            # step 4, 5
            self.remove_prefixes()
            if self.process_is_stopped:
                return

            # step 2, 3
            self.remove_suffixes()
            if self.process_is_stopped:
                return

            # if the trial is failed, restore the original word
            # and continue to normal rule precedence (suffix first, prefix afterwards)
            self.current_word = self.original_word
            self.removals = []

        # step 2, 3
        self.remove_suffixes()
        if self.process_is_stopped:
            return

        # step 4, 5
        self.remove_prefixes()
        if self.process_is_stopped:
            return

        # Remove prefixes before ECS pengembalian loop
        if self.removals:
            # return the word before precoding (the subject of first prefix removal)
            self.current_word = self.removals[0].subject

        for removal in self.removals:
            if removal.affixType == 'DP':
                self.removals.remove(removal)

        # ECS loop pengembalian akhiran
        removals = self.removals
        current_word = self.current_word

        for removal in reversed(removals):

            if not self.is_suffix_removal(removal):
                continue

            if removal.removedPart == 'kan':
                self.current_word = removal.result + 'k'

                # step 4,5
                self.remove_prefixes()
                if self.process_is_stopped:
                    return
                self.current_word = removal.result + 'kan'

            else:
                self.current_word = removal.subject

            # step 4,5
            self.remove_prefixes()
            if self.process_is_stopped:
                return

            self.removals = removals
            self.current_word = current_word

    def remove_prefixes(self):
        """
        Accept prefix_visitors rules.
        """
        for try_ in range(3):
            # accept_prefix_visitors
            removal_count = len(self.removals)

            for visitor in Rules.VisitorProvider.prefix_visitors:
                self.accept(visitor)
                if self.process_is_stopped:
                    return None
                if len(self.removals) > removal_count:
                    break
        return None

    def remove_suffixes(self):
        """
        Accept suffix_visitors rules.
        """
        self.accept_visitors(Rules.VisitorProvider.suffix_visitors)

    def accept_visitors(self, visitors):
        """
        Accept visitors rules.

        Immediately stop stemming process if current_word processed by a visitor
        is in dictionary.
        """
        for visitor in visitors:
            self.accept(visitor)
            if self.process_is_stopped:
                return None
        return None

    def accept(self, visitor):
        """
        Accept visitor rule.

        Stop stemming process if current_word processed by visitor is in
        dictionary.
        """
        visitor(self)
        if self.current_word in self.dictionary:
            self.stop_process()

    def is_suffix_removal(self, removal):
        """
        Check whether the removed part is a suffix.
        """
        return removal.affixType == 'DS' \
                or removal.affixType == 'PP' \
                or removal.affixType == 'P'
