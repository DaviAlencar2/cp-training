n = int(input()) 
cartas = list(map(int, input().split()))

sereja = 0
dima = 0
turno_sereja = True
inicio = 0
fim = n - 1

for i in range(n):
    if cartas[inicio] > cartas[fim]:   
        escolha = cartas[inicio]
        inicio += 1 
    else:
        escolha = cartas[fim]
        fim -= 1  
    
    if turno_sereja:
        sereja += escolha
    else:
        dima += escolha
    
    turno_sereja = not turno_sereja 

print(sereja, dima)
