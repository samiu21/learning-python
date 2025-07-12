#problem 1  swapping two elements in a list

a=[4,5,6,7,33,45]
temp=a[0]
a[0]=a[len(a)-1]
a[len(a)-1]=temp
print(a)

#problem 2  count unique elements in a list

a=[1,2,2,3,3,3,4,5,6]
b=[]
count=0
for i in a:
    if i not in b:
        count+=1
        b.append(i)
print(count)      #total unique elements
print(b)          #list of unique elements

#problem 3  Given al list , extract all elements whose frequency is grteater than k .
# input : Test_list = [4,6,4,3,3,4,3,4,3,8],k=3
# ouptut : [4,3]
test_list=[4,6,4,3,3,4,3,4,3,8]
e=[]

for l in test_list:
    countt=0
    for k in test_list:
        if l == k:
           countt+=1
    if countt>3 and  l not in e:
        e.append(l)

print(e)   

# another way   
test_list2=[4,6,4,3,3,4,3,4,3,8,9]
f=[]
for i in test_list2:
    res=test_list2.count(i)
    if res>3 and i not in f:
        f.append(i)
        
print(f)

 # problem 4 create the following list using list comprehension
 #  [[1,2,3,4],[0,2,3,4],[0,1,3,4],[0,1,2,4],[0,1,2,3]]
 
compre = [[ j for j in range(5) if i!=j]for i in range (5)]
print(compre)