
###
""" 
This script fetches data from https://data.police.uk
For this coursework, Cambridgeshire will be the local area considered
"""
###


urls = ['https://data.police.uk/data/archive/2019-01.zip',
        'https://data.police.uk/data/archive/2019-02.zip',
        'https://data.police.uk/data/archive/2019-03.zip',
        'https://data.police.uk/data/archive/2019-04.zip',
        'https://data.police.uk/data/archive/2019-05.zip',
        'https://data.police.uk/data/archive/2019-06.zip',
        'https://data.police.uk/data/archive/2019-07.zip',
        'https://data.police.uk/data/archive/2019-08.zip',
        'https://data.police.uk/data/archive/2019-09.zip',
        'https://data.police.uk/data/archive/2019-10.zip',
        'https://data.police.uk/data/archive/2019-11.zip',
        'https://data.police.uk/data/archive/2019-12.zip',
        'https://data.police.uk/data/archive/2020-01.zip',
        'https://data.police.uk/data/archive/2020-02.zip',
        'https://data.police.uk/data/archive/2020-03.zip',
        'https://data.police.uk/data/archive/2020-04.zip',
        'https://data.police.uk/data/archive/2020-05.zip',
        'https://data.police.uk/data/archive/2020-06.zip',
        'https://data.police.uk/data/archive/2020-07.zip',
        'https://data.police.uk/data/archive/2020-08.zip',
        'https://data.police.uk/data/archive/2020-09.zip',
        'https://data.police.uk/data/archive/2020-10.zip',
        'https://data.police.uk/data/archive/2020-11.zip',
        'https://data.police.uk/data/archive/2020-12.zip']

files = ['2019-01/2019-01-cambridgeshire-outcomes.csv',
         '2019-02/2019-02-cambridgeshire-outcomes.csv',
         '2019-03/2019-03-cambridgeshire-outcomes.csv',
         '2019-04/2019-04-cambridgeshire-outcomes.csv',
         '2019-05/2019-05-cambridgeshire-outcomes.csv',
         '2019-06/2019-06-cambridgeshire-outcomes.csv',
         '2019-07/2019-07-cambridgeshire-outcomes.csv',
         '2019-08/2019-08-cambridgeshire-outcomes.csv',
         '2019-09/2019-09-cambridgeshire-outcomes.csv',
         '2019-10/2019-10-cambridgeshire-outcomes.csv',
         '2019-11/2019-11-cambridgeshire-outcomes.csv',
         '2019-12/2019-12-cambridgeshire-outcomes.csv',
         '2020-01/2020-01-cambridgeshire-outcomes.csv',
         '2020-02/2020-02-cambridgeshire-outcomes.csv',
         '2020-03/2020-03-cambridgeshire-outcomes.csv',
         '2020-04/2020-04-cambridgeshire-outcomes.csv',
         '2020-05/2020-05-cambridgeshire-outcomes.csv',
         '2020-06/2020-06-cambridgeshire-outcomes.csv',
         '2020-07/2020-07-cambridgeshire-outcomes.csv',
         '2020-08/2020-08-cambridgeshire-outcomes.csv',
         '2020-09/2020-09-cambridgeshire-outcomes.csv',
         '2020-10/2020-10-cambridgeshire-outcomes.csv',
         '2020-11/2020-11-cambridgeshire-outcomes.csv',
         '2020-12/2020-12-cambridgeshire-outcomes.csv']

from remotezip import RemoteZip

for f, b, in zip(urls, files):
    with RemoteZip(f) as zip:
        zip.extract(b)