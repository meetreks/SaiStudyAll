#Lets Play with Files - shall we
import os
path = 'C:/'
path1 = 'C:/Analytics Vidhya Machine Learning/JPA_Cloud_AWS_GCP_Matter/sairam.txt'
path2 = 'C:/Analytics Vidhya Machine Learning/JPA_Cloud_AWS_GCP_Matter/sai-file.txt'
entries = os.listdir(path)
#for name in entries:
#    print(name[0])
print(entries[0])
f = open(path1,'r')
for line in f:
    print(line)
f.close()
fr = open(path2,'w')
fr.write("Om Sairam")
fr.close()
### with open in read & write will make the file automatically closed after the block.
##readlines and writelines helps to read all or write ALL at one go
#pickle serealises objects into bytes and deserializes if reverse is required. Let us see some example
import pickle as pk
f1 = open("data.pkl",'wb')
cities = ["ram","sai","sairam","riddhi","ritvik"]
pk.dump(cities,f1)
f1.close()
f2 = open("data.pkl",'rb')
kisi = pk.load(f2)
print(kisi)