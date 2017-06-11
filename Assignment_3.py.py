import pandas as pd
import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt

gpa_df = pd.read_excel(r"C:\Users\Raktim\Desktop\Study\QSTP\Assignments\Assignment 3\sat.xls")

x_train = pd.DataFrame({"ones" : np.ones(gpa_df.shape[0]) , "high_GPA" : gpa_df["high_GPA"]})
x_train = np.array(x_train[["ones" , "high_GPA"]])
y_train = np.array(gpa_df["univ_GPA"])
xt = np.transpose(x_train)

theta = np.dot(np.dot(inv(np.dot(xt,x_train)),xt),y_train)

theta_0 = theta[0]
theta = theta[1]

plt.plot(gpa_df["high_GPA"] , gpa_df["univ_GPA"] , 'bo')
plt.plot(gpa_df["high_GPA"] , [(theta_0 + (theta*x))for x in gpa_df["high_GPA"]] , 'r-')

def univ_GPA(high_gpa):
    return (theta_0 + theta*high_gpa)
