import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

homicide=pd.read_csv(r"C:\Users\Raktim\Desktop\Study\QSTP\Datasets\Homicide\homicide.csv")

# Number of cases solved
len(homicide[homicide["Crime Solved"] == "Yes"])

# Top five weapons used
weapons_used=Counter(homicide["Weapon"])

plt.bar(range(len(weapons_used)),weapons_used.values())
plt.xticks(range(0,len(weapons_used)),weapons_used,rotation=75)

plt.show()

#OR
i=0
for x in sorted(weapons_used, key = weapons_used.get , reverse = True):
    if i <= 5 :
        print (x , weapons_used[x])
        i += 1
    else :
        break
    
#State-wise most used weapon 

us_states = pd.read_csv(r"C:\Users\Raktim\Desktop\Study\QSTP\Datasets\Homicide\american_states.csv")
us_states.drop("Abbreviation" , axis = 1 , inplace = True)
us_states = us_states[us_states["State"] != "Rhode Island"]
def by_state(state):
    try:
        state_df = homicide[homicide["State"] == state ]
        total_weapons = state_df.shape[0]
        current_weapons = Counter(state_df["Weapon"])
        
        for x in sorted(current_weapons , key = current_weapons.get , reverse= True):
            weapon_required = { x : (current_weapons[x]/total_weapons)*100}
            return (weapon_required)
       
    except(ValueError,IndexError,ZeroDivisionError):
            return

for i in us_states["State"]:
    print (i , by_state(i))

#Bar Graph by Year

homicide_by_year = []

for x in range(1980,2015):
    dummy_df = homicide[homicide["Year"] == x]
    homicide_by_year.append(dummy_df.shape[0])

homicide_by_year_df = pd.DataFrame({"Year" : range(1980,2015) , "No_Of_Homicides" :homicide_by_year})

plt.bar(homicide_by_year_df["Year"],homicide_by_year_df["No_Of_Homicides"],width = 0.5)
plt.xticks(range(1980,2015,2),range(1980,2015,2),rotation = 90)
plt.show()


