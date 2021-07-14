
import pandas as pd

data = pd.read_csv(open(r'C:\Users\phamv\Downloads\MAS_PROJECT\01_DATA\COUNTRIES_CONTINENTS.csv', encoding= "utf8"))



def showCountry(Continent, data):

    subcontinent = []
    countries=[]

    for row in data.iterrows():
        if Continent == row[1]['NAME']:
            for row1 in data.iterrows():
                if row1[1]['PARENT_CODE'] == row[1]['CODE']:
                    subcontinent.append(row1[1]['NAME'])

    temp_subcon= subcontinent.copy()
    while len(temp_subcon)>0:
        temp=[]
        for name in temp_subcon:
            # print(name)
            for row in data.iterrows():

                if row[1]['NAME'] == name:
                    for row1 in data.iterrows():
                         if row1[1]['PARENT_CODE'] == row[1]['CODE']:
                            if checkSub(subcontinent, row1[1]['NAME']):
                                temp.append(row1[1]['NAME'])
                            else:
                                countries.append(row1[1]['NAME'])


        temp_subcon=temp.copy()
    if Continent == "Total, all countries or areas":
        return countries[6:]
    else:
        return countries

def checkSub(lst, coun):
    for name in lst:
        if name in coun:
            return True


