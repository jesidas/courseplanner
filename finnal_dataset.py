import csv
VocabList = []
f = open("../datasets/CISC499 Dataset/vocab.txt")
line = f.readline()
while line:
    rs = line.replace('\n','')
    rs = rs.replace(' ','_')
    VocabList.append(rs)
    
    line = f.readline()

f.close()
adict = {}
with open("../datasets/CISC499 Dataset/cs_preq.csv") as csvfile1:
    csv_reader = csv.reader(csvfile1)
    birth_header = next(csv_reader)
    adict[birth_header[0].lower()] = birth_header[1].lower()
    for row in csv_reader:
        lower1 = row[0].lower()
        lower2 = row[1].lower()
        
        if row[0] in adict.keys():
            
            adict[row[0]]=adict[lower1]+","+lower2
            
            
        else:
            adict[lower1]=lower2

csvfile1.close()
    
with open("../datasets/CISC499 Dataset/FinalDataset.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["concept","Preconcept","label"])
    for i in VocabList:
        #lower3 = i.lower()
        for j in VocabList:
            #lower4=j.lower()
            
            if i.lower() != j.lower() and i.lower() in adict.keys() and j.lower() in adict[i.lower()]:
                
                writer.writerows([[i,j,1]])
            elif i.lower() != j.lower():
                writer.writerows([[i,j,0]])
        
        
csvfile.close()

