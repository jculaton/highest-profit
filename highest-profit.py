# highest-profit.py
# April 9, 2021
# (c) Joseph Culaton

#import statements
import csv
import json

#output variables
totalRowCount=0
validProfit=0
top20=0
temp =[] #empty list for output file

with open('data.csv','r') as data: #opening input file
	with open('data2.json', 'w') as data2: #creating output file

		output = csv.DictReader(data)

		for row in output:
			profit = row['Profit (in millions)'] #HashKey
			a = profit.replace('.','') #removing . and - from data in profit column
			b = a.replace('-','')
			if b.isdigit(): #checking if modified data is valid
				validProfit+=1
				temp.append(row) #storing all valid rows
			totalRowCount+=1
		data2.write(json.dumps(temp, indent = 4)) #Writing all valid rows into output file

temp.sort(key=lambda row: row['Profit (in millions)'], reverse=True) #sorting to output top 20 rows with highest profit values
print("Total row count: " + str(totalRowCount)) 
print("Total valid row count: " + str(validProfit))
while top20 < 20:
	print(temp[top20])
	top20+=1

