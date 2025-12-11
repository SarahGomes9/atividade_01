cargo = "Visitantes"
status_ativo = True

if cargo == "Administrador" and status_ativo == True:
    print("Acesso total ao Sistema.")
elif cargo == "Usuario" and status_ativo == True:
    print("Acesso Limitado: Módulod de Manutenção.")
elif cargo == "Visitantes" and status_ativo == True:
    print("Acesso Somente a Leitura.")
else:
    print("Acesso Negado: Usuario Inativo.")
