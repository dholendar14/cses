sum = 0
num = int(input())
l = input().split()
for i in l:
    sum = sum + int(i)
total = num*(num+1)/2 - sum
print(int(total))


