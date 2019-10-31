# Created by AJ CLark on 10/21/2019
# test

import re
import operator
import collections


class ParseLogFile:

    def __init__(self, fileName, verbose=False):
        # Arguments:
        #   fileName:       STRING      Name of file to open.
        #   verbose:        BOOL        Enables verbose information to be printed throughout the module.
        # Objects:
        #   self.verbose    BOOL        Stores verbose value.
        #   self.logfile    FILE        Opens a file object using fileName.
        #   self.lineCount  INT         Stores the total number of lines in a file.
        self.verbose = verbose
        self.logfile = open(fileName, "r")
        self.lineCount = sum(1 for line in self.logfile)

    def printDictionary(self, dictionary):
        # This method simply prints a dictionary.
        # Arguments:
        #   dictionary      DICTIONARY  A dictionary to print.
        for key in dictionary:
            print str(key) + " : " + str(dictionary[key])

    def countOccurrencesByLine(self, string):
        # This method counts the number of lines in which a string occurs at least once.
        # Arguments:
        #   string:         STRING      String to count occurrences of.
        # Returns:
        #   counter         INT         The total number of lines where the string was found.
        self.logfile.seek(0)
        counter = 0
        for line in self.logfile:
            if string in line:
                counter += 1
        if self.verbose is True: print "Number of lines with \'%s\': %d" % (string, counter)
        return counter

    def countOccurrences(self, string):
        # This method counts the total number of occurrences of a string in the whole file.
        # Arguments:
        #   string:         STRING      String to count occurrences of.
        # Returns:
        #   counter         INT         The total number of occurrences of the string.
        self.logfile.seek(0)
        counter = 0
        for line in self.logfile:
            count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(string), line))
            counter += count
        if self.verbose is True: print "Number of occurrences of \'%s\': %d" % (string, counter)
        return counter

    def addByColumn(self, column):
        # This method adds all of the total values in a certain column of a file throughout the file.
        # Arguments:
        #   column          INT         Column number in the line.
        # Returns:
        #   adder           INT         The total of that certain column through the file.
        self.logfile.seek(0)
        adder = 0
        counter = 0
        s = ""
        for line in self.logfile:
            line = line.split()
            try:
                adder += int(line[column])
                counter += 1
            except IndexError as e:
                print "Error, tried to read from column %s on line \'%s\'(line %d)." % (column, s.join(line), counter)
                exit()
        if self.verbose is True: print "Column %d added is: %d (%d occurrences added)" % (column, adder, counter)
        return adder

    def addByColumnWithString(self, column, string):
        # This method adds all of the total values in a certain column of a line that includes the string.
        # Arguments:
        #   column          INT         Column number in the line.
        #   string          STRING      String to match.
        # Returns:
        #   adder           INT         The total of that certain column through the file.
        self.logfile.seek(0)
        adder = 0
        counter = 0
        occurrences = 0
        s = ""
        for line in self.logfile:
            counter += 1
            if string in line:
                line = line.split()
                try:
                    adder += int(line[column])
                    occurrences += 1
                except IndexError as e:
                    print "Error, tried to read from column %s on line \'%s\'(line %d)." % (column, s.join(line), counter)
                    exit()
        if self.verbose is True: print "Column %d added for lines with \'%s\': %d (%d occurrences added)" % (column, string, adder, occurrences)
        return adder

    def addByColumnWithUniqueColumn(self, column, uniqueColumn, largestFirst=False):
        # This method adds all of the total values in a certain column of a line for each unique occurrence of a column item.
        # Arguments:
        #   column          INT         Column number in the line.
        #   uniqueColumn    INT         Unique column to count from column of.
        #   largestFirst    BOOL        Returns values sorted from greatest to smallest if True.
        # Returns:
        #   sortedValue     DICTIONARY  The sorted dictionary of values.
        self.logfile.seek(0)
        values = {}
        counter = 0
        s = ""
        for line in self.logfile:
            line = line.split()
            counter += 1
            try:
                if line[uniqueColumn] in values:
                    values[line[uniqueColumn]] += int(line[column])
                else:
                    values[line[uniqueColumn]] = int(line[column])
            except IndexError as e:
                print "Error, tried to read from column %s on line \'%s\'(line %d)." % (column, s.join(line), counter)
                exit()
        if largestFirst is True:
            sortedList = sorted(values.items(), key=operator.itemgetter(1), reverse=largestFirst)
        else:
            sortedList = sorted(values.items(), key=operator.itemgetter(1))
        sortedValues = collections.OrderedDict(sortedList)
        if self.verbose is True: print "Column %d added for lines with unique column %d value: " % (column, uniqueColumn) + str(sortedValues)
        return sortedValues

    def getColumnUniqueValuesSorted(self, column, largestFirst=False):
        # This method gets all of the unique values in a column and sorts them. Default sorts from smallest to largest.
        # Arguments:
        #   column          INT         Column number in the line.
        #   largestFirst    BOOL        Sort by the largest number first.
        # Returns:
        #   values          LIST        List containing all unique column values sorted.
        self.logfile.seek(0)
        values = []
        counter = 0
        s = ""
        nextValue = 0
        for line in self.logfile:
            line = line.split()
            try:
                nextValue = int(line[column])
                counter += 1
            except IndexError as e:
                print "Error, tried to read from column %s on line \'%s\'(line %d)." % (column, s.join(line), counter)
                exit()
            if nextValue not in values:
                values.append(nextValue)
        if largestFirst is True:
            values.sort(reverse=True)
        else:
            values.sort()
        if self.verbose is True: print "Column %d values sorted: " % column + str(values)
        return values

    def getColumnUniqueValuesAmountAdded(self, column, largestFirst=False):
        # This method adds all of the total values in a certain column of a line for each unique occurrence of a column item.
        # Arguments:
        #   column          INT         Column number in the line.
        #   uniqueColumn    INT         Unique column to count from column of.
        #   largestFirst    BOOL        Returns values sorted from greatest to smallest if True.
        # Returns:
        #   sortedValue     DICTIONARY  The sorted dictionary of values.
        self.logfile.seek(0)
        values = {}
        counter = 0
        adder = 0
        s = ""
        for line in self.logfile:
            line = line.split()
            counter += 1
            try:
                if line[column] in values:
                    values[line[column]] += 1
                else:
                    values[line[column]] = 1
            except IndexError as e:
                print "Error, tried to read from column %s on line \'%s\'(line %d)." % (column, s.join(line), counter)
                exit()
        if largestFirst is True:
            sortedList = sorted(values.items(), key=operator.itemgetter(1), reverse=largestFirst)
        else:
            sortedList = sorted(values.items(), key=operator.itemgetter(1))
        sortedValues = collections.OrderedDict(sortedList)
        if self.verbose is True: print "Column %d added for lines with unique column %d value: " % (column, column) + str(sortedValues)
        return sortedValues

    def getColumnUniqueValuesCounted(self, column, string, uniqueColumn, largestFirst=False):
        # This method gets the amount for each unique item ina column line by another column line.
        # Arguments:
        #   column          INT         Column number in the line to look for string.
        #   string          STRING      String to match for in the column.
        #   uniqueColumn    INT         Unique column to get occurrences of.
        #   largestFirst    BOOL        Returns values sorted from greatest to smallest if True.
        # Returns:
        #   sortedValue     DICTIONARY  The sorted dictionary of values.
        self.logfile.seek(0)
        values = {}
        counter = 0
        s = ""
        for line in self.logfile:
            line = line.split()
            counter += 1
            try:
                if string in line[column]:
                    if line[uniqueColumn] in values:
                        values[line[uniqueColumn]] += 1
                    else:
                        values[line[uniqueColumn]] = 1
            except IndexError as e:
                print "Error, tried to read from column %s on line \'%s\'(line %d)." % (column, s.join(line), counter)
                exit()
        if largestFirst is True:
            sortedList = sorted(values.items(), key=operator.itemgetter(1), reverse=largestFirst)
        else:
            sortedList = sorted(values.items(), key=operator.itemgetter(1))
        sortedValues = collections.OrderedDict(sortedList)
        if self.verbose is True: print "In lines with \'%s\' in column %d, unique values in column %d were: " % (string, column, uniqueColumn) + str(sortedValues)
        return sortedValues
