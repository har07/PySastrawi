from Sastrawi.stemming.rules import PrecedenceAdjustmentSpecification as PAS

class Context(object):
    """Stemming Context using Nazief and Adriani, CS, ECS, Improved ECS"""

    def __init__(self, original_word, dictionary, visitor_provider):

        self.process_is_stopped = False
        self.original_word = original_word
        self.current_word = original_word
        self.result = ''
        self.dictionary = dictionary
        self.removals = []

        self.visitors = visitor_provider.visitors
        self.suffix_visitors = visitor_provider.suffix_visitors
        self.prefix_visitors = visitor_provider.prefix_visitors

        self.execute()

    def stopProcess(self):
        self.process_is_stopped = True

    def add_removal(self, removal):
        self.removals.append(removal)

    def execute(self):
        """Execute stemming process; the result can be retrieved with result"""

        # step 1 - 5
        self.start_stemming_process()

        # step 6
        if self.current_word in self.dictionary:
            self.result = self.current_word
        else:
            self.result = self.original_word

    def start_stemming_process(self):

        # step 1
        if self.current_word in self.dictionary:
            return

        self.accept_visitors(self.visitors)
        if self.process_is_stopped:
            return

        # Confix Stripping
        # Try to remove prefix before suffix if the specification is met
        if PAS().is_satisfied_by(self.original_word):
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

        # ECS loop pengembalian akhiran
        self.restore_prefix()

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
        for try_ in range(3):
            self.accept_prefix_visitors()
            if self.process_is_stopped:
                return

    def accept_prefix_visitors(self):
        removal_count = len(self.removals)
        for visitor in self.prefix_visitors:
            self.accept(visitor)
            if self.process_is_stopped or len(self.removals) > removal_count:
                return

    def remove_suffixes(self):
        self.accept_visitors(self.suffix_visitors)

    def accept_visitors(self, visitors):
        for visitor in visitors:
            self.accept(visitor)
            if self.process_is_stopped:
                return

    def accept(self, visitor):
        visitor.visit(self)
        if self.current_word in self.dictionary:
            self.stopProcess()


    def is_suffix_removal(self, removal):
        """Check wether the removed part is a suffix"""
        return removal.affixType == 'DS' \
               or removal.affixType == 'PP' \
               or removal.affixType == 'P'

    def restore_prefix(self):
        """Restore prefix to proceed with ECS loop pengembalian akhiran"""

        if self.removals:
            # return the word before precoding (the subject of first prefix removal)
            self.current_word = self.removals[0].subject

        for removal in self.removals:
            if removal.affixType == 'DP':
                self.removals.remove(removal)
