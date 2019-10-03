import warnings; warnings.simplefilter("ignore")
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import csv

#read workbook
events= pd.read_csv(r"/home/rauchdi/Desktop/5A IPS/Madeth/Pastel/Traces outil PASTEL/cleaned_events1.csv")

#print all data
#print(events)

#events[["id","userId"]]

#with open('mycsv.csv','w',newline='') as f:
#    thewriter = csv.writer(f)

#    thewriter.writerows(events[:])

l=['mehdi','ali',0]
x=['ali',0,'moha']

n=0

for i in l:
    if i in x:
        n+=1

print(n)


