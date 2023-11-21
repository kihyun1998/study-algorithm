L = int(input())

arr = list(input())

r=31
M=1234567891
hashSum=0

for i,v in enumerate(arr):
    hashSum += (ord(v)-96) * (r**(i))

print(hashSum%M)