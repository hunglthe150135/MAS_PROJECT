import csv
import matplotlib.pyplot as plt
import numpy as np


data = csv.reader(open(r'C:\Users\dell\OneDrive\Desktop\MAS\MAS_PROJECT\01_DATA\D01_Population\01_Population, Surface Area and Density.csv'))
data1 = csv.reader(open(r'C:\Users\dell\OneDrive\Desktop\MAS\MAS_PROJECT\01_DATA\D01_Population\01_Population, Surface Area and Density.csv'))


def density(series, data):
    values = []
    x = []
    y = []
    NAME = input()
    for row in data:
        if (NAME == row[1]):
            if row[3] == series:
                x.append(row[2])
                y.append(row[4])
    values.append(x)
    values.append(y)

    return values




series = 'Population density'
lst_VN = density(series, data)
lst_Total = density(series, data1)
def cal(list,n):
    x = float(list[n][0])
    x1 = float(list[n][-1])
    X = x1-x
    return X
def pred(lst):
    Inc = cal(lst,1)/cal(lst,0)
    Result = float(lst[1][0]) + Inc*(2100-float(lst[0][0]))
    return Result
x = pred(lst_VN)
y = pred(lst_Total)

print('Population density of Viet Nam in 2100 = ',round(x,4),'people/km2')
print('Population density of The World in 2100 = ',round(y,4),'people/km2')
lst_VN[0].append(2100)
lst_VN[1].append(round(x,4))
lst_Total[0].append(2100)
lst_Total[1].append(round(y,4))
print(lst_VN)
print(lst_Total)

plt.plot(lst_Total[0],lst_Total[1])
plt.plot(lst_VN[0],lst_VN[1])
plt.legend(['The world','Viet Nam'])
plt.show()
data2 = csv.reader(open(r'C:\Users\dell\OneDrive\Desktop\MAS\MAS_PROJECT\01_DATA\D01_Population\01_Population, Surface Area and Density.csv'))
def sexRatio(series,data):
    values = []
    x = []
    y = []
    for row in data:
        if row[3] == series:
            if float(row[4]) >106:
                x.append(row[1])
                y.append(row[4])
    values.append(x)
    values.append(y)
    return values
lst_values = sexRatio('Sex ratio (males per 100 females)',data2)
print(lst_values)
