import csv



#doc file csv
data = csv.reader(open('/home/vietduong/Desktop/workspace/MAS_Proj/MAS_PROJECT/01_DATA/COUNTRIES_CONTINENTS.csv', 'r'))
data1= csv.reader(open('/home/vietduong/Desktop/workspace/MAS_Proj/MAS_PROJECT/01_DATA/COUNTRIES_CONTINENTS.csv', 'r'))

def showContinent(countries, data):
    for row in data:
        if(countries == row[1]):
            for row1 in data1:
                print(row1)
                if row1[0] == row[2]:
                    print(row1[0])
                    return row1[1]
            


countries = input()

print(showContinent(countries, data))




