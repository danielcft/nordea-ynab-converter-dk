import csv
import argparse
  
__author__ = 'Daniel Torres'

def get_cli_args():
    parser = argparse.ArgumentParser( description='Parse Nordea Bank transactions files into into YNAB-ready files. Designed and tested for the Danish version of Nordea\'s website.')
    parser.add_argument('-s', '--source', type=str, help='Source filename (the CSV file exported using Nordea Web Banking)', required=True)
    parser.add_argument('-d', '--destination', type=str, help='Destination filename', default='ynab.csv')
    args = parser.parse_args()
    return args.source, args.destination

def main():
    source, destination = get_cli_args()
    with open(source) as csvDataFile:
        csvDataFile.seek(1); # remove first line
        csvReader =  csv.reader(csvDataFile,delimiter=';')
        with open(destination, 'w+') as outputFile:
            rowCount = 0;
            for row in csvReader:
                if(rowCount==1):
                    outputFile.write('Date;Payee;Rente;Outflow\n')
                if(rowCount!=1 and rowCount!=0):
                    outputFile.write(';'.join(row) + '\n')
                rowCount=rowCount+1
    print('YNAB file written to \'' + destination + '\'')

if __name__=="__main__":
   main() 
