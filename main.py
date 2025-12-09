login_salvo = "admin_ti"
senha_salva = "Sistema@123"
login_digitado = input("Digite o seu login: " )
senha_digitada = input("Digite sua senha: " )


if login_digitado == login_salvo and senha_digitada == senha_salva:
    print("Acesso concedido. Bem-vindo ao painel de controle.")
elif login_digitado == "guest" or senha_digitada == "123456":
    print("Acesso Negado: Credenciais de baixo risco ou padrão de segurança.")
else:
    print("Erro de acesso: Login ou senha inválido.")