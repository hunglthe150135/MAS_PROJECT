import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math 
# x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
# y = np.array([5, 20, 14, 32, 22, 38])
# print(x)
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)
# print('coefficient of determination:', r_sq)

# y_pred = model.predict(x)
# print('predicted response:', y_pred, sep='\n')

# plt.scatter(x, y, color = "black")
# plt.plot(x, model.predict(x), color = "blue")
# plt.title("Visualization")
# plt.xlabel("Ox")
# plt.ylabel("Oy")
# plt.show()

# data = pd.read_csv(open(r'E:\EGDownloads\_FPT\MAS\_MAS_PROJECT\MAS_PROJECT\01_DATA\D04_Labour_market\01_Labour Force and Unemployment.csv', encoding= "utf8"))
# dataLabour = []
# for row in data.iterrows():
#     if row[1]['YEAR'] == 2020 and row[1]['SERIES'] == 'Labour force participation - Total' :
#         dataLabour.append((row[1]['NAME'], row[1]['VALUE']))

# data = pd.read_csv(open(r'E:\EGDownloads\_FPT\MAS\_MAS_PROJECT\MAS_PROJECT\01_DATA\D02_National_accounts\01_GDP_and_GDPPerCapita.csv', encoding= "utf8"))
# dataGdp = []
# for row in data.iterrows():
#     if row[1]['SERIES'] == 'GDP per capita (US dollars)' :
#         dataGdp.append((row[1]['NAME'], row[1]['YEAR'], row[1]['VALUE']))

# data2020 = []
# tempCountry = []
# previous = ''
# countriesDataLabour = []
# for i in range(len(dataLabour)):
#     countriesDataLabour.append(dataLabour[i][0])

# for i in range(len(dataGdp)):
#     if str(dataGdp[i][0]) not in countriesDataLabour: 
#         continue
#     while i < len(dataGdp) and (tempCountry == [] or str(dataGdp[i][0]) == str(tempCountry[0][0])):
#         tempCountry.append(dataGdp[i])
#         i = i+1
#     if previous != tempCountry[0][0]:
#         x = []
#         y = []
#         for tmp in tempCountry:
#             x.append(tmp[1])
#             y.append(tmp[2])
#         x = np.array(x).reshape((-1, 1))
#         y = np.array(y)
#         model = LinearRegression().fit(x, y)
#         data2020.append((tempCountry[0][0], model.predict(np.array(2020).reshape(-1, 1))[0]))
#         previous = tempCountry[0][0]
#     tempCountry = []

# countriesData2020 = []
# for i in range(len(data2020)):
#     countriesData2020.append(data2020[i][0])

# print(list(set(countriesDataLabour)-set(countriesData2020)))
# for i in countriesDataLabour:
#     if i in list(set(countriesDataLabour)-set(countriesData2020)):
#         countriesDataLabour.pop(countriesDataLabour.index(i))

# print(len(countriesDataLabour))
# dataLabourForce = []
# for i in dataLabour:
#     if i[0] in countriesDataLabour:
#         dataLabourForce.append(i)


# dataLabourForce = sorted(dataLabourForce)
# data2020 = sorted(data2020)

# x = []
# y = []
# for i in range(len(data2020)):
#     y.append(data2020[i][1])
#     x.append(dataLabourForce[i][1])

# x = np.array(x).reshape((-1, 1))
# y = np.array(y)

# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)
# print('coefficient of determination:', math.sqrt(r_sq))

# y_pred = model.predict(x)
# print('predicted response:', y_pred, sep='\n')

# plt.scatter(x, y, color = "black")
# plt.plot(x, model.predict(x), color = "blue")
# plt.title("Regression of labour force participation to GDP per capita")
# plt.xlabel("Labour force participation (%)")
# plt.ylabel("GDP per capita (US dollars)")
# plt.show()

