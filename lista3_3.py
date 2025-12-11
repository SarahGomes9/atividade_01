pontuacoes = [5,9,3,10,2,7,8]
criticas_encontradas = 0

for pontuacoes in range(11):
    if pontuacoes >=8:
        criticas_encontradas += 1
print (f"total de máquinas em Situação Crítica (>=8): {criticas_encontradas}")
