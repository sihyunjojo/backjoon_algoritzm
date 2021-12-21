num = int(input())

while(num==1):
    if (num % 3 == 0):
        num = num/3
        break
    if (num % 2 == 0):
        num = num/2
        break
    if (num != 1):
        num = num-1
        
#dp문제
 