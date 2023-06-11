import matplotlib.pyplot as plt
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

def validar_nome():
    nome_valido = False
    while not nome_valido:
        nome = input('Digite seu nome: ')
        if isinstance(nome, str) and len(nome) >= 3:
            nome_valido = True
            print('Nome válido')
        else:
            print('Nome inválido, tente novamente')

    return nome

def validar_senha():
    senha_valida = False
    while senha_valida == False:
        senha = input('Digite sua senha: ')
        if (len(senha) < 6):
            print('Senha invalida\nÉ necessário que a senha possua pelo menos 6 caracteres, tente novamente!')
        else:
            senha_valida = True
    return senha

def validar_telefone():
    telefone_valido = False
    while not telefone_valido:
        telefone = input('Digite seu telefone: ')
        if telefone.isdigit() and len(telefone) >= 8:
            telefone_valido = True
            print('Telefone válido')
        else:
            print('Telefone inválido, tente novamente')

    return telefone

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
    return email

def gerar_grafico(vendedores, usuario):
    nomes = []
    quantidade = []

    for produto in vendedores[usuario][5]:
        nomes.append(produto['nome'])
        quantidade.append(produto['quantidade'])

    fig = plt.figure(figsize=(10, 5))
    plt.bar(nomes, quantidade, color='maroon', width=0.4)
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade')
    plt.title('Grafico Produtos')
    plt.show()

def salvar_relatorio(vendedores, usuario):
   nome_arquivo = f"relatorio_{usuario}.txt"

   with open(nome_arquivo, "w") as arquivo:
       arquivo.write(f"Relatório de produtos do vendedor {vendedores[usuario][1]}:\n\n")

       for produto in vendedores[usuario][5]:
           arquivo.write(f"Nome: {produto['nome']}\n")
           arquivo.write(f"Código: {produto['codigo']}\n")
           arquivo.write(f"Preço: R${produto['preco']:.2f}\n")
           arquivo.write(f"Quantidade: {produto['quantidade']}\n")
           arquivo.write(f"Descrição: {produto['descricao']}\n\n")

   print(f"Relatório salvo com sucesso no arquivo {nome_arquivo}")
