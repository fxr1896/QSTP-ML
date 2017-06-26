import pandas as pd
import numpy as np
from sklearn import linear_model
import seaborn as sns
import matplotlib.pyplot as plt

homicide_df = pd.read_csv(r"C:\Users\Raktim\Desktop\Study\QSTP\Datasets\Homicide\homicide.csv")

homicide_df["Perpetrator Age"].iloc[634666] = 0

homicide_df["Perpetrator Age"] = pd.to_numeric(homicide_df["Perpetrator Age"])

train_df = homicide_df[homicide_df["Perpetrator Age"] != 0]

train_df = train_df[train_df["Victim Age"] <= 100]

X = train_df["Victim Age"].reshape(-1,1)

Y = train_df["Perpetrator Age"].reshape(-1,1)

reg = linear_model.LinearRegression()

reg.fit(X,Y)

Xtest = homicide_df[homicide_df["Perpetrator Age"] == 0]

Xtest = homicide_df["Victim Age"][homicide_df["Victim Age"] <= 100].reshape(-1,1)
Ytest = reg.predict(Xtest)

plt.plot(X,Y,'bo' , alpha = 0.4)

plt.plot(Xtest , Ytest , 'r-')
