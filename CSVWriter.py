import csv

class CSVWriter():

    def writeToCSV(self, fileName, csvRow):
        with open(fileName, 'a') as outputFile:
            w = csv.writer(outputFile)
            w.writerow(csvRow)
            # w.write('\n')