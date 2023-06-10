import funcao_cliente
import funcao_vend
import funcao_prodt
import usarchatgpt

vendedores = {'aa': ['aa', 'aa', '11111111111', 111, 'aa', [{'nome': 'bolsa', 'codigo': '1', 'preco': 12.0, 'quantidade': 12, 'descricao': 'adfffff'}, {'nome': 'carro', 'codigo': '2', 'preco': 222222.0, 'quantidade': 1, 'descricao': 'dfd'}]],
              'ab': ['ab', 'ab', '11111111114', 114, 'ab', [{'nome': 'iphone', 'codigo': '4', 'preco': 15.0, 'quantidade': 1, 'descricao': 'adddddd'}, {'nome': 'ded', 'codigo': '5', 'preco': 22.0, 'quantidade': 13, 'descricao': 'fffd'}]]}
codigos = ['1', '2', '4', '5']
clientes = {'aa': {'senha': '123123', 'nome': 'sasa', 'cpf': '11122233344', 'tel': 12231123, 'email': 'brenda@gmail.com', 'compras': [{'nome': 'bolsa', 'codigo': '1', 'preco': 12.0, 'quantidade': 5, 'descricao': 'adfffff'}, {'nome': 'carro', 'codigo': '2', 'preco': 222222.0, 'quantidade': 1, 'descricao': 'dfd'}, {'nome': 'bolsa', 'codigo': '1', 'preco': 12.0, 'quantidade': 2, 'descricao': 'adfffff'}]}}

