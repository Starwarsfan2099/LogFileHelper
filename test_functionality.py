# Created by AJ Clark on 10/22/2019

import LogFileHelper

fileName = "test_log.txt"
verbose = True

logfile = LogFileHelper.ParseLogFile(fileName, verbose=verbose)

assert logfile.lineCount == 10

assert logfile.countOccurrencesByLine("the") == 5

assert logfile.countOccurrences("the") == 7

assert logfile.addByColumn(4) == 4988

assert logfile.getColumnUniqueValuesSorted(4, largestFirst=True)[0] == 4798

assert logfile.getColumnUniqueValuesSorted(4)[0] == 0

assert logfile.getColumnUniqueValuesSorted(4) == [0, 1, 4, 5, 8, 12, 34, 59, 67, 4798]

assert logfile.addByColumnWithString(4, "the") == 4936

assert logfile.addByColumnWithUniqueColumn(4, 0, largestFirst=True)['the'] == 4924



print "Success"
