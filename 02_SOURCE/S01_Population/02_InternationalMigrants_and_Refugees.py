from matplotlib import pyplot
import csv
import pandas as pd
import numpy as np


data = pd.read_csv(r'F:\\GitHub\\MAS_PROJECT\\01_DATA\\D01_Population\\02_International Migrants and Refugees.csv')
df = pd.DataFrame(data, columns=['CODE','NAME','YEAR','SERIES','VALUE'])

def question_a():
    continents = ['Europe', 'Asia', 'Africa', 'Oceania', 'Northern America', 'South America']
    condition = ['International migrant stock: Both sexes (% total population)']
    result = df.loc[df['YEAR'] == 2019]
    result_final = result.loc[result['SERIES'].isin(condition)]
    result_final_1 = result_final.loc[result_final['NAME'].isin(continents)]

    graph_name = result_final_1['NAME']
    graph_value = result_final_1['VALUE']

    pyplot.plot(graph_name,graph_value,color='green')

    pyplot.show()
    pyplot.savefig('F:\\GitHub\\MAS_PROJECT\\03_RESULT\\R01_Population\\02_InternationalMigrants_and_Refugees\\question_a.png')


def question_b():
    code_condition = [ 9, 155, 39, 154, 151, 150, 145, 34, 35, 30, 143, 142, 5,13, 29, 419, 21, 11,18,17,14,202,15,2]
    condition = ['International migrant stock: Both sexes (% total population)']
    result = df.loc[df['YEAR'] == 2019]
    result_final = result.loc[result['SERIES'].isin(condition)]
    show_result = result_final.sort_values(by='VALUE', ascending=False)
    #Chưa thế tìm ra cách để tên chéo như trong Docs mà BA yêu cầu
    graph_name = show_result['NAME'].head(10)
    graph_value = show_result['VALUE'].head(10)
    #Nếu present sử dụng Pycharm thì đạt lại size để có thể có output rõ hơn
    #pyplot.figure(figsize=(14.00, 8.0))
    pyplot.plot(graph_name,graph_value)
    pyplot.xlabel("Name")
    pyplot.ylabel("Value")
    pyplot.show()

    pyplot.savefig('F:\\GitHub\\MAS_PROJECT\\03_RESULT\\R01_Population\\02_InternationalMigrants_and_Refugees\\question_b.png')

def question_c():

    year = [2005, 2010, 2015, 2019]

    male = ['International migrant stock: Male (% total Population)']
    female = ['International migrant stock: Female (% total Population)']

    result = df.loc[df['CODE'] == 704]
    male_graph = result.loc[result['SERIES'].isin(male)]
    female_graph = result.loc[result['SERIES'].isin(female)]

    male_value = male_graph['VALUE']
    female_value = female_graph['VALUE']


    #pyplot.figure(figsize=(1920,1080))
    pyplot.xticks(year)
    pyplot.plot(year,male_value , color = 'blue')
    pyplot.plot(year,female_value , color = 'red')
    pyplot.xlabel("Year")
    pyplot.ylabel("Value")

    pyplot.savefig('F:\\GitHub\\MAS_PROJECT\\03_RESULT\\R01_Population\\02_InternationalMigrants_and_Refugees\\question_c.png')

    pyplot.show()

question_a()
question_b()
question_c()

