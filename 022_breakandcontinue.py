for i in range(10):
    if i == 5:      # 5 will not print because of continue
        continue
    print(i)

for i in range(10):
    if i == 7:        # here will print 0,1,2,3,4,5,6 and then break
        break
    print(i)
