#importando conexão com banco de dados
from conexao import conect
#importação do datetime para trabalhr com data
import datetime
class Hospede:
    #instanciando classe Hospede
    def __init__(self,nome,cpf,rg,telefone,email,senha):
        self.nome=nome
        self.cpf=cpf
        self.rg=rg
        self.telefone=telefone
        self.email=email
        self.senha=senha
    #Método de cadastro de hospedes
    def cadastra(self):
        #Trazendo conexão
        con=conect.conecta()
        #criando cursor
        cursor=con.cursor()
        #criando tupla para fazer um dos tipos de inserts
        tupla=(self.nome,self.cpf,self.rg,self.telefone,self.email,self.senha)
        #validando CPF
        #v=Hospede.valida_cpf(self.cpf)
        #executando query
        cursor.execute('insert into hospede values(default,%s,%s,%s,%s,%s,%s)',(tupla))
        con.commit()
        #linhas afetadas
        row=cursor.rowcount
        #validando cadastro
        if(row>=1):
            print('Cadastrado com sucesso!')
            n=int(input('''
            Deseja voltar?
            1.Sim
            2.Não
            '''))
            
            if(n==1):
                #retorna ao menu principal
                from main import menu
                menu()
            else:
                exit
#    def valida_cpf(cpf):
#        con=conect.conecta()
#        cursor=con.cursor()
#        cursor.execute(f"select*from hospede where cpf='{cpf}'")
#        row=cursor.rowcount
#        if(row<=0):
#            from main import menu
#            menu()
#        else:
#            from main import menu
#            print("CPF já cadastrado")
#            menu()
    #função de listagem para o perfil
    def listar(cod:int):
        #trazendo conexao e cursor
        con=conect.conecta()
        cursor=con.cursor()
        tupla=(cod,)
        #busca por codigo trazido como parâmetro
        cursor.execute('select*from hospede where idhospede=%s;',tupla)
        i=cursor.fetchone()
        row=cursor.rowcount
        if(row>=1):
            #mostrando resultados na tela
            print("="*68,'Usuário',"="*65)
            print('Nome: ',i[1])
            print('CPF: ',i[2])
            print('RG: ',i[3])
            print('Telefone: ',i[4])
            print('E-mail: ',i[5])
            print('-'*141)
            print('Alterado com sucesso!')
            op2=int(input('''
            Deseja voltar?
            1.Sim
            2.Não
            '''))
            if(op2==1):
                #retornando ao menu principal
                from main import menu
                menu()
            else:
                exit
    #método de login do hospede
    def login(cpf,senha):
        #trazendo conexao e cursor
        con=conect.conecta()
        cursor=con.cursor()
        tupla=(cpf,str(senha))
        #verifica login
        cursor.execute('select*from hospede where cpf=%s and senha=%s',(tupla))
        result=cursor.fetchone()
        row=cursor.rowcount
        #valida login
        if(row>=1):
            cod=result[0]
            #retorna o codigo do hospede
            return int(cod)
        else:
            print('Senha Incorreta!')
            from main import menu
            menu()
    #método de alterar dados
    def altera(self,op):
        #trazendo conexao e cursor
        con=conect.conecta()
        cursor=con.cursor()
        tupla=(self.nome,self.cpf,self.rg,self.telefone,self.email,op)
        #script de alteração
        cursor.execute('update hospede set nome=%s, cpf=%s,rg=%s,telefone=%s,email=%s where idhospede=%s',(tupla))
        con.commit()
        row=cursor.rowcount
        #verificação da alteração
        if(row>=1):
            print('Alterado com sucesso!')
            op2=int(input('''
            Deseja voltar?
            1.Sim
            2.Não
            '''))
            if(op2==1):
                from main import menu
                menu()
            else:
                exit
    #método para dar baixa
    def baixa(cod_adm,id_hospede):
        #trazendo conexão e cursor
        con=conect.conecta()
        cursor=con.cursor()
        #query de busca por dados do Hóspede
        cursor.execute(f'''select h.nome,h.cpf,h.telefone,r.valor_total,r.data_entrada,r.data_saida,r.idreserva
        from reserva r,hospede h where hospede_idhospede={id_hospede} and idhospede={id_hospede};''')
        i=cursor.fetchall()
        row=cursor.rowcount
        #from administrador import Administrador
        #val=Administrador.multa(i[0][3],i[0][4],i[0][5],i[0][7])
        if(row>=1):
            #verificando se qual das reservas deseja dar baixa
            print("="*67,'Usuário',"="*65)
            print('Nome: ',i[0][0])
            print('CPF: ',i[0][1])
            print('Telefone: ',i[0][2])
            print('Valor Total: ',i[0][3])
            print('Data de Entrada: ',i[0][4])
            print('Data Saída: ',i[0][5])
            cod_reserva=i[0][6]
            op2=int(input('''
            Deseja dar Baixa?
            1.Sim
            2.Não
            '''))
            #se sim
            if(op2==1):
                #inserção na tabela baixa
                cursor.execute(f"insert into baixa(idbaixa,fk_idreserva_b,fk_administrador) values(default,{cod_reserva},{cod_adm})")
                con.commit()
                n=cursor.rowcount
                if(n>=0):
                    print('Baixa realizada com sucesso!')
                else:
                    print('Algo não deu certo!')
            elif(op2==2):
                #leva para menu do administrador
                from administrador import Administrador
                Administrador.menu_adm(cod_adm)
    #método de reserva
    def reservar(cod):
        #importando datatime
        import datetime
        #importando a classe data
        from ler_data import data
        num=str(input('Número do quarto: '))
        #importando e trazendo a conexao e criando o cursor
        from conexao import conect
        con=conect.conecta()
        cursor=con.cursor()
        cursor.execute(f"select idquarto,custo_quarto from quarto where numero={num}")
        result=cursor.fetchall()
        row=cursor.rowcount
        codigo=0
        valor=0
        #trazendo codigo e valor da diária do quarto
        for i in result:
            codigo=i[0]
            valor=i[1]
        
        #print('cod: ',codigo)
        if(row>=1):
            #buscando data atual
            data_atual = datetime.datetime.now()
            print("Informe os dados do dia da entrada: ")
            #chamando função ler para ser informada pelo usuário 
            data_entrada = data.ler_data()
            print("Informe os dados do dia da saida: ")
            data_saida = data.ler_data()
            #Calculo de quantos dias o hospede vai ficar
            d=data_saida-data_entrada
            dias=d.days
            #calculando total de acordo com a quantidade de dias
            valor=valor*dias
            #cliente informa se vai querer algum serviço
            service=int(input('''
            Deseja algum serviço?
            1.Sim
            2.Não
            '''))
            #se sim
            if(service==1):
                #importando classe Servicos
                from servicos import Servicos
                status=1
                #chamando método solicita_serviço da classe Servicos
                Servicos.solicita_servico(cod,data_atual,data_entrada,data_saida,valor,status,codigo)
            #se não quiser serviço
            elif(service==2):
                #print(cod,'-',data_atual,'-',data_entrada,'-',data_saida,'-',valor,'-',1,'-',codigo)
                tpl1=(cod,data_atual,data_entrada,data_saida,valor,'1',codigo)
                #inserindo reserva no banco
                query='''insert into reserva(idreserva,hospede_idhospede,data_reserva,data_entrada,data_saida,valor_total,status,fk_idquarto) values(default,%s,%s,%s,%s,%s,%s,%s)'''
                cursor.execute(query,tpl1)
                con.commit()
                row=cursor.rowcount
                if(row>=1):
                    print('reservado com sucesso!')
                    op2=int(input('''
                    Deseja voltar?
                    1.Sim
                    2.Não
                    '''))
                    if(op2==1):
                        from main import menu
                        menu()
                    else:
                        exit
                elif(row==0 or row==None):
                    print('Algo de errado não está certo!')
        else:
            print('''Quarto inválido!
            Selecione novamente:
            ''')
            Hospede.reservar(cod)
''' #uma possivel função multa
       def multa(self):
        con=conect.conecta()
        cursor=con.cursor()'''