chamado = {
    "equipamento": "Servidor Principal",
    "tempo_parado_horas": 5,
    "setor": "Financeiro",
    "status": "aberto"
}

equip = chamado["equipamento"]
tempo = chamado["tempo_parado_horas"]
setor = chamado["setor"]

if equip == "Servidor Principal" or tempo > 4:
    prioridade = "P1 - Crítica"
elif setor == "Financeiro" and tempo > 1:
    prioridade = "P2 - Alta"
else:
    prioridade = "P3 - Normal"
print(f"Equipamento: {equip} | Prioridade definida: {prioridade}")