# data = pd.read_csv(open(r'E:\EGDownloads\_FPT\MAS\_MAS_PROJECT\MAS_PROJECT\01_DATA\D01_Population\03_Population Growth, Fertility and Mortality Indicators.csv', encoding= "utf8"))
# dataFertility = []
# dataMortality = []
# countryFertality = []
# countryMortality = []
# for row in data.iterrows():
#     if row[1]['YEAR'] == 2015 and row[1]['SERIES'] == 'Total fertility rate (children per women)' :
#         dataFertility.append((row[1]['NAME'], row[1]['VALUE']))
#         countryFertality.append(row[1]['NAME'])

#     if row[1]['YEAR'] == 2015 and row[1]['SERIES'] == 'Maternal mortality ratio (deaths per 100,000 population)' :
#         dataMortality.append((row[1]['NAME'], row[1]['VALUE']))
#         countryMortality.append(row[1]['NAME'])

# # print(list(set(countryFertality)-set(countryMortality)))
# # print(len(countryFertality))
# # print(len(countryMortality))
# overlapCountry = list(set(countryFertality)-set(countryMortality))
# for i in dataFertility:
#     if i[0] in overlapCountry:
#         dataFertility.pop(dataFertility.index(i))
#         countryFertality.pop(countryFertality.index(i[0]))

# # print(len(countryFertality))
# # print(len(dataFertility))
# # print(list(set(countryFertality)-set(countryMortality)))
# overlapCountry = ['Asia', 'Middle Africa', 'Melanesia', 'Polynesia', 'Guam', 'Eastern Europe', 'Oceania', 'Central America', 
# 'French Polynesia', 'Western Africa', 'Southern Europe', 'China, Macao SAR']
# for i in dataFertility:
#     if i[0] in overlapCountry:
#         dataFertility.pop(dataFertility.index(i))
#         countryFertality.pop(countryFertality.index(i[0]))
# # print(list(set(countryFertality)-set(countryMortality)))

# overlapCountry = ['Melanesia', 'Asia', 'Southern Europe', 'Western Africa']
# for i in dataFertility:
#     if i[0] in overlapCountry:
#         dataFertility.pop(dataFertility.index(i))
#         countryFertality.pop(countryFertality.index(i[0]))
# # print(list(set(countryFertality)-set(countryMortality)))

# overlapCountry = ['Melanesia']
# for i in dataFertility:
#     if i[0] in overlapCountry:
#         dataFertility.pop(dataFertility.index(i))
#         countryFertality.pop(countryFertality.index(i[0]))
# # print(list(set(countryFertality)-set(countryMortality)))
# # print(len(dataFertility))
# # print(len(dataMortality))
# dataMortality = sorted(dataMortality)
# dataFertility = sorted(dataFertility)
# x = []
# y = []
# for i in range(len(dataMortality)):
#     y.append(dataMortality[i][1])
#     x.append(dataFertility[i][1])

# x = np.array(x).reshape((-1, 1))
# y = np.array(y)

# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)
# print('coefficient of determination:', math.sqrt(r_sq))

# plt.scatter(x, y, color = "black")
# plt.plot(x, model.predict(x), color = "blue")
# plt.title("Regression of fertility rate to mortality ratio")
# plt.xlabel("Total fertility rate (children per women)")
# plt.ylabel("Maternal mortality ratio (deaths per 100,000 population)")
# plt.show()


data = pd.read_csv(open(r'E:\EGDownloads\_FPT\MAS\_MAS_PROJECT\MAS_PROJECT\01_DATA\D03_Education\01_Education_at_the_primary_secondary_and_tertiary_levels.csv', encoding= "utf8"))
dataTertiaryMale = []
dataTertiaryFemale = []

for row in data.iterrows():
    if row[1]['YEAR'] == 2018 and row[1]['SERIES'] == 'Gross enrollment ratio - Tertiary (male)' :
        dataTertiaryMale.append((row[1]['NAME'], row[1]['VALUE']))
    if row[1]['YEAR'] == 2018 and row[1]['SERIES'] == 'Gross enrollment ratio - Tertiary (female)' :
        dataTertiaryFemale.append((row[1]['NAME'], row[1]['VALUE']))
