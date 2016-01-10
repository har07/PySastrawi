import re

class PrecedenceAdjustmentSpecification(object):
    """Confix Stripping Rule Precedence Adjustment Specification.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval" page 78-79.

    @link   http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def isSatisfiedBy(self, value):
        regexRules = [
            r'^be(.*)lah$',
            r'^be(.*)an$',
            r'^me(.*)i$',
            r'^di(.*)i$',
            r'^pe(.*)i$',
            r'^ter(.*)i$',
        ]

        for rule in regexRules:
            if re.match(rule, value):
                return True

        return False



