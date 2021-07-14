import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\phamv\Desktop\workspace\Projects\MAS_Proj_1\MAS_PROJECT\01_DATA\D02_National_accounts\01_GDP_and_GDPPerCapita.csv")

countries = ['Qatar', 'United Arab Emirates', 'Saudi Arabia', 'Iran (Islamic Republic of)', 'Iraq', 'Pakistan']
#get value
val = []
for name in countries:

    for row in data.iterrows():
        if row[1]['NAME'] == name and row[1]['YEAR']==2018 and row[1]['SERIES'] == 'GDP per capita (US dollars)':
           val.append(row[1]['VALUE'])

#draw

fig = plt.figure(figsize=(10, 5))

plt.bar(countries, val, color='blue',
        width=0.4)

plt.xlabel("Countries")
plt.ylabel("US dollars")
plt.title("GDP per capita(US dollars)")
plt.show()