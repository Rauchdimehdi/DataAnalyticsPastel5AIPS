import warnings; warnings.simplefilter("ignore")
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import csv

#read workbook
note= pd.ExcelFile(r"/home/rauchdi/Desktop/5A IPS/Madeth/Pastel/NotesGpV1.xlsx")

#print all data
#print(note)

dfs = {sheet_name: note.parse("Sheet1") 
          for sheet_name in note.sheet_names}



def extract():
    x=dfs.values()
    #transformer en str
    s=str(dfs)
    #diviser les données
    spli=s.splitlines()
    #enlevé les ****
    spli.remove("{'Sheet1':                 Barême: ")
    #faire les groupe brute
    nwList=[]
    for i in spli:
        nwList.append(i.split(" "))
    for j in range(0,len(nwList)):
        while '' in nwList[j]:
            nwList[j].remove('')
    #faire les 
    G1,G2,G3,G4,G5,G6=['G1'],['G2'],['G3'],['G4'],['G5'],['G6']
    for i in range(0,len(nwList)):
        if int(nwList[i][0]) >0 and int(nwList[i][0])<5 :
            G1.append(nwList[i][1:][0])
        if int(nwList[i][0]) >5 and int(nwList[i][0])<11 :
            G2.append(nwList[i][1:][0])
        if int(nwList[i][0]) >11 and int(nwList[i][0])<16 :
            G3.append(nwList[i][1:][0])
        if int(nwList[i][0]) >16 and int(nwList[i][0])<21 :
            G4.append(nwList[i][1:][0])
        if int(nwList[i][0]) >21 and int(nwList[i][0])<27 :
            G5.append(nwList[i][1:][0])
        if int(nwList[i][0]) >27 :
            G6.append(nwList[i][1:][0])
    
    
    #print(nwList)
    #print(G1)
    tete=['nomGroup','M1','M2','M3','M4','M5']
    with open ('groupe.csv','w') as new_file:
        csv_writer =csv.writer(new_file, delimiter=',')
        csv_writer.writerow(tete)
        csv_writer.writerow(G1)
        csv_writer.writerow(G2)
        csv_writer.writerow(G3)
        csv_writer.writerow(G4)
        csv_writer.writerow(G5)
        csv_writer.writerow(G6)
        


print(extract())  


