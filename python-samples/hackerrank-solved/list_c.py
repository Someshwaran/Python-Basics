x = int(input())
y = int(input())
z = int(input())
n = int(input())
new_list = []
for i in range(x +1):
    for j in range(y +1):
        for k in range(z +1):
            if (i + j + k) != n:
                new_list.append([i,j,k])

for values in new_list:
    print(values)


