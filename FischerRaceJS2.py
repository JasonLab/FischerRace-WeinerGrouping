print("Welcome to the Rh grouping helper. Please enter your results as indicated.")
Rh_Pheno= input("Please enter the antigens that were positive. So for example if you got D+C+c-E+e+ you would enter DCEe. If D is neg you don't need to enter d:  ")
Rh_List=['d'] #d always present so we left it here instead of Rh_ALL
Rh_All=['D','C','c','E','e'] #Provides list which is used to search users input
D_Group=['d','D']
Patient_D=[]
E_Group=["E","e"]
Patient_E=[]
C_Group=['C','c']
Patient_C=[]
Rh_Combos=[]
Rh_Combos2=[]
Final_Combos=[] #List of Legal Combos after being sifted through
Wiener_Temp=[]
Wiener_Group=[]
Wiener_Orders=[]
ESChecker = 0
EqualScore=[]
FC_Counter = -3   #Counters necessary to run the Wiener grouping loop
FC_Counter2 = -2 #Needs to remain 1 higher than other counter
for x in Rh_All:
    if x in Rh_Pheno:
        Rh_List.append(x)
#print(Rh_List) checkpoint commented out
for x in Rh_List:
    if x in D_Group:
        Patient_D.append(x)
#print(Patient_D) checkpoint commented out
for x in Rh_List:
    if x in E_Group:
        Patient_E.append(x)
#print(Patient_E) checkpoint commented out
for x in Rh_List:
    if x in C_Group:
        Patient_C.append(x)
#print(Patient_C) checkpoint commented out

for d in Patient_D:
    for c in Patient_C:
        for e in Patient_E:
            Rh_Combos.append(d+c+e)  #Old way of getting all the possible iterations
            #print(Rh_Combos)  Commenting out this checkpoint
for x in Rh_Combos:
    for y in Rh_Combos:
        if  (x+y) not in Rh_Combos2 and(y+x) not in Rh_Combos2: #The y+x is redundant but I kept it as a momento of my tiredness
            Rh_Combos2.append(x+y)
            #print(Rh_Combos2) Commenting out this checkpoint
Rh_List.remove('d') #To prevent the next for from forcing a d into the combination.
print("Your final combinations are as follows: ")
for x in Rh_Combos2:
    if len(Rh_List) == 3:
        if Rh_List[0] in x and Rh_List[1] in x and Rh_List[2] in x: #If all patient letters in then its acceptable
            print(x)
            Final_Combos.append(x)
    elif len(Rh_List) == 2:
        if Rh_List[0] in x and Rh_List[1] in x:
            print(x)
            Final_Combos.append(x)
    elif len(Rh_List) == 4:
        if Rh_List[0] in x and Rh_List[1] in x and Rh_List[2] in x and Rh_List[3] in x:
            print(x)
            Final_Combos.append(x)
    elif len(Rh_List) == 5:
        if Rh_List[0] in x and Rh_List[1] in x and Rh_List[2] in x and Rh_List[3] in x and Rh_List[4] in x:
            print(x)
            Final_Combos.append(x)
#Wiener grouping begins
print("The possible Wiener groupings are as follows: ")
FC_Counter = FC_Counter + 1
FC_Counter2= FC_Counter2 + 1
for x in Final_Combos:
    if 'DceDce' in x:
        Wiener_Temp.append('R0')
    if 'DCeDCe' in x:
        Wiener_Temp.append('R1')
    if 'DcEDcE' in x:
        Wiener_Temp.append('R2')
    if 'DCEDCE' in x:
        Wiener_Temp.append('RZ')
    if 'dcEdcE' in x:
        Wiener_Temp.append('rII')
    if 'dCedCe' in x:
        Wiener_Temp.append('rI')
    if 'dCEdCE' in x:
        Wiener_Temp.append('ry')
    if 'dce' in x:
        Wiener_Temp.append('r')
    if 'DcE' in x:
        Wiener_Temp.append('R2')
    if 'dcE'in x:
        Wiener_Temp.append('rII')
    if 'dCe'in x:
        Wiener_Temp.append('rI')
    if 'dCE'in x:
        Wiener_Temp.append('ry')
    if 'DCE'in x:
        Wiener_Temp.append('RZ')
    if 'Dce'in x:
        Wiener_Temp.append('R0')
    if 'DCe' in x:
        Wiener_Temp.append('R1')
    if 'dcedce' in x:
        Wiener_Temp.append('r')
    FC_Counter = FC_Counter + 2
    FC_Counter2 = FC_Counter2 + 2
    print (Wiener_Temp[FC_Counter] + Wiener_Temp[FC_Counter2])
    Wiener_Group.append(Wiener_Temp[FC_Counter] + Wiener_Temp[FC_Counter2]) #Gets list for classification
#print(Wiener_Group) Checkpoint
for x in Wiener_Group: #Gives a score to each genotype based on the orders of classification
    Wiener_Score= 4
    if 'RZRZ' in x:
        Wiener_Score = Wiener_Score - 2
    if 'ryry' in x:
        Wiener_Score = Wiener_Score - 2
    if 'R0R0' in x:
        Wiener_Score = Wiener_Score - 1
    if 'rIrI' in x:
        Wiener_Score = Wiener_Score - 1
    if 'rIIrII' in x:
        Wiener_Score = Wiener_Score - 1
    if 'ry' in x:
        Wiener_Score= Wiener_Score - 2
    if 'RZ' in x:
        Wiener_Score = Wiener_Score - 2
    if 'R0' in x:
        Wiener_Score = Wiener_Score - 1
    if 'rI' in x:
        Wiener_Score = Wiener_Score - 1
    if 'rII' in x:
        Wiener_Score = Wiener_Score - 1
    Wiener_Orders.append(Wiener_Score) #Note that the Wiener_Group and Wiener_Orders match in terms of sequence
#print(Wiener_Orders) #Important checkpoint until I'm certain classification is fixed

MaxPos= (Wiener_Orders.index(max(Wiener_Orders))) #Gives the location of the first maxvalue in Wiener_Orders
#print(MaxPos)
FirstNumberOne= Wiener_Group[MaxPos] #Saving it as a variable because I need to use the list and reverse it
for x in Wiener_Orders:
    if x == max(Wiener_Orders) and Wiener_Orders.index(x) != FirstNumberOne: #Still having issues with this formula
        Wiener_Orders.reverse() #Index only picks the first one so this way I can pick one on the other side. Does not function if >3 equivalencies
        EqualScore.append(Wiener_Orders.index(x))
print("The most probable genotype(s) are: ")
print(FirstNumberOne)
#print(EqualScore)
Wiener_Group.reverse()
for x in EqualScore:
    if Wiener_Group[x] != FirstNumberOne and ESChecker != 1 and Rh_Pheno != 'Dce' : #Dce giving errors so putting a temp fix
        ESChecker= ESChecker +1 #Temporary fix for getting duplicates in the EqualScore list
        print (Wiener_Group[x])

