import csv
from db import Database

db = Database('DataAnd.db')

tab = db.get_table('history')
print(tab[0])

with open('test' + '.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(tab[1])
    for row in tab[0]:
        writer.writerow(row)