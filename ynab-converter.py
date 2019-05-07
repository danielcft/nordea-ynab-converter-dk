import csv
import argparse
from datetime import datetime 

__author__ = 'Daniel Torres'

def get_cli_args():
    parser = argparse.ArgumentParser( description='Parse Nordea Bank transactions files into into YNAB-ready files. Designed and tested for the Danish version of Nordea\'s website.')
    parser.add_argument('-s', '--source', type=str, help='Source filename (the CSV file exported using Nordea Web Banking)', required=True)
    parser.add_argument('-d', '--destination', type=str, help='Destination filename', default='ynab.csv')
    args = parser.parse_args()
    return args.source, args.destination
	
def convertToValidDate(row):
    newRow = []
    for cell in row:
        try: 
            parsed = datetime.strptime(cell,"%d-%m-%Y")
            newRow.append(parsed.strftime("%d/%m/%Y"))
        except:
            newRow.append(cell)
    return newRow

def main():
    source, destination = get_cli_args()
	# The .csv file from Nordea uses some sort of encoding other than unicode
    with open(source,encoding='ansi') as csvDataFile:
        # remove first lines
        csvDataFile.readline();

        csvObj =  csv.reader(csvDataFile,delimiter=';')
		# the destination file will be encoded using unicode
        with open(destination, 'w+', encoding='utf-8') as outputFile:
            outputFile.write('Date;Payee;Memo;Inflow\n')
            for row in csvObj:
                del(row[2]) # Delete duplicate date
                del(row[3]) # Delete balance
                row.insert(2,row[1]) # Backup payee information to 'Memo'
                row=convertToValidDate(row)
                outputFile.write(';'.join(row) + '\n')
    print('YNAB file written to \'' + destination + '\'')

if __name__=="__main__":
   main() 
