from Sastrawi.Stemmer.ConfixStripping.PrecedenceAdjustmentSpecification \
   import PrecedenceAdjustmentSpecification

class Context(object):
    """Stemming Context using Nazief and Adriani, CS, ECS, Improved ECS"""

    def __init__(self, original_word, dictionary, visitor_provider):
        self.original_word = original_word
        self.current_word = original_word
        self.dictionary = dictionary
        self.visitor_provider = visitor_provider

        self.process_is_stopped = False
        self.removals = []
        self.visitors = []
        self.suffix_visitors = []
        self.prefix_pisitors = []
        self.result = ''

        self.init_visitors()

    def init_visitors(self):
        self.visitors = self.visitor_provider.get_visitors()
        self.suffix_visitors = self.visitor_provider.get_suffix_visitors()
        self.prefix_pisitors = self.visitor_provider.get_prefix_visitors()

    def stopProcess(self):
        self.process_is_stopped = True

    def add_removal(self, removal):
        self.removals.append(removal)

    def execute(self):
        """Execute stemming process; the result can be retrieved with result"""

        #step 1 - 5
        self.start_stemming_process()

        #step 6
        if self.dictionary.contains(self.current_word):
            self.result = self.current_word
        else:
            self.result = self.original_word

    def start_stemming_process(self):

        #step 1
        if self.dictionary.contains(self.current_word):
            return
        self.accept_visitors(self.visitors)
        if self.dictionary.contains(self.current_word):
            return

        csPrecedenceAdjustmentSpecification = PrecedenceAdjustmentSpecification()

        #Confix Stripping
        #Try to remove prefix before suffix if the specification is met
        if csPrecedenceAdjustmentSpecification.is_satisfied_by(self.original_word):
            #step 4, 5
            self.remove_prefixes()
            if self.dictionary.contains(self.current_word):
                return

            #step 2, 3
            self.remove_suffixes()
            if self.dictionary.contains(self.current_word):
                return
            else:
                #if the trial is failed, restore the original word
                #and continue to normal rule precedence (suffix first, prefix afterwards)
                self.current_word = self.original_word
                self.removals = []

        #step 2, 3
        self.remove_suffixes()
        if self.dictionary.contains(self.current_word):
            return

        #step 4, 5
        self.remove_prefixes()
        if self.dictionary.contains(self.current_word):
            return

        #ECS loop pengembalian akhiran
        self.loop_pengembalian_akhiran()

    def remove_prefixes(self):
        for i in range(3):
            self.accept_prefix_visitors(self.prefix_pisitors)
            if self.dictionary.contains(self.current_word):
                return

    def remove_suffixes(self):
        self.accept_visitors(self.suffix_visitors)

    def accept(self, visitor):
        visitor.visit(self)

    def accept_visitors(self, visitors):
        for visitor in visitors:
            self.accept(visitor)
            if self.dictionary.contains(self.current_word):
                return self.current_word
            if self.process_is_stopped:
                return self.current_word

    def accept_prefix_visitors(self, visitors):
        removalCount = len(self.removals)
        for visitor in visitors:
            self.accept(visitor)
            if self.dictionary.contains(self.current_word):
                return self.current_word
            if self.process_is_stopped:
                return self.current_word
            if len(self.removals) > removalCount:
                return

    def loop_pengembalian_akhiran(self):
        """ECS Loop Pengembalian Akhiran"""
        self.restore_prefix()

        removals = self.removals
        reversed_removals = reversed(removals)
        current_word = self.current_word

        for removal in reversed_removals:
            if not self.is_suffix_removal(removal):
                continue
            if removal.get_removed_part() == 'kan':
                self.current_word = removal.result + 'k'

                #step 4,5
                self.remove_prefixes()
                if self.dictionary.contains(self.current_word):
                    return
                self.current_word = removal.result + 'kan'
            else:
                self.current_word = removal.get_subject()

            #step 4,5
            self.remove_prefixes()
            if self.dictionary.contains(self.current_word):
                return

            self.removals = removals
            self.current_word = current_word

    def is_suffix_removal(self, removal):
        """Check wether the removed part is a suffix"""
        return removal.get_affix_type() == 'DS' \
               or removal.get_affix_type() == 'PP' \
               or removal.get_affix_type() == 'P'

    def restore_prefix(self):
        """Restore prefix to proceed with ECS loop pengembalian akhiran"""
        for removal in self.removals:
            #return the word before precoding (the subject of first prefix removal)
            self.current_word = removal.get_subject()
            break

        for removal in self.removals:
            if removal.get_affix_type() == 'DP':
                self.removals.remove(removal)

