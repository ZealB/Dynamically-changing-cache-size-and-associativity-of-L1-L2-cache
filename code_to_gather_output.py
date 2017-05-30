#This script copies all data frm each text file into a single text file, 
#thus bringing all the 80*4 instances together in a single text file alldata.txt in csv format

#name of file you want to read from
source = open('C:/Users/zeal/Desktop/SMTSIM/results/applu0', 'r') 

#name of file you want to write to
new = open('C:/Users/zeal/Desktop/IPC_applu0.txt', 'w')  

while True:
    charactersrc=str(source.readline()) 
    if characterdsrc[0:1] == "N":
       new.write(charactersrc[89:])
    
        

source	.close()
dest.close()
new.close()		

