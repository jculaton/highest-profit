# Highest-profit solution

## Deliverables

### Part 1
1) Printing total number of data rows from provided input file
2) Printing all rows with profit column containing numerical values

### Part 2:
1) Printing top 20 rows with highest profit values

### Part 3: 
1) data2.json is created

## Thought Process

I chose to code my solution in Python3 so I could use the csv and json libraries.

I checked data.csv to see what kinds of values the profit column had. I found 3 types: int, (positive and negative) float, and 'N.A.' The only invalid case is N.A. My solution was to access the profit value, remove '.' and '-', then see if the modified value is valid. The only case that would fail this check is 'N.A.' and I would omit it from the list (temp) to be written to data2.json.

After writing all of the valid data rows into data2.json, I sorted the list in descending order and printed the top 20 rows using a while loop. 

To verify my output values were correct, I used Excel to find the total number of data rows and used command + find to get the frequency of N.A. in the profit column. Then I subtracted the total rows - N.A. frequency and compared with my code output. 
