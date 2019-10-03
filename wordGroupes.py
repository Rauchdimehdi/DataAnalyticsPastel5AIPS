import csv 


with open('groupe.csv','r') as group:
    csv_reader =csv.reader(group)

    next(csv_reader)
    G=[]
    for line in csv_reader:
        G.append(line)
    #print(G)
    G1,G2,G3,G4,G5,G6=[],[],[],[],[],[]
    for i in range(len(G)):
        if i==0:
            G1=G[i][1:]
        elif i==1:
            G2=G[i][1:]
        elif i==2:
            G3=G[i][1:]
        elif i==3:
            G4=G[i][1:]
        elif i==4:
            G5=G[i][1:]
        else:
            G6=G[i][1:]
    

with open('/home/rauchdi/Desktop/5A IPS/Madeth/Pastel/Trello Et Etherpad/full_users_notes.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)
    #sauter la premiere ligne
    next(csv_reader)
    #print(csv)
    data=[]
    for line in csv_reader:
        #ajouter nom et nombre de word
        l=[line[4],line[11]]
        data.append(l)
        #print('\n')
        #l.write("\n")

    

    #print(data)
    #calculer le nbr de mot par groupe
    nbG1,nbG2,nbG3,nbG4,nbG5,nbG6=0,0,0,0,0,0    
    for item in data:
        #print(item[0])
        if item[0] in G1:
            #print(item[0])
            #incrementer nbG1
            nbG1= nbG1+ int(item[1])
        elif item[0] in G2:
            #print(item[0])
            #incrementer nbG1
            nbG2+=int(item[1])
        elif item[0] in G3:
            #print(item[0])
            #incrementer nbG1
            nbG3+=int(item[1])
        elif item[0] in G4:
            #print(item[0])
            #incrementer nbG1
            nbG4+=int(item[1])
        elif item[0] in G5:
            #print(item[0])
            #incrementer nbG1
            nbG5+=int(item[1])
        else:
            #print(item[0])
            #incrementer nbG1
            nbG6+=int(item[1])

    #print(nbG1,nbG2,nbG3,nbG4,nbG5,nbG6)
    li=[str(nbG1),str(nbG2),str(nbG3),str(nbG4),str(nbG5),str(nbG6)]

tete=['G1','G2','G3','G4','G5','G6']
with open ('nbMortParGroupe.csv','w') as new_file:
    csv_writer =csv.writer(new_file, delimiter=',')
    csv_writer.writerow(tete)
    csv_writer.writerow(li)
    
            
            
             
    #print(data)