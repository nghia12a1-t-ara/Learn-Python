
import csv, os
from datetime import datetime

os.chdir("D:\Python\CSV\Exercise1")

''' Open and Read each row of csv file '''
''' And save each row to an element of a list 'title_row' '''
title_row = []  # Read the input csv file

with open('input.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile, delimiter=',')
    for row in csv_reader:
        title_row.append(row)

''' Get current time '''
now = datetime.now()
datetime_str = now.strftime("%d/%m/%y %H:%M:%S")

''' Calculate Seniority '''
seni_str = []   # Save the seniority of employees
now_year = now.strftime("%y")
now_month = now.strftime("%m")

''' Calculate the several time from Jan_20 to now '''
seni_20 = str(int(now_year) - 20)
seni_Jan = str(int(now_month) - 1)
seni_Jan_20 = float(seni_20) + (float(seni_Jan) / 10)


for col in range(len(title_row[0])):
    if title_row[0][col] == 'Jan-20':
        for row in range(1, len(title_row)):
            last_seni = title_row[row][col]
            now_seni = str(float(last_seni) + seni_Jan_20)
            seni_str.append(now_seni)
            

''' Open and Write to output csv file '''
with open('output.csv', 'w') as outfile:
    writer = csv.writer(outfile, delimiter=',',\
    quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(len(title_row)):
        if i == 0:
            writer.writerow(['Account', 'Date', 'Seniority'])
        else:
            for col in range(len(title_row[0])):
                if (title_row[0][col] == 'Account'):
                    writer.writerow([title_row[i][col], datetime_str, seni_str[i - 1]])
