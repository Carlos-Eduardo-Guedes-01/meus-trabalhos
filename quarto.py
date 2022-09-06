#importando conexao
from re import A
from conexao import conect
class Quarto:
    #construtor da classe
    def __init__(self,numero,tipo, custo, status):
        self.numero=numero
        self.tipo=tipo
        self.custo=custo
        self.status=status
    #metodo de cadastro de quarto
    def cadastro_quarto(self,cod):
        #trazendo conexao e criando cursor
        con=conect.conecta()
        cursor=con.cursor()
        tupla=(self.numero,self.tipo,self.status,cod,self.custo)
        #inserindo no banco os dados do quarto
        cursor.execute("insert into quarto values(default,%s,%s,%s,%s,%s)",(tupla))
        con.commit()
        row=cursor.rowcount
        #verifica inserção
        if(row>=0):
            print('Inserido com sucesso!')
            voltar=int(input('''Deseja voltar?
            1.Sim
            2.Não
            '''))
            if(voltar==1):
                from administrador import Administrador
                Administrador.menu_adm(cod)
            else:
                exit
        else:
            print('Quarto não inserido!')
    #método alterar dados do quarto
    def altera(self,op):
        #trazendo conexao e criando cursor
        con=conect.conecta()
        cursor=con.cursor()
        tupla=(self.numero,self.custo,self.tipo,self.status,op)
        #atualizando dados no banco de dados
        cursor.execute('update quarto set numero=%s, custo_quarto=%s,tipo=%s,status=%s where idquarto=%s',(tupla))
        con.commit()
        row=cursor.rowcount
        #verifica atualizalção
        if(row>=1):
            print('Alterado com sucesso!')
            op2=int(input('''
            Deseja voltar?
            1.Sim
            2.Não
            '''))
            if(op2==1):
                from administrador import Administrador
                Administrador.menu_adm()
            else:
                exit
    #método de listar os quartos 
    def listar():
        #trazendo conexao e criando cursor
        con=conect.conecta()
        cursor=con.cursor()
        #query de consulta dos quartos 
        cursor.execute('select*from quarto where status=1')
        result=cursor.fetchall()
        #Mostrando quartos na tela
        print("="*76,"Quartos","="*73)
        for i in result:
            print('Nº: ',i[1])
            print('Id: ',i[0])
            print('Tipo: ',i[2])
            print('Estadia: ',i[3])
            print('Status: ',i[4])
            print('Id do Administrador que Adicionou o quarto: ',i[5])
            print('='*158)

    '''def listar_desocupado(data_entrada,data_saida,codigo):
        con=conect.conecta()
        cursor=con.cursor()
        tupla=(codigo,data_entrada,data_saida,data_entrada,data_saida,data_entrada,data_saida)
        cursor.execute('SELECT * FROM reserva r WHERE fk_idquarto=%s and (data_entrda<=%s and data_saida>=%s) or ((data_entrada between %s and %s) and (data_saida between %s and %s));',(tupla))
        result=cursor.fetchall()
        print("="*76,"Quartos","="*73)
        for i in result:
            print('Nº: ',i[1])
            print('Id: ',i[0])
            print('Tipo: ',i[2])
            print('Estadia: ',i[3])
            print('Status: ',i[4])
            print('Id do Administrador que Adicionou o quarto: ',i[5])
            print('='*158)'''