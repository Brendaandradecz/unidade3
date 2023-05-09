codigos = []
vendedores = {}

op = 9999

while (op != 0):
    print('\n--------MENU----------\n')
    print('1 - Fazer cadastro')
    print('2 - Fazer login')
    print('0 - Sair')

    op = int(input('Digite o numero correspondente à opção desejada: '))

    if (op == 1):
        usuario_valido = False
        while usuario_valido == False:
            usuario = input('Digite seu usuario: ')
            for user in vendedores.keys():
                if user == usuario:
                    print('Esse usuario já está cadastrado. Tente novamente.')
                    break
            else:
                usuario_valido = True
                senha = input('Digite sua senha: ')
                nome = input('Digite seu nome completo: ')

                cpf_valido = False

                while cpf_valido == False:
                    cpf = (input('Digite seu cpf: '))
                    if len(cpf) == 11:
                        cpf_valido = True
                        if cpf_valido:
                            print('CPF válido')
                    else:
                        print('CPF inválido, Tente novamente')

                tel = int(input('Digite seu telefone: '))
                email = input('Digite seu email: ')
                vendedores[usuario] = [senha, nome, cpf, tel, email, []]
                print('Cadastro Realizado Com Sucesso')
                break


    elif (op == 2):
        usuario = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')

        sistema = False

        for user in vendedores:
            if (user == usuario):
                senha1 = vendedores[usuario][0]
                if (senha1 == senha):
                    sistema = True
                    print(f'Bem-vindo(a), {vendedores[usuario][1]}!')

                    op2 = 99999
                    while (op2 != 0):
                        print('\n--------LOGADO----------\n')
                        print('1 - Cadastrar novo produto para venda')
                        print('2 - Buscar produtos cadastrados')
                        print('3 - Remover produtos cadastrados')
                        print('4 - Atualizar produtos cadastrados')
                        print('5 - Atualizar senha')
                        print('0- Sair')

                        op2 = int(input('Digite o numero correspondente à opção desejada: '))

                        if (op2 == 1):
                            produtos = {}
                            codigo_valido = False

                            while codigo_valido == False:
                                codigo = (input('Digite o código do produto: '))
                                for produto in vendedores[usuario][5]:
                                    if produto['codigo'] == codigo:
                                        print('Já existe um produto com esse código. Por favor, tente novamente.')
                                        break
                                else:
                                    codigo_valido = True

                            nome = input('Digite o nome do produto: ')
                            preco = float(input('Digite o preço do produto: '))
                            quantidade = int(input('Digite a quantidade em estoque: '))
                            vendedores[usuario][5].append({'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade})
                            codigos.append(codigo)
                            print('Produto cadastrado com sucesso!')


                        elif (op2 == 2):
                            print('\n--------BUSCAR PRODUTO CADASTRADO---------\n')
                            nome_produto = input('Digite o nome do produto: ')

                            achados = False

                            for produto in vendedores[usuario][5]:
                                if produto['nome'].find(nome_produto) != -1:
                                    print('CODIGO - NOME - PREÇO - QUANTIDADE')
                                    print(f"{produto['codigo']} - {produto['nome']} - {produto['preco']} - {produto['quantidade']}")
                                    achados = True

                            if achados == False:
                                print('Produto não encontrado.')


                        elif (op2 == 3):
                            print('\n------------Produtos Cadastrados------------\n')
                            print('CODIGO - NOME - PREÇO - QUANTIDADE ')
                            for produto in vendedores[usuario][5]:
                                print(f"{produto['codigo']} - {produto['nome']} - {produto['preco']} - {produto['quantidade']}")

                            codigo_produto = input('digite o codigo do produto que deseja remover: ')
                            produtos_vendedor = vendedores[usuario][5]
                            indice_produto = -1

                            for i in range(len(produtos_vendedor)):
                                if produtos_vendedor[i]['codigo'] == codigo_produto:
                                    indice_produto = i
                                    break

                            if indice_produto == -1:
                                print('Produto não encontrado.')
                            else:
                                vendedores[usuario][5].remove(produtos_vendedor[indice_produto])
                                print('Produto removido com sucesso!')


                        elif (op2 == 4):
                            print('\n------------Produtos Cadastrados------------\n')
                            print('CODIGO - NOME - PREÇO - QUANTIDADE')
                            for produto in vendedores[usuario][5]:
                                print(f"{produto['codigo']} - {produto['nome']} - {produto['preco']} - {produto['quantidade']}")

                            codigo_produto = input('digite o codigo do produto que deseja atualizar: ')
                            produtos_vendedor = vendedores[usuario][5]
                            indice_produto = -1

                            for i in range(len(produtos_vendedor)):
                                if produtos_vendedor[i]['codigo'] == codigo_produto:
                                    indice_produto = i
                                break

                            if indice_produto == -1:
                                print('Produto não encontrado.')


                            else:
                                novo_nome = input('Digite o novo nome do produto ou pressione ENTER para manter o mesmo: ')
                                if novo_nome != "":
                                    produtos_vendedor[indice_produto]['nome'] = novo_nome

                                novo_preco = input('Digite o novo preco do produto ou pressione ENTER para manter o mesmo: ')
                                if novo_preco != "":
                                    produtos_vendedor[indice_produto]['preco'] = float(novo_preco)

                                nova_quantidade = input('Digite a nova quantidade do produto ou pressione ENTER para manter a mesma: ')
                                if nova_quantidade != "":
                                    produtos_vendedor[indice_produto]['quantidade'] = int(nova_quantidade)
                                print('Produto atualizado com sucesso!')


                        elif (op2 == 5):
                            nova_senha = input('digite a nova senha: ')
                            vendedores[usuario][0] = nova_senha
                            print('Senha atualizada com sucesso!')

                        elif (op2 != 0):
                            print('Seleçao invalida')

                        else:
                            print('-------DESLOGADO--------')

                else:
                    print('usuario e/ou senha incorreto(s)')

    elif (op != 0):
        print('Seleçao invalida')

    else:
        print('Programa Finalizado')