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