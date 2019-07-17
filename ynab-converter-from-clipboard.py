import argparse
import re
from datetime import datetime 

__author__ = 'Daniel Torres'

def get_cli_args():
    parser = argparse.ArgumentParser( description='Parse Nordea Bank transactions files into into YNAB-ready files. Designed and tested for the Danish version of Nordea\'s website.')
    parser.add_argument('-s', '--source', type=str, help='Source filename (the CSV file exported using Nordea Web Banking)', required=True)
    parser.add_argument('-d', '--destination', type=str, help='Destination filename', default='ynab.csv')
    args = parser.parse_args()
    return args.source, args.destination

def main():
    source, destination = get_cli_args()
    regex = re.compile("(\d\d-\d\d-\d\d\d\d)\s*(.*).(\d\d-\d\d-\d\d\d\d).\s(-?\d*,\d{2})\skr\.\s*(-?\d+.?\d+,\d{2})\skr.")
    
    data = []
    with open(source) as file:
        for line in file:
            collumn = regex.search(line)
            data.append([collumn[1].strftime("%d/%m/%Y"),collumn[2],collumn[2],collumn[4]])

    with open(destination, 'w+') as outputFile:
        outputFile.write('Date;Payee;Memo;Inflow\n')
        for row in data:			
            outputFile.write(';'.join(row) + '\n')

    print('YNAB file written to \'' + destination + '\'')

if __name__=="__main__":
   main()