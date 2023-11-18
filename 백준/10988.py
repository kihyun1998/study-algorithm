s = input()
isPrint = False

for i in range(1,len(s)//2 + 1):
    if s[i-1] != s[-i]:
        print(0)
        isPrint=True
        break

if not isPrint:
    print(1)