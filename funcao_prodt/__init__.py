def validar_codigo():
    codigo_valido = False
    while codigo_valido == False:
        codigo = input('Digite o código do produto: ')
        codigo_repetido = False
        for cod in codigos:
            if cod == codigo:
                print('Já existe um produto com esse código. Por favor, tente novamente.')
                codigo_repetido = True
                break
        if codigo_repetido == False:
            codigo_valido = True
            codigos.append(codigo)
    return codigo

def buscarProduto(nome_produto):
    achados = False
    for produto in vendedores[usuario][5]:
        if produto['nome'].find(nome_produto) != -1:
            print('CODIGO - NOME - PREÇO - QUANTIDADE - DESCRIÇÃO')
            print(f"{produto['codigo']} - {produto['nome']} - {produto['preco']} - {produto['quantidade']} - {produto['descricao']} ")
            achados = True
    if achados == False:
        print('Produto não encontrado.')

def listarProduto(vendedores, usuario):
    print('\n------------Produtos Cadastrados------------\n')
    print('CODIGO - NOME - PREÇO - QUANTIDADE - DESCRIÇÃO')
    for produto in vendedores[usuario][5]:
        print(f"{produto['codigo']} - {produto['nome']} - {produto['preco']} - {produto['quantidade']} - {produto['descricao']}")

def buscar_indice_produto(produtos_vendedor, codigo_produto):
    indice_produto = -1

    for i in range(len(produtos_vendedor)):
        if produtos_vendedor[i]['codigo'] == codigo_produto:
            indice_produto = i
            return indice_produto
    return indice_produto

def atualizar_produto(produtos_vendedor, indice_produto, novo_nome, novo_preco, nova_quantidade, nova_descricao):
    if novo_nome != "":
        produtos_vendedor[indice_produto]['nome'] = novo_nome
    if novo_preco != "":
        produtos_vendedor[indice_produto]['preco'] = float(novo_preco)
    if nova_quantidade != "":
        produtos_vendedor[indice_produto]['quantidade'] = int(nova_quantidade)
    if nova_descricao != "":
        produtos_vendedor[indice_produto]['descricao'] = nova_descricao

    print('Produto atualizado com sucesso!')
