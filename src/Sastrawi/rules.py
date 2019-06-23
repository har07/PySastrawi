"""
This module contains all stemming rules.
"""

import re
import Sastrawi.rules_disambiguate as dsm
from collections import namedtuple

Removal = namedtuple('Removal', 'subject result removedPart affixType')

def isPAS(word):
    """
    Check if Precedence Adjustment Specification is satisfied by word.

    Confix Stripping Rule Precedence Adjustment Specification.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval" page 78-79.
    @link   http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
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

class VisitorProvider():
    """
    description of class.
    """

    def __init__(self):
        self.visitors = [DontStemShortWord()]

        # {lah|kah|tah|pun}, {ku|mu|nya}, {i|kan|an}
        self.suffix_visitors = [RemoveInflectionalParticle(),
                                RemoveInflectionalPossessivePronoun(),
                                RemoveDerivationalSuffix()]

        # {di|ke|se}
        self.prefix_visitors = [RemovePlainPrefix()]

        # Add all rules in rules_disambiguator to prefix_visitors
        for num in range(1, 43):
            # group rule(s) by its number
            rules = [getattr(dsm, rule) for rule in dir(dsm)
                     if str(num).zfill(2) in rule]

            self.prefix_visitors.append(PrefixDisambiguator(rules))


class DontStemShortWord():
    """
    Stop stemming process if word length is less than 4.
    """

    def visit(self, context):
        if len(context.current_word) <= 3:
            context.stop_process()

class RemoveInflectionalParticle():
    """
    Remove Inflectional particle.

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 60
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        """
        Remove inflectional particle : lah|kah|tah|pun
        """

        result = re.sub(r'-*(lah|kah|tah|pun)$', '', context.current_word, 1)
        if result != context.current_word:
            removed_part = re.sub(result, '', context.current_word, 1)
            removal = Removal(context.current_word, result, removed_part, 'P')

            context.add_removal(removal)
            context.current_word = result

class RemoveInflectionalPossessivePronoun():
    """
    Remove Inflectional Possessive Pronoun.

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 60
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        """
        Remove inflectional possessive pronoun : ku|mu|nya|-ku|-mu|-nya
        """

        result = re.sub(r'-*(ku|mu|nya)$', '', context.current_word, 1)
        if result != context.current_word:
            removed_part = re.sub(result, '', context.current_word, 1)
            removal = Removal(context.current_word, result, removed_part, 'PP')

            context.add_removal(removal)
            context.current_word = result

class RemoveDerivationalSuffix():
    """
    Remove Derivational Suffix.

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 61
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        """
        Remove derivational suffix.
        Original rule : i|kan|an
        Added the adopted foreign suffix rule : is|isme|isasi
        Added the adopted suffix rule : wan|wati
        """

        # wan -beri -beriman
        result = re.sub(r'(wan|wati)$', '', context.current_word, 1)

        if result in context.dictionary:
            removed_part = re.sub(result, '', context.current_word, 1)
            removal = Removal(context.current_word, result, removed_part, 'DS')

            context.add_removal(removal)
            context.current_word = result
            return

        result = re.sub(r'(is|isme|isasi|i|kan|an)$', '', context.current_word, 1)
        if result != context.current_word:
            removed_part = re.sub(result, '', context.current_word, 1)
            removal = Removal(context.current_word, result, removed_part, 'DS')

            context.add_removal(removal)
            context.current_word = result

class RemovePlainPrefix():
    """
    Remove Plain Prefix.

    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 61
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        """Remove plain prefix : di|ke|se"""

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
        result = None

        for rule in self.rules:
            result = rule(context.current_word)
            if result in context.dictionary:
                break

        if result is None:
            return None

        removed_part = re.sub(result, '', context.current_word, 1)
        removal = Removal(context.current_word, result, removed_part, 'DP')

        context.add_removal(removal)
        context.current_word = result
