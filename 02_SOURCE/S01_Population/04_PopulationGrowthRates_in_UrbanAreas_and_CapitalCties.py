from matplotlib import pyplot
import pandas as pd
import xlsxwriter
import csv

data = pd.read_csv(r'F:\\GitHub\\MAS_PROJECT\\01_DATA\\D01_Population\\04_Population Growth Rates in Urban areas and Capital cities.csv')
df = pd.DataFrame(data,columns=['CODE','NAME','YEAR','SERIES','CAPITAL_CITY','VALUE'])
df2 = df.append(df)



def question_a():
    capital = ['Viet Nam', 'Thailand','Malaysia','Indonesia','Timor-leste','Myanmar','Brunei','Cambodia','Laos','Philippines','Singapore']
    condition_1 = ['Urban population (percent)']
    condition_2 = ['Urban population (percent growth rate per annum)']
    result_raw = df.loc[df['YEAR'] == 2015]
    result_raw2 = df2.loc[df['YEAR'] == 2015]
    result_condition_1 = result_raw.loc[result_raw['SERIES'].isin(condition_1)]
    graph_1_y = result_condition_1['VALUE']
    result_condition_2 = result_raw2.loc[result_raw2['SERIES'].isin(condition_2)]
    graph_2_y = result_condition_2['VALUE']
    result_condition_capital = result_raw.loc[result_raw['NAME'].isin(capital)]
    graph_name = result_condition_capital['NAME']

    fig, ax1 = pyplot.subplots(1,1,figsize = (6,4))
    ax1.plot(capital,graph_1_y)

    ax2 = ax1.twinx()
    ax2.plot(capital,graph_2_y,color = 'blue')

    ax1.set_ylabel('Name Y1', color = 'red')
    ax1.set_xlabel('Year')
    ax2.ticl_params(axis='y',labelcolor = 'blue')



    pyplot.show()

    pyplot.savefig('F:\\GitHub\\MAS_PROJECT\\03_RESULT\\R01_Population\\04_Population Growth Rates in Urban areas and Capital cities\\question_a.png')


def question_b():
    final = []
    condition = ['Urban population (percent growth rate per annum)']
    value_condition = df.loc[df['YEAR'] == 2015].sort_values(by='VALUE', ascending=False)
    vietnam = df2.loc[(df.NAME == "Viet Nam") & (df.SERIES == "Urban population (percent growth rate per annum)" )]
    vietnam1 = vietnam.loc[vietnam.VALUE == 3.2]
    final.append(vietnam1)
    moving_column = value_condition.drop(columns = ['CAPITAL_CITY'])
    print(final)
    moving_column_1 = moving_column.set_index('CODE')
    # moving_column_1 = moving_column_1.drop(str(524))
    result = moving_column.loc[moving_column['VALUE'] <= str(3.1)]
    print("......")
    print(result)

    # final.append(result)

    compression_opts = dict(method = 'zip', archive_name= 'Result_question_b.csv')
    result.to_csv('F:\\GitHub\\MAS_PROJECT\\03_RESULT\\R01_Population\\04_PopulationGrowthRates_in_UrbanAreas_and_CapitalCties\\Result_question_b.zip',index=False, compression=compression_opts)




def question_c():
    continents = ['Northern Africa','Western Africa','Eastern Africa','Sub-Saharan Africa','Total, all countries or areas', 'Southern Africa', 'Middle Africa','Caribbean','Latin America & the Caribbean','Central America','Eastern Asia','South-eastern Asia','Southern Asia','Western Asia','Eastern Europe','Southern Europe','Western Europe','Northern Africa','Europe', 'Asia', 'Africa', 'Oceania', 'Northern America', 'South America']
    condition = ['Total, all countries or areas']
    condition_series = ['Urban population (percent)']
    urban_world = df.loc[df['YEAR'] == 2018]

    print(urban_world)
    result_world = urban_world.loc[urban_world['SERIES'].isin(condition_series)]
    print(result_world)
    result_world_1 = result_world.loc[result_world['NAME'].isin(continents)]
    print(result_world_1)
    show_result = result_world_1.sort_values(by='VALUE', ascending=False)
    graph_name = show_result['NAME'].head(10)
    graph_value = show_result['VALUE'].head(10)


    pyplot.bar(graph_name,graph_value,color='red')
    pyplot.ylim(0,50)
    pyplot.axis("equal")
    pyplot.xticks(rotation = 45)

    pyplot.show()

# def question_d():

question_a()