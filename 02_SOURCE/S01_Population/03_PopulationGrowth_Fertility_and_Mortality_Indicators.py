from matplotlib import pyplot
import csv
import pandas as pd
import numpy as np


data = csv.reader(open(r'F:\\GitHub\\MAS_PROJECT\\01_DATA\\D01_Population\\03_Population Growth, Fertility and Mortality Indicators.csv'))
data1 = pd.read_csv(r'F:\\GitHub\\MAS_PROJECT\\01_DATA\\D01_Population\\03_Population Growth, Fertility and Mortality Indicators.csv')
df = pd.DataFrame(data1, columns=['NAME','YEAR','SERIES','VALUE'])




def fact():
    condition = ['Total fertility rate (children per women)']
    conditon_2 = ['Population annual rate of increase (percent)']


    graph_name = []

    result = df.loc[df["YEAR"] == 2015]
    result_final = result.loc[result['SERIES'].isin(condition)]
    result2 = result_final.drop(index = 15)
    result3 = result_final.sort_values(by='VALUE', ascending=False)
    for name in result3.iterrows():
        graph_name.append(name[1]['NAME'])

    graph_name = graph_name[:3] + ['United States of America','China','Japan']
    value1 = []


    for name in graph_name:
        for row in df.iterrows():
            if row[1]['NAME'] == name and row[1]['YEAR'] == 2015 and row[1]['SERIES'] == 'Total fertility rate (children per women)':
                value1.append(row[1]['VALUE'])


    value2 = []
    for name in graph_name:
        for row in df.iterrows():
            if row[1]['NAME'] == name and row[1]['YEAR'] == 2015 and row[1]['SERIES'] == 'Population annual rate of increase (percent)':
                value2.append(row[1]['VALUE'])



    # lst = [graph_name,value1,value2]
    # print(lst)

    lst = {'name': graph_name,'value1': value1,'value2':value2}

    df2 = pd.DataFrame(lst)


    df2.plot(x = 'name', kind = 'bar',stacked = False, ylabel = 'Value')
    pyplot.xticks(rotation= 0)
    figure = pyplot.gcf()
    figure.set_size_inches(15, 10)

    pyplot.savefig(
        'F:\\GitHub\\MAS_PROJECT\\03_RESULT\\R01_Population\\03_PopulationGrowth_Fertility_and_Mortality_Indicators\\graph1.png')

    pyplot.show()



def mmr(series,data):
    values = []
    x = []
    y = []
    y2 = []
    z = []

    for row in data:
        if series == row[3] and row[2]=='2015':
            values.append((float(row[4]),row[1]))
    max_min = sorted(values,reverse=True)[:5] + sorted(sorted(values)[:5],reverse=True)

    for value,name in max_min:
        x.append(name)
        y.append(value)
    x2= []
    for name in x:
        data1 = csv.reader(open(r'F:\\GitHub\\MAS_PROJECT\\01_DATA\\D01_Population\\03_Population Growth, Fertility and Mortality Indicators.csv'))
        for row in data1:

            if name == row[1] and row[3] == 'Total fertility rate (children per women)' and row[2] == '2015':
                x2.append(row[1])
                y2.append(float(row[4]))
    # print(x2)
    # print(y2)
    z.append(x)
    z.append(y)
    z.append(y2)
    return z
series = 'Maternal mortality ratio (deaths per 100,000 population)'
lst_mmr = mmr(series,data)

# print(lst_mmr)
fig, ax1 = pyplot.subplots()
y_pos = np.arange(10)
plot = ax1.bar(y_pos,lst_mmr[1],align='center',alpha = 0.5)
ax1.set_xlabel('Country')
ax1.set_ylabel('values')
for value in plot:
    height = value.get_height()
    pyplot.text(value.get_x() + value.get_width()/2.,
             1.002*height,'%.2f' % float(height), ha='center', va='bottom')
ax2 = ax1.twinx()
ax2.plot(lst_mmr[0],lst_mmr[2],color = 'red')
figure = pyplot.gcf()
figure.set_size_inches(15, 10)

pyplot.show()

pyplot.savefig('F:\\GitHub\\MAS_PROJECT\\03_RESULT\\R01_Population\\03_PopulationGrowth_Fertility_and_Mortality_Indicators\\graph2.png')

fact()
