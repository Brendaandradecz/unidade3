def buscar_produtos(vendedores):
    encontrado = False
    produtos_encontrados = []
    print('\n--------BUSCAR PRODUTO---------\n')
    nome_produto = input('Digite o nome do produto: ')
    for vendedor, produtos_vendedor in vendedores.items():
        for produto in produtos_vendedor[5]:
            #if (produto['quantidade'] >= 1 ):
                if produto['quantidade'] >= 1 and (nome_produto.lower() in produto['nome'].lower() or nome_produto.lower() in produto['descricao'].lower()):
                    print(f'Produto encontrado: Vendedor: {vendedor} | Nome: {produto["nome"]} | Código: {produto["codigo"]} | Preço: R${produto["preco"]} | Quantidade: {produto["quantidade"]} | Descrição: {produto["descricao"]}')
                    produtos_encontrados.append(produto)
                    encontrado = True

    if not encontrado:
        print('Produto não encontrado')

    return produtos_encontrados


def realizar_compra(produtos_encontrados):
    if produtos_encontrados:
        quero = input('Voce deseja comprar algum dos produtos encontrados?\n s - Sim\n n - Não\n')
        while (quero.lower() == 's'):
            codigo_produto = input('Digite o código do produto que deseja comprar: ')
            for p in produtos_encontrados:
                if codigo_produto == p['codigo']:
                    if p['quantidade'] > 0:
                        print('Produto disponível. Efetuando compra...')
                        p['quantidade'] -= 1
                        print('Compra realizada com sucesso!')
                        break
                    else:
                        print('Produto indisponível.')
            else:
                print('Produto não encontrado.')

            quero = input('Continuar comprando?\n s - Sim\n n - Não\n')

def comprar_indice_produto(vendedores):
    op4 = input('Você deseja buscar e/ou comprar algum produto?\n s - Sim\n n - Não\n')
    while op4.lower() == 's':
        produtos_encontrados = buscar_produtos(vendedores)
        if produtos_encontrados:
            realizar_compra(produtos_encontrados)

        op4 = input('Você deseja buscar e/ou comprar mais algum produto?\n s - Sim\n n - Não\n')

    return op4
