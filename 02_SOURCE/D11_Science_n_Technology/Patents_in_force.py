import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv(open(r'C:\Users\phamv\Desktop\workspace\Projects\MAS_Proj_1\MAS_PROJECT\01_DATA\D11_Science_and_Technology\03_Patents.csv', encoding= "utf8"))

# 10 quoc gia co patent in force cao nhat tg
countries = []
for row in data.iterrows():
    if row[1]['YEAR'] == 2018 and row[1]['SERIES'] == 'Patents in force (number)' :
        countries.append((row[1]['NAME'], row[1]['VALUE']))

countries.sort( key = lambda tup: tup[1], reverse=True)
countries = countries[:10]
name = []
value = []
for cou in countries:
    name.append(cou[0])
    value.append(cou[1])


#Draw
fig1 = plt.figure(figsize=(10, 5))

plt.bar(name, value, color='blue',
        width=0.4)

plt.xlabel("Countries")
plt.ylabel("numbers")
plt.title("Patents in force (number)")
plt.show()


#My va Trung Quoc tu nam 2017
countries_comp = ['China', 'United States of America']
Ch_values = []
A_values = []
years = [2005, 2010, 2016, 2017, 2018]
for year in years:

    for row in data.iterrows():
        if row[1]['NAME'] == 'China' and  row[1]['YEAR'] == year and row[1]['SERIES'] == 'Patents in force (number)' :

            Ch_values.append(row[1]['VALUE'])
        if row[1]['NAME'] == 'United States of America' and  row[1]['YEAR'] == year and row[1]['SERIES'] == 'Patents in force (number)':
            A_values.append(row[1]['VALUE'])


# #Linear Regression
model_Ch = LinearRegression()
model_Ch.fit(np.array(years).reshape(-1, 1), Ch_values)

model_A = LinearRegression()
model_A.fit(np.array(years).reshape(-1, 1), A_values)
y_pred_Ch = model_Ch.predict(np.array(2019).reshape(-1, 1))
y_pred_A = model_A.predict(np.array(2019).reshape(-1, 1))
start_year = 2019

while(y_pred_A> y_pred_Ch):
    start_year = start_year+1
    years.append(start_year)
    y_pred_Ch = model_Ch.predict(np.array(start_year).reshape(-1, 1))
    Ch_values.append(int(round(y_pred_Ch[0],0)))
    y_pred_A = model_A.predict(np.array(start_year).reshape(-1, 1))
    A_values.append(int(round(y_pred_A[0], 0)))
print(years)
print(Ch_values)
print(A_values)
#Draw
years = years[4:]

x = np.arange(len(years))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, Ch_values[4:], width, label='China')
ax.bar(x + width/2, A_values[4:], width, label='USA')
ax.set_title('Patents in Force comparision between USA and China')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(years)

ax.legend()
plt.show()