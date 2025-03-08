
n = int(input())
cartas = list(map(int, input().split()))

frequencia = {}
for carta in cartas:
    frequencia[carta] = frequencia.get(carta, 0) + 1
    # 1:2,2:2,3:2

numeros_disponiveis = sorted(frequencia.keys()) # 123
melhor_escada = []

for pico in numeros_disponiveis:
    nums_crescente = [num for num in numeros_disponiveis if num <= pico]
    nums_decrescente = [num for num in numeros_disponiveis if num < pico]
    
    escada_atual = [] #-> 1
    contagem_usada = {} #0,0,0 ->  1,0,0
    
    for num in nums_crescente:
        if num not in contagem_usada:
            contagem_usada[num] = 0
        if contagem_usada[num] < frequencia[num]:
            escada_atual.append(num)
            contagem_usada[num] += 1

    for num in sorted(nums_decrescente, reverse=True):
        if num not in contagem_usada:
            contagem_usada[num] = 0
        if contagem_usada[num] < frequencia[num]:
            escada_atual.append(num)
            contagem_usada[num] += 1
    
    if len(escada_atual) > 1 and escada_atual.index(pico) < len(escada_atual) - 1:
        if len(escada_atual) > len(melhor_escada):
            melhor_escada = escada_atual


if not melhor_escada:
    melhor_escada = sorted(cartas, reverse=True)

print(len(melhor_escada))
print(*melhor_escada)