menu = 9999
while (menu != 0):
    print('\nSEJA BEM-VINDO(A) AO SERTÃO LIVRE!\n1 - MENU Vendedor\n2 - MENU Cliente\n0 - Sair')
    menu = int(input('Escolha a opção referente ao MENU que você deseja acessar: '))

    if (menu == 1):
        op = 9999
        while (op != 0):
             print('\nSEJA BEM-VINDO(A) AO MENU VENDEDOR\n\n1 - Fazer  cadastro como vendedor\n2 - Fazer login como vendedor \n0 - Sair\n')
             op = int(input('Digite o numero correspondente à opção desejada: '))

             if (op == 1):
                 usuario = funcao_vend.validar_usuario(vendedores)
                 cpf = funcao_vend.validar_cpf()
                 senha = funcao_vend.validar_senha()
                 nome = funcao_vend.validar_nome()
                 tel = funcao_vend.validar_telefone()
                 email = funcao_vend.validar_email()
                 vendedores[usuario] = [senha, nome, cpf, tel, email, []]
                 print('\nCadastro Realizado com Sucesso!\n')

             elif (op == 2):
                 sistema = False
                 while sistema == False:
                     usuario = input('Digite seu usuario: ')
                     senha = input('Digite sua senha: ')
                     if usuario in vendedores:
                         if vendedores[usuario][0] == senha:
                             sistema = True
                             print(f'\nBem-vindo(a), {vendedores[usuario][1]}!')
                             op2 = 99999

                             while (op2 != 0):
                                 print('\n--------LOGADO----------\n\n1 - Cadastrar novo produto para venda\n''2 - Buscar produtos cadastrados\n''3 - Remover produtos cadastrados\n''4 - Atualizar produtos cadastrados\n5 - Atualizar senha\n6 - ... 7 - ...0- Sair\n')
                                 op2 = int(input('Digite o numero correspondente à opção desejada: '))

                                 if (op2 == 1):
                                     produtos = {}
                                     codigo = funcao_prodt.validar_codigo()

                                     nome = input('Digite o nome do produto: ')
                                     preco = float(input('Digite o preço do produto: '))
                                     quantidade = int(input('Digite a quantidade em estoque: '))
                                     descricao = input('Digite a descrição do produto: ')
                                     vendedores[usuario][5].append({'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade, 'descricao': descricao})
                                     codigos.append(codigo)
                                     print('Produto cadastrado com sucesso!')

                                 elif (op2 == 2):
                                     print('\n--------BUSCAR PRODUTO CADASTRADO---------\n')
                                     nome_produto = input('Digite o nome do produto: ')
                                     funcao_prodt.buscarProduto(nome_produto)

                                 elif (op2 == 3):
                                     produtos_vendedor = vendedores[usuario][5]
                                     funcao_prodt.listarProduto(vendedores, usuario)
                                     codigo_produto = input('digite o codigo do produto que deseja remover: ')
                                     indice_produto = funcao_prodt.buscar_indice_produto(produtos_vendedor, codigo_produto)

                                     if indice_produto == -1:
                                         print('Produto não encontrado.')
                                     else:
                                         vendedores[usuario][5].pop(indice_produto)
                                         codigos.remove(codigo_produto)
                                         print('Produto removido com sucesso!')

                                 elif (op2 == 4):
                                     produtos_vendedor = vendedores[usuario][5]
                                     funcao_prodt.listarProduto(vendedores, usuario)

                                     codigo_produto = input('Digite o código do produto que deseja atualizar: ')
                                     indice_produto = funcao_prodt.buscar_indice_produto(produtos_vendedor, codigo_produto)

                                     if indice_produto == -1:
                                         print('Produto não encontrado.')
                                     else:
                                         novo_nome = input('Digite o novo nome do produto ou pressione ENTER para manter o mesmo: ')
                                         novo_preco = input('Digite o novo preço do produto ou pressione ENTER para manter o mesmo: ')
                                         nova_quantidade = input('Digite a nova quantidade do produto ou pressione ENTER para manter a mesma: ')
                                         nova_descricao = input('Digite a nova descrição do produto ou pressione ENTER para manter a mesma: ')
                                         funcao_prodt.atualizar_produto(produtos_vendedor, indice_produto, novo_nome, novo_preco, nova_quantidade, nova_descricao)

                                 elif (op2 == 5):
                                     nova_senha = funcao_vend.validar_senha()
                                     vendedores[usuario][0] = nova_senha
                                     print('Senha atualizada com sucesso!')

                                 elif (op2 == 6):
                                     funcao_vend.gerar_grafico(vendedores, usuario)

                                 elif (op2 != 0):
                                     print('Seleçao invalida')
                                     print(vendedores)
                                     print(clientes)
                                     print(codigos)
                                 else:
                                     print('-------DESLOGADO--------')
                         else:
                             print('Senha Incorreta')
                     else:
                         print('Usuário não encontrado')

             elif(op != 0):
                 print('Seleçao invalida')
             else:
                 print('\nVocê saiu do MENU Vendedor')

    elif (menu == 2):
             op3 = 999
             while (op3 != 0):
                 print('\nSEJA BEM-VINDO(A) AO MENU CLIENTE!\n\n1 - Fazer cadastro como cliente\n2 - Fazer login como cliente\n0 - Sair')
                 op3 = int(input('Digite o numero correspondente à opção desejada: '))

                 if (op3 == 1):
                     cliente = funcao_vend.validar_usuario(clientes)
                     cpf_cli = funcao_vend.validar_cpf()
                     senha_cli = funcao_vend.validar_senha()
                     nome_cli = funcao_vend.validar_nome()
                     tel_cli = funcao_vend.validar_telefone()
                     email_cli = funcao_vend.validar_email()
                     clientes[cliente] = {'senha': senha_cli, 'nome': nome_cli, 'cpf': cpf_cli, 'tel': tel_cli, 'email': email_cli, 'compras': []}
                     print('Cadastro Realizado Com Sucesso')

                 elif(op3 == 2):
                     sistema = False
                     while sistema == False:
                         cliente = input('Digite seu usuario: ')
                         senha = input('Digite sua senha: ')

                         if cliente in clientes:
                             if clientes[cliente]['senha'] == senha:
                                 sistema = True
                                 print(f'\nBem-vindo(a), {clientes[cliente]["nome"]}!')

                                 opcli = 999
                                 while (opcli != 0):
                                     print('\n --------LOGADO---------\n\n1 - Fazer busca/compra\n2 - Listar compras anteriores\n3 - Consultar descrição de produto\n0 - sair ')
                                     opcli = int(input('Digite o numero correspondente à opção desejada: '))

                                     if (opcli == 1):
                                         op4 = funcao_cliente.comprar_indice_produto(vendedores, clientes, cliente)

                                     elif (opcli == 2):
                                         funcao_cliente.listar_compras_realizadas(clientes, cliente)

                                     elif (opcli == 3):
                                         nome_produto = input('Digite o nome do produto que deseja consultar: ')
                                         produto_encontrado = False

                                         for vendedor, dados_vendedor in vendedores.items():
                                             produtos = dados_vendedor[-1]

                                             for produto in produtos:
                                                 if produto["nome"] == nome_produto:
                                                     produto_encontrado = True
                                                     descricao = usarchatgpt.consultarchatgpt(produto["nome"])
                                                     print(f"A descrição do produto {nome_produto} é: {descricao}")

                                         if not produto_encontrado:
                                             print("Produto não encontrado.")

                                     elif(opcli != 0):
                                         print('Seleção Invalida')
                                     else:
                                         print('-------DESLOGADO--------')
                             else:
                                 print('Senha Incorreta')
                         else:
                             print('Usuário não encontrado')

                 elif(op3 != 0):
                     print('Seleção Invalida')
                     print(clientes)
                     print(vendedores)
                 else:
                     print('\nVocê saiu do MENU cliente')

    elif (menu != 0):
        print('Esta seleçao é invalida')
    else:
        print('Programa Finalizado')