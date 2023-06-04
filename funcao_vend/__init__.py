
def validar_usuario(vendedores):
   usuario_valido = False
   while usuario_valido == False:
       usuario = input('Digite seu usuario: ')
       for user in vendedores.keys():
           if user == usuario:
               print('\nEsse usuario já está cadastrado. Tente novamente.\n')
               break
       else:
           usuario_valido = True
   return usuario

def validar_cpf():
   cpf_valido = False
   while cpf_valido == False:
       cpf = (input('Digite seu cpf: '))
       if len(cpf) == 11:
           cpf_valido = True
           if cpf_valido:
               print('CPF válido')
       else:
           print('CPF inválido, Tente novamente')
   return cpf

def validar_senha():
    senha_valida = False
    while senha_valida == False:
        senha = input('Digite sua senha: ')
        if (len(senha) < 6):
            print('Senha invalida\nÉ necessário que a senha possua pelo menos 6 caracteres, tente novamente!')
        else:
            senha_valida = True
    return senha

def validar_email():
    email_valido = False
    while email_valido == False:
        email = input('Digite seu email: ')
        if '@' and '.com' in email:
            email_valido = True
        if email_valido:
            print('Email valido')
        else:
            print('Email invalido, tente novamente')

def grafico(vendedores):
    data = {}
    for vendedor, dados_vendedor in vendedores.items():
        produtos = dados_vendedor[-1]
        for produto in produtos:
            nome = produto['nome']
            quantidade = produto['quantidade']
            if nome in data:
                data[nome] += quantidade
            else:
                data[nome] = quantidade

    # Criando o gráfico de barras
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # Criando o gráfico de barras
    plt.bar(courses, values, color='maroon', width=0.4)

    plt.xlabel("Produtos")
    plt.ylabel("Quantidade")
    plt.title("Sertao Livre")
    plt.show()