arr = map(int,input().split())

intervals = list(arr).copy()

s_intervals = sorted(intervals)
r_intervals = sorted(intervals,reverse=True)

if intervals == s_intervals:
    print("ascending")
elif intervals == r_intervals:
    print("descending")
else:
    print("mixed")