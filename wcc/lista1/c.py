n = int(input())
c = 0

for i in range(n):
    lista = list(map(int, input().split()))
    if lista.count(1) > 1:
        c += 1

print(c)