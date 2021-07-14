import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt


class LR:
    def __init__(self, path):
        self.path = path


    def readFile(self):
         return pd.read_csv(path)

    def chooseData(self, fea, limit, x_name, y_name, df):
        data=[]
        x=[]
        y=[]
        for row in df.iterrows():
            if row[1][fea] == limit :
                x.append(row[1][x_name])
                y.append(row[1][y_name])
        data.append(x)
        data.append(y)
        return data

    def makeLR(self, df):
        # ten column muon chon vi du nhu : ten nuoc, ten luc dia ...
        print("Ten column muon chon:")
        fea = input()
        # gia tri cua column minh muon chon vi du nhu Japan, China, ...
        print("Gia tri cua column: ")
        limit = input()
        # column minh muon du doan x
        print("Dau vao x:")
        x = input()
        # column minh muon du doan y
        print("Phan muon du doan:")
        y = input()

        #tap du lieu x, y
        data = self.chooseData(fea, limit, x, y, df)
        x_data = np.array(data[0]).reshape(-1,1)
        y_data = np.array(data[1])

        self.runModel(x_data, y_data)

        data[x_data, y_data]
        return data

    def runModel(self, x_data, y_data):
        model = LinearRegression()
        model.fit(x_data, y_data)
        print("Nhap dau vao x:")
        x_input = float(input())
        x_arr = np.array(x_input).reshape(-1, 1)
        y_pred = model.predict(x_arr)
        print("Du doan: "+ str(round(y_pred[0], 0)))

    def visualize(self, x_data, y_data):
        #Visualize ket qua
        plt.scatter(x_data, y_data, color = "blue")
        plt.plot(x_data, model.predict(x_data), color = "yellow")
        plt.title("Visualization")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

