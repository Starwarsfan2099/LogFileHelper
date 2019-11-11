import LogFileHelper

fileName = "error_log.txt"
verbose = False

logfile = LogFileHelper.ParseLogFile(fileName, verbose=verbose)

# Question 1
errors = logfile.countOccurrencesByLine("File does not exist")
print "%s \'File does not exist\' errors." % errors

# Question 2
count = len(logfile.getColumnUniqueValuesSorted(7))
print "Unique IP addresses: %s" % count

# Question 3
ip = logfile.getColumnUniqueValuesCounted(5, "[error]", 7, largestFirst=True)
mostErrors = logfile.getLargestItemInDictionary(ip)
print "IP with most errors: %s" % mostErrors.strip("]")

# Question 4
stuff = logfile.getColumnUniqueValuesByColumn(7, -1)
mostUniqueFiles = logfile.getMostItemsForKeyInDictionary(stuff).strip("]")
print "IP with most unique requested files: %s" % mostUniqueFiles

# Question 5
count = logfile.countUniqueOccurrencesByLineIfColumn("File does not exist", 7, mostUniqueFiles, 12)
print "Unique file/directory requests from %s that yielded a \'Does not exists\': %s" % (mostUniqueFiles, count)
