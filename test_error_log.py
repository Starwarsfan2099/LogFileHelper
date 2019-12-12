import LogFileHelper

fileName = "error_log.txt"
verbose = False

logfile = LogFileHelper.ParseLogFile(fileName, verbose=verbose)

# Question 1
errors = logfile.countOccurrencesByLine("File does not exist")
print "1: %s \'File does not exist\' errors." % errors
assert errors == 65119

# Question 2
count = len(logfile.getColumnUniqueValues(7))
print "2: Unique IP addresses: %s" % count
assert count == 8121

# Question 3
ip = logfile.getColumnUniqueValuesCounted(5, "[error]", 7)
mostErrors = logfile.getLargestItemInDictionary(ip).strip("]")
print "3: IP with most errors: %s" % mostErrors
assert mostErrors == "88.80.10.1"

# Question 4
stuff = logfile.getColumnUniqueValuesByColumn(7, -1)
mostUniqueFiles = logfile.getMostItemsForKeyInDictionary(stuff).strip("]")
print "4: IP with most unique requested files: %s" % mostUniqueFiles
assert mostUniqueFiles == "176.53.21.162"

# Question 5
count = logfile.countUniqueOccurrencesByLineIfColumn("File does not exist", 7, mostUniqueFiles, 12)
print "5: Unique file/directory requests from %s that yielded a \'Does not exists\' error: %s" % (mostUniqueFiles, count)
assert count == 1559
