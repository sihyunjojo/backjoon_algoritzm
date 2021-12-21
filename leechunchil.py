a, b = map(int,input().split())
c = ["SUN","MON","TUE","WE","THU","FRI","SAT"]
d = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = 0
for i in range(0,a-1):
    sum +=d[i]
    
print(c[(sum+b)%7])