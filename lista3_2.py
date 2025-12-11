lista_inventario = [
    {"id":101, "modelo":"Notebook i5", "status":"ativo"},
    {"id":102, "modelo":"Desktop i3", "status":"manutenção"},
    {"id":103, "modelo":"Notebook i7", "status":"ativo"},
    {"id":104, "modelo":"Servidor Dell", "status":"ativo"}
]

for inventario in lista_inventario:
    if inventario["status"] == "ativo":
        print(inventario)
