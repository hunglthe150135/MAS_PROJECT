import csv
import os

#dung function de doc file csv
#function se lay duong link tuong doi theo dang 'D01_Population/01_Population, Surface Area and Density.csv'
#sau do tra ve file data
#Dai co the sua csv.reader thanh pd.read csv roi return ra dataframe
def read_csv(path):
	array = format(os.getcwd()).split('\\')
	array = array[:array.index('MAS_PROJECT') + 1]
	toData = ['01_DATA']
	array += toData
	toCsv = path
	array += toCsv.split('/')
	absolutePath = ''
	for step in array:
    		if step.startswith('0'): absolutePath += '\\'
    		absolutePath += step + "\\"

	absolutePath = absolutePath[:len(absolutePath) - 1]

	data = csv.reader(open(absolutePath, 'r'))

	return data

input_path =input()

data = read_csv(input_path)

for row in data:
	print(row)