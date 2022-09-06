#importação da classe Hospede
from fileinput import hook_encoded
from hospede import Hospede
#declarando variável global cod do tipo insteiro
cod:int
#criação da função menu
def menu():
    #pedir ao usuário que informe o número da opção desejada
    opcao=int(input('''
Digite o número da opção desejada:
1.Login
2.Cadastro de Hospede
3.Area do administrador
'''))
#Caso a opção seja 1 será feito o login por CPF e senha do hospede
    if(opcao==1):
        from hospede import Hospede
        print("="*68,"Login","="*66)
        l=str(input('CPF: '))
        s=str(input('Senha: '))
        print('='*141)
        #chamando a função login da classe Hospede
        cod=Hospede.login(l,s)
        #Verificando se o retorno é nulo para validar o login
        if(cod!=None):
            #usuário digita p que deseja fazer
            num=int(input('''Informe o número da opção desejada: 
            1.Perfil
            2.Aletrar dados
            3.Reservar quarto
            4.logout
            '''))
            #mostrar o perfil
            if(num==1):
                Hospede.listar(cod)
            #alterar os dados, para isso informa dados que irão substituir os do banco
            elif(num==2):
                print('Preencha os dados')
                nome=str(input('Nome: '))
                cpf=str(input('CPF(com pontos e digito): '))
                rg=str(input('RG(com pontos e digito): '))
                telefone=str(input('Telefone: '))
                email=str(input('E-mail: '))
                #Após receber os dados, instanciamos a classe Hospede
                hospede=Hospede(nome,cpf,rg,telefone,email,0)
                #chamando método de alterar
                hospede.altera(cod)
                #reservar algum quarto
            #reserva de quarto
            elif(num==3):
                #envio do id do hospede que veio da função login
                Hospede.reservar(cod)
    #Área para o cliente se cadastrar
    elif(opcao==2):
        from hospede import Hospede
        print('Preencha os dados')
        nome=str(input('Nome: '))
        cpf=str(input('CPF(com pontos e digito): '))
        #Hospede.valida_cpf(cpf)
        rg=str(input('RG(com pontos e digito): '))
        telefone=str(input('Telefone: '))
        email=str(input('E-mail: '))
        senha=str(input('Senha: '))
        #Após receber os dados, instanciamos a classe Hospede
        hospede=Hospede(nome,cpf,rg,telefone,email,senha)
        #chamando método de cadastro
        hospede.cadastra()

    #Área do administrador
    elif(opcao==3):
        from administrador import Administrador
        #será feito o login do administrador pelo método login da classe Administrador
        cod=Administrador.login_adm()
        #Verificando se o retorno é nulo para validar o login
        if(cod!=None):
            #chamando menu do administrador após a validação do login
            Administrador.menu_adm(cod)
    else:
        #caso não seja nenhuma das opções direcionará a função de menu inicial
        menu()
menu()