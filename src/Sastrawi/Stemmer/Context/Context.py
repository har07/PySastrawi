from Sastrawi.Stemmer.ConfixStripping.PrecedenceAdjustmentSpecification \
   import PrecedenceAdjustmentSpecification

class Context(object):
    """Stemming Context using Nazief and Adriani, CS, ECS, Improved ECS"""

    def __init__(self, originalWord, dictionary, visitorProvider):
        self.originalWord = originalWord
        self.currentWord = originalWord
        self.dictionary = dictionary
        self.visitorProvider = visitorProvider

        self.processIsStopped = False
        self.removals = []
        self.visitors = []
        self.suffixVisitors = []
        self.prefixVisitors = []
        self.result = ''

        self.initVisitors()

    def initVisitors(self):
        self.visitors = self.visitorProvider.getVisitors()
        self.suffixVisitors = self.visitorProvider.getSuffixVisitors()
        self.prefixVisitors = self.visitorProvider.getPrefixVisitors()

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getDictionary(self):
        return self.dictionary

    def getOriginalWord(self):
        return self.originalWord

    def setCurrentWord(self, word):
        self.currentWord = word

    def getCurrentWord(self):
        return self.currentWord

    def stopProcess(self):
        self.processIsStopped = True

    #def processIsStopped(self):
    #    return self.processIsStopped

    def addRemovals(self, removal):
        self.removals.append(removal)

    def getRemovals(self):
        return self.removals

    def getResult(self):
        return self.result

    def execute(self):
        """Execute stemming process; the result can be retrieved with getResult()"""

        #step 1 - 5
        self.startStemmingProcess()

        #step 6
        if self.getCurrentWord() in self.dictionary:
            self.result = self.getCurrentWord()
        else:
            self.result = self.originalWord

    def startStemmingProcess(self):

        #step 1
        if self.currentWord in self.dictionary:
            return
        self.acceptVisitors(self.visitors)
        if self.currentWord in self.dictionary:
            return

        csPrecedenceAdjustmentSpecification = PrecedenceAdjustmentSpecification()

        #Confix Stripping
        #Try to remove prefix before suffix if the specification is met
        if csPrecedenceAdjustmentSpecification.isSatisfiedBy(self.getOriginalWord()):
            #step 4, 5
            self.removePrefixes()
            if self.getCurrentWord() in self.dictionary:
                return

            #step 2, 3
            self.removeSuffixes()
            if self.getCurrentWord() in self.dictionary:
                return
            else:
                #if the trial is failed, restore the original word
                #and continue to normal rule precedence (suffix first, prefix afterwards)
                self.setCurrentWord(self.originalWord)
                self.removals = []

        #step 2, 3
        self.removeSuffixes()
        if self.getCurrentWord() in self.dictionary:
            return

        #step 4, 5
        self.removePrefixes()
        if self.getCurrentWord() in self.dictionary:
            return

        #ECS loop pengembalian akhiran
        self.loopPengembalianAkhiran()

    def removePrefixes(self):
        for i in range(3):
            self.acceptPrefixVisitors(self.prefixVisitors)
            if self.getCurrentWord() in self.dictionary:
                return

    def removeSuffixes(self):
        self.acceptVisitors(self.suffixVisitors)

    def accept(self, visitor):
        visitor.visit(self)

    def acceptVisitors(self, visitors):
        for visitor in visitors:
            self.accept(visitor)
            if self.getCurrentWord() in self.dictionary:
                return self.getCurrentWord()
            if self.processIsStopped:
                return self.getCurrentWord()

    def acceptPrefixVisitors(self, visitors):
        removalCount = len(self.removals)
        for visitor in visitors:
            self.accept(visitor)
            if self.getCurrentWord() in self.dictionary:
                return self.getCurrentWord()
            if self.processIsStopped:
                return self.getCurrentWord()
            if len(self.removals) > removalCount:
                return

    def loopPengembalianAkhiran(self):
        """ECS Loop Pengembalian Akhiran"""
        self.restorePrefix()

        removals = self.removals
        reversedRemovals = reversed(removals)
        currentWord = self.getCurrentWord()

        for removal in reversedRemovals:
            if not self.isSuffixRemoval(removal):
                continue
            if removal.getRemovedPart() == 'kan':
                self.setCurrentWord(removal.getResult() + 'k')

                #step 4,5
                self.removePrefixes()
                if self.getCurrentWord() in self.dictionary:
                    return
                self.setCurrentWord(removal.getResult() + 'kan')
            else:
                self.setCurrentWord(removal.getSubject())

            #step 4,5
            self.removePrefixes()
            if self.getCurrentWord() in self.dictionary:
                return

            self.removals = removals
            self.setCurrentWord(currentWord)

    def isSuffixRemoval(self, removal):
        """Check wether the removed part is a suffix"""
        return removal.getAffixType() == 'DS' \
               or removal.getAffixType() == 'PP' \
               or removal.getAffixType() == 'P'

    def restorePrefix(self):
        """Restore prefix to proceed with ECS loop pengembalian akhiran"""
        for removal in self.removals:
            #return the word before precoding (the subject of first prefix removal)
            self.setCurrentWord(removal.getSubject())
            break

        for removal in self.removals:
            if removal.getAffixType() == 'DP':
                self.removals.remove(removal)

