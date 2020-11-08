# python3
x, y, z  = map(int,input().split())
lst = [0]
i = 0
flag = 0

if z == 0:
    print(i)
    flag = 1
    
if  flag == 0 and ((y > x and z > x) or (x == 0 and z!=0) or (y == x and z != x )):
    print("-1")
    flag = 1

while flag == 0 and (lst[-1] <= z or lst[-2] <= z):
#    print(lst)
    first = lst[-1] + x
    lst.append(first)
    i+=1
    if lst[-1] == z:
        print(i)
        flag = 1
        break
    second = lst[-1] - y
    lst.append(second)
    i+=1
    if lst[-1] == z:
        print(i)
        flag = 1
        break
if flag == 0:
    print("-1")

#print(lst)