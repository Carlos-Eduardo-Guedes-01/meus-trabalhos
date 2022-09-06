#classe Administrador
class Administrador:
    #método construtor do adminstrador
    def __init__(self,nome,cpf,rg,telefone,email,senha):
        self.nome=nome
        self.cpf=cpf
        self.rg=rg
        self.telefone=telefone
        self.email=email
        self.senha=senha
    #método do menu do administrador
    def menu_adm(cod):
        #importação da classe Quarto
        from quarto import Quarto
        #importação da classe Servicos
        from servicos import Servicos
        #exibição/leitura do menu do adminstrador
        opadm=int(input('''
            Informe o numero da opção de administrador desejada
            1.Cadastrar quarto
            2.Alterar dados do quarto
            3.Cadastrar Serviço
            4.Baixa na reserva
            5.Logout
            '''))
        #se a opção for igual a 1, será efetuado cadastro do quarto
        if(opadm==1):
            #leitura dos dados
            tipo=str(input('Informe o tipo do quarto: '))
            numero=int(input('Informe o número do quarto: '))
            custo=int(input('Informe o custo da estadia do quarto: '))
            status=int(input('Informe o status do quarto(1 para disponivel ou 0 para indisponível): '))
            #instanciando a classe quarto
            quarto=Quarto(numero,tipo,custo,status)
            #chamando método de cadastro do quarto no banco
            quarto.cadastro_quarto(cod)        
        #Caso a for igual a 2, será feita a alteração dos dados dos quartos
        elif(opadm==2):
            #chamando a função listar da classe Quarto
            Quarto.listar()
            #pedindo código do quarto a ser alterado
            op=int(input('Digite o código do quarto que deseja alterar: '))
            print('Agora Informe os dados a serem alterados')
            #informando os dados que vão substituir os do banco
            num=int(input('Nº: '))
            tipo=str(input('Tipo: '))
            valor=str(input('Estadia: '))
            status=int(input('Status: '))
            #instanciando a classe Quarto
            quarto=Quarto(num,tipo,valor,status)
            #função para alterar no banco de dados
            quarto.altera(op)
        #Caso a opção seja igual a 3 será cadastrado o novo serviço
        elif(opadm==3):
            #leitura dos dados
            nome=str(input('Informe o nome do serviço: '))
            custo=int(input('Informe o custo para o serviço: '))
            #instanciando classe Servicos
            servico=Servicos(nome,custo)
            #cadastrando no banco de dados
            servico.cadastrar()
        #caso a opção seja igual a 4 será dada baixa em alguma reserva
        elif(opadm==4):
            #importação da classe Hospede
            from hospede import Hospede
            #importação da classe conect
            from conexao import conect
            #chamando método para fazer conexão com banco de dados
            con=conect.conecta()
            #chamando cursor
            cursor=con.cursor()
            #pedindo CPF do cliente para ser dados baixa
            cpf=str(input('Informe o CPF do hospede: '))
            #procurando no banco de dados
            cursor.execute(f"select*from hospede where cpf='{cpf}'")
            #Convertendo resultado da consulta pra algo que o python entenda
            cpf2=cursor.fetchall()
            #trazendo o codigo da reserva
            cd=cpf2[0][0]
            #chamando função de baixa da classe hospede
            Hospede.baixa(cod,cd)
        #caso a opção seja igual a 5 será feito logout
        elif(opadm==5):
            from main import menu
            menu()
    def login_adm():
        from conexao import conect
        cpf=str(input('CPF: '))
        senha=str(input('Senha: '))
        con=conect.conecta()
        cursor=con.cursor()
        tupla=(cpf,str(senha))
        cursor.execute('select*from administrador where cpf=%s and senha=%s',(tupla))
        result=cursor.fetchall()
        row=cursor.rowcount
        if(row>=1):
            cod=result[0][0]
            return int(cod)
        else:
            print('Senha Incorreta!')
            from main import menu
            menu()
'''    def multa(val,data_ini,data_fim,diaria):
        import datetime
        hj=datetime.datetime.now()
        if(data_fim<hj):
            d=data_fim-data_ini
            dhj=hj-data_fim
            mult=dhj.days
            day=d.days
            min_tot=60*(day*24)
            valor_min=(diaria/24)/60
#protótipo de cadastro de adm   
    def cadastra_adm(self):
        from conexao import conect
        con=conect.conecta()
        cursor=con.cursor()
        cursor.execute(f"select*from administrador where cpf={self.cpf}")
        row=cursor.rowcount
        if(row==0):
            cursor.execute(f"insert into administrador(idadm,nome,cpf,rg,telefone,email,senha) values(default,{self.nome},{self.cpf},{self.rg},{self.telefone},{self.email},{self.senha})")
            con.commit()
            r=cursor.rowcount
            if(r>0):
                print('Cadastrado com sucesso!')
                Administrador.menu_adm()
        elif(row>0):
            print('CPF já cadastrado!')'''
    