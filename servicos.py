#importando a conexao
from conexao import conect
class Servicos:
    #contrutor da classe
    def __init__(self,nome,custo):
        self.nome=nome
        self.custo=custo
    #método de cadastro
    def cadastrar(self):
        #trazendo a conexao e o cursor
        con=conect.conecta()
        cursor=con.cursor()
        #verifica conexao
        if con:
            tupla=(self.nome,self.custo)
            #inserindo os dados no banco
            cursor.execute("insert into servicos(idservicos,nome,custo) values(default,%s, %s)",(tupla))
            con.commit()
        row=cursor.rowcount
        #Verifica se a inserção foi feita
        if(row>=0):
            print('Inserido com sucesso!')
            voltar=int(input('''Deseja voltar?
            1.Sim
            2.Não
            '''))
            if(voltar==1):
                from main import menu
                menu()
        else:
            print('Serviço não inserido!')
    #método de listar os serviços disponíveis
    def listar():
        #trazendo conexão e cursor
        con=conect.conecta()
        cursor=con.cursor()
        #query de consulta
        cursor.execute('''Select*from servicos''')
        result=cursor.fetchall()
        row=cursor.rowcount
        #Verifica se existe algum serviço
        if(row>=1):
            #mostra os serviços
            print("="*66,"SERVIÇOS","="*65)
            for i in result:
                c=i[0]
                custo=i[2]
                print('Código: ',c)
                print('Seviço: ',i[1])
                print('Custo: ',custo)
                print('='*141)
    #método de solicitar serviço
    def solicita_servico(cod,data_atual,data_entrada,data_saida,valor,status,codigo):
        #listando serviços
        Servicos.listar()
        #trazendo conexão e cursor
        con=conect.conecta()
        cursor=con.cursor()
        #informa o código do serviço
        cod2=int(input('Digite o Código de serviço desejado: '))
        #verifica existencia do codigo digitado
        cursor.execute(f"select * from servicos where idservicos={cod2}")
        shop=cursor.fetchall()
        line=cursor.rowcount
        print('Linhas afetadas: ',line)
        #line*=(-1)
        if(line>=1):
            for i in shop:
                #trazendo custo do seviço e codigo do serviço
                custo=i[0]
                cod2=i[2]
                #somando custo com o valor total da estadia
                valor=valor+custo
                #insere no banco os dados da reserva
                cursor.execute(f'''insert into reserva(idreserva,hospede_idhospede,data_reserva,data_entrada,data_saida,valor_total,status,fk_idquarto) values(default,{cod},'{data_atual}','{data_entrada}','{data_saida}',{valor},{status},{codigo});''')
                con.commit()
                row=cursor.rowcount
                #insere no banco os dados da solicitação do serviço
                cursor.execute(f'''insert into solicita(idsolicita,fk_idservicos,fk_idhospede) values(default,{cod2},{codigo})''')
                con.commit()
                row2=cursor.rowcount
                #verifica se foi inserido
                if(row>=1 and row2>=1):
                    print('Inserido com sucesso!')
                    print('reservado com sucesso!')
                    print('Valor Total: ',valor)
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
        else:
            print('Nenhum dado encontrado!')