looplist=["Mango","banana","Jackfruit","Lychee","palm"]

for i in looplist:     #print all the item
     print(i)
     
#Use the range() and len() functions to create a suitable iterable
print("\n")
    
for i in range(0,len(looplist)):  #all the item will print
    print(looplist[i])  
    
print("\n")   
    
for i in (looplist[1:4]):      #banana,jackfruil,Lychee will print index 1 to 3
    print(i)
print("\n")    
for i in range(0,3):           #banana,jackfruit will print index 0 to 2
    print(looplist[i])