dataTertiary = []
countryTertiary = []
for i in range(len(dataTertiaryFemale)):
    dataTertiary.append((dataTertiaryFemale[i][0], (dataTertiaryMale[i][1]/2+dataTertiaryFemale[i][1]/2)))
    countryTertiary.append(dataTertiaryFemale[i][0])

data = pd.read_csv(open(r'E:\EGDownloads\_FPT\MAS\_MAS_PROJECT\MAS_PROJECT\01_DATA\D02_National_accounts\01_GDP_and_GDPPerCapita.csv', encoding= "utf8"))
dataGdp = []
countryGdp = []
for row in data.iterrows():
    if row[1]['YEAR'] == 2018 and row[1]['SERIES'] == 'GDP per capita (US dollars)' :
        dataGdp.append((row[1]['NAME'], row[1]['VALUE']))
        countryGdp.append(row[1]['NAME'])

overlapCountry = list(set(countryGdp)-set(countryTertiary))
while len(overlapCountry) != 0:
    for i in dataGdp:
        if i[0] in overlapCountry:
            dataGdp.pop(dataGdp.index(i))
            countryGdp.pop(countryGdp.index(i[0]))
    overlapCountry = list(set(countryGdp)-set(countryTertiary))

dataGdp = sorted(dataGdp)
dataTertiary = sorted(dataTertiary)

x = []
y = []
for i in range(len(dataGdp)):
    y.append(dataGdp[i][1])
    x.append(dataTertiary[i][1])

x = np.array(x).reshape((-1, 1))
y = np.array(y)

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', math.sqrt(r_sq))

plt.scatter(x, y, color = "black")
plt.plot(x, model.predict(x), color = "blue")
plt.title("Regression of gross enrollment (tertiary) to GDP per capita")
plt.xlabel("Gross enrollment ratio - Tertiary (%)")
plt.ylabel("GDP per capita (US dollars)")
plt.show()
# data2020 = []
# tempCountry = []
# previous = ''
# countriesDataLabour = []
# for i in range(len(dataLabour)):
#     countriesDataLabour.append(dataLabour[i][0])

# for i in range(len(dataGdp)):
#     if str(dataGdp[i][0]) not in countriesDataLabour: 
#         continue
#     while i < len(dataGdp) and (tempCountry == [] or str(dataGdp[i][0]) == str(tempCountry[0][0])):
#         tempCountry.append(dataGdp[i])
#         i = i+1
#     if previous != tempCountry[0][0]:
#         x = []
#         y = []
#         for tmp in tempCountry:
#             x.append(tmp[1])
#             y.append(tmp[2])
#         x = np.array(x).reshape((-1, 1))
#         y = np.array(y)
#         model = LinearRegression().fit(x, y)
#         data2020.append((tempCountry[0][0], model.predict(np.array(2020).reshape(-1, 1))[0]))
#         previous = tempCountry[0][0]
#     tempCountry = []

# countriesData2020 = []
# for i in range(len(data2020)):
#     countriesData2020.append(data2020[i][0])

# print(list(set(countriesDataLabour)-set(countriesData2020)))
# for i in countriesDataLabour:
#     if i in list(set(countriesDataLabour)-set(countriesData2020)):
#         countriesDataLabour.pop(countriesDataLabour.index(i))

# print(len(countriesDataLabour))
# dataLabourForce = []
# for i in dataLabour:
#     if i[0] in countriesDataLabour:
#         dataLabourForce.append(i)


# dataLabourForce = sorted(dataLabourForce)
# data2020 = sorted(data2020)

# x = []
# y = []
# for i in range(len(data2020)):
#     y.append(data2020[i][1])
#     x.append(dataLabourForce[i][1])

# x = np.array(x).reshape((-1, 1))
# y = np.array(y)

# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)
# print('coefficient of determination:', math.sqrt(r_sq))

# y_pred = model.predict(x)
# print('predicted response:', y_pred, sep='\n')

# plt.scatter(x, y, color = "black")
# plt.plot(x, model.predict(x), color = "blue")
# plt.title("Regression of labour force participation to GDP per capita")
# plt.xlabel("Labour force participation (%)")
# plt.ylabel("GDP per capita (US dollars)")
# plt.show()

