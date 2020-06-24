count = 0
count1 = 0
count2 = 0
count3 = 0
st = input()
l = list(st.strip())
for i in l:
    if 'A' == i:
        count = count + 1
    elif 'T' == i:
        count1 = count1 + 1
    elif 'C' == i:
        count2 = count2 + 1
    else:
        count3 = count3 + 1
print(max(count, count1, count2, count3))
