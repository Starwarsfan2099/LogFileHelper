import LogFileHelper

fileName = "error_log.txt"

logfile = LogFileHelper.ParseLogFile(fileName)

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
