import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
        if len(countries) > 0:
            return countries
        else:
            return subcontinent

def checkSub(lst, coun):
    for name in lst:
        if name in coun:
            return True



data2 = pd.read_csv(r"C:\Users\phamv\Desktop\workspace\Projects\MAS_Proj_1\MAS_PROJECT\01_DATA\D04_Labour_market\01_Labour Force and Unemployment.csv")

all_countries = showCountry("Total, all countries or areas", data)
western_asia = showCountry("Western Asia", data)

def findCountriesbyYear(list, year, series):
    countries = []
    for row in data2.iterrows():
        if row[1]['NAME'] in list and row[1]['YEAR'] == year and row[1]['SERIES']==series:

                countries.append((row[1]["NAME"], row[1]['VALUE']))

    return sorted(countries, key=lambda x: x[1])

def findRatenCoun(name_list, year , series):
    lst = []
    for tup in name_list:
        for row in data2.iterrows():
            if row[1]['NAME'] == tup[0] and row[1]['YEAR'] == year and row[1]['SERIES']==series:
                lst.append((row[1]['NAME'], row[1]['VALUE']))
    return lst

def findUnqRate(lab_lst, unm_lst):
    not_a = []
    for i in range(len(lab_lst)):
        not_a.append((lab_lst[i][0], round(100-lab_lst[i][1]-unm_lst[i][1], 2)))

    return not_a



#Tren the gioi
#tim 5 nuoc co ty le lao dong thap nhat trong nam 2005
lst1 = findCountriesbyYear(all_countries, 2005, "Labour force participation - Total")
five_least_lab = lst1[:6]

#that nghiep
five_least_unm = findRatenCoun(five_least_lab, 2005, "Unemployment rate - Total")

#khong du kha nang lao dong
five_least_unq = findUnqRate(five_least_lab, five_least_unm)



#5 nuoc co ty le cao nhat o Western Asia trong nam 2005
lst4 = findCountriesbyYear(western_asia, 2005, "Labour force participation - Total")
five_most_lab = lst4[len(lst4)-6:]

#that nghiep
five_most_unm = findRatenCoun(five_most_lab, 2005, "Unemployment rate - Total")

#khong du kha nang lao dong
five_most_unq = findUnqRate(five_most_lab, five_most_unm)


#Stacked bar graph

def loadData(list1, list2, pos):
    lst = []
    for tup in range(len(list1)):
        lst.append(list1[tup][pos])

    for tup in range(len(list1)):
        lst.append(list2[tup][pos])

    return lst

label = loadData(five_least_lab, five_most_lab, 0)
labour_data = loadData(five_least_lab, five_most_lab, 1)
unm_data = loadData(five_least_unm, five_most_unm, 1)
unq_data = loadData(five_least_unq, five_most_unq, 1)

width = 0.35
bars = np.add(unq_data, unm_data).tolist()
fig, ax = plt.subplots()

ax.bar(label, unq_data, width,  label='Not afford')
ax.bar(label, unm_data, width,  bottom=unq_data,
       label='Unemployment rate - Total')
ax.bar(label, labour_data, width, bottom=bars,
       label='Labour force participation - Total')

ax.set_ylabel('Percent')
ax.set_title('Countries')
ax.legend()

plt.show()