# nordea-ynab-converter-dk
Convert Nordea Bank transactions files into into YNAB-ready files.
Made for the Danish version of Nordea's website.

### Usage example:
Open the terminal and run
```sh
$ py ynab-converter.py -s nordea.csv 
```
### Options:

```sh
py ynab-converter.py [-h] -s SOURCE [-d DESTINATION]
```

### How to export CSV file from Nordea
Export your bank transactions using Nordea Home banking
![Imgur](https://i.imgur.com/aLoTe8w.png)

Save file (ex: nordea.csv)

### How to import transactions to YNAB
Convert the CSV file from Nordea to a YNAB file using nordea-ynab-converter-dk.
To import the file from YNAB, click on the desired account > Import 


![Imgur](https://i.imgur.com/9JsYIye.png)


Select Import file

![Imgur](https://i.imgur.com/UNDtXde.png)

And point to the generated YNAB file.
### Requirements
 Python v3.0+
