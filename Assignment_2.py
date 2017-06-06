import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

homicide_df = pd.read_csv(r"C:\Users\Raktim\Desktop\Study\QSTP\Datasets\Homicide\homicide.csv")

# Graph of Weapons by year
homicide_weapons_df = homicide_df[["Year","Weapon"]]

s = homicide_weapons_df.groupby('Year')

weapons_list = ['Handgun' , 'Knife' , 'Blunt Object' ,'Shotgun']
weapons_by_year =[]

for i in np.arange(1980,2015):
    weapons =[i]
    for j in weapons_list:
        weapons.append(s.get_group(i)["Weapon"].value_counts()[j])
    weapons_by_year.append(weapons)

del weapons
weapons_by_year = np.array(weapons_by_year)

weapons_by_year = pd.DataFrame(weapons_by_year)
weapons_by_year.columns = ["Year","Handgun" , "Knife" , "Blunt Object" ,"Shotgun"]

plt.plot(weapons_by_year["Year"] , weapons_by_year["Handgun"] ,'r-', label = 'Handgun')
plt.plot(weapons_by_year["Year"] , weapons_by_year["Knife"] , 'b-' , label ='Knife')
plt.plot(weapons_by_year["Year"] ,weapons_by_year["Blunt Object"] , 'k-' , label ='Blunt Object')
plt.plot(weapons_by_year["Year"] ,weapons_by_year["Shotgun"] , 'y-' ,label ='Shotgun')
plt.title('No. Of Homicides vs. Year')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
plt.xlabel('Year')
plt.ylabel('Number Of Homicides')
plt.show()

# Graph relationship vs year

homicide_rel_df =homicide_df[["Year","Relationship"]]

r = homicide_rel_df.groupby("Year")

relationship_list = ["Acquaintance" ,"Stranger" ,"Wife" ,"Ex-Wife"]

rel_by_year = []
for i in np.arange(1980,2015):
    rel = [i]
    for j in relationship_list:
        rel.append(r.get_group(i)["Relationship"].value_counts()[j])
    rel_by_year.append(rel)
del rel 
rel_by_year = np.array(rel_by_year)

rel_by_year = pd.DataFrame(rel_by_year)
rel_by_year.columns = ["Year" ,"Acquaintance" ,"Stranger" ,"Wife" ,"Ex-Wife"]

plt.plot(rel_by_year["Year"] , rel_by_year["Acquaintance"] , 'r-' , label = "Acquaintance")
plt.plot(rel_by_year["Year"] , rel_by_year["Stranger"] , 'b-' , label = "Stranger")
plt.plot(rel_by_year["Year"] , rel_by_year["Wife"] , 'k-' , label = "Wife")
plt.plot(rel_by_year["Year"] , rel_by_year["Ex-Wife"] , 'y-' , label = "Ex-Wife")
plt.title('No. Of Homicides vs. Year')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
plt.xlabel('Year')
plt.ylabel('Number Of Homicides')
plt.show()

# Boxplots

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6,6), sharey=True)

axes[0,0].boxplot(weapons_by_year["Handgun"])
axes[0,0].set_title('Handgun')
axes[0,1].boxplot(weapons_by_year["Knife"])
axes[0,1].set_title('Knife')
axes[1,0].boxplot(weapons_by_year["Blunt Object"])
axes[1,0].set_title('Blunt Object')
axes[1,1].boxplot(weapons_by_year["Shotgun"])
axes[1,1].set_title('Shotgun')
plt.show()

