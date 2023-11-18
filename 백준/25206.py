gradeMap = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0
}
gp=0.0
p=0.0

all = [list(input().split()) for _ in range(20)]



for subject in all:
    if subject[2] != 'P':
        p += float(subject[1])
        gp += float(subject[1]) * gradeMap[subject[2]] 

print(gp/p)