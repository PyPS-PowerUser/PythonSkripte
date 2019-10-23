getSubnet = int(input())
#howManyTimes = int(getSubnet/8+1)

#print (howManyTimes)
text = str()

#for i in range(howManyTimes):
addIt = int()
for b in range(getSubnet):
    print(b)
    subnetList = [128,64,32,16,8,4,2,1]
    addIt += int(subnetList[b])
    print(addIt)
text += str(addIt + ".")

print(text)


#if getSubnet > 24:
#    print (addIt/3 + "." + add)
