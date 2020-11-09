# python3
# python3
n = int(input())
a = list(map(int, input().strip().split()))
max_el = max(a)
#print(max_el)
a_sorted = sorted(a, reverse = True)
flag = 0
if n>2 and a_sorted[0] == a_sorted[2]:
     flag = 1
if (flag == 0):
     for el in a:
          if max_el == el:
               continue
          else:
               print(el, end = " ")
else:
     i = 0
     for el in a:
          if max_el == el:
               i+=1
          if max_el == el and i == 3:
               continue
          else:
               print(el, end = " ")
