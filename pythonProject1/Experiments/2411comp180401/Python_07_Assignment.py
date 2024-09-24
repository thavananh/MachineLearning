print('Nhap 3 tham so: ', end='')
T, P, C = input().split()
T = int(T)
P = int(P)
C = int(C)
print(T, P, C)
while T < 1 or T > 2:
    print('T: ', end='')
    T = input()

while P < 1:
    print('P: ', end='')
    P = input()

while C > 109 or C < 0:
    print('C: ', end='')
    C = input()

output = 0
if T == 1:
    output = P
else:
    output = P / 2
    if P % 2 != 0:
        output += 1

print(int(output * C))