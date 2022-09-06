#importando mysql
import mysql.connector
class conect:
    def conecta():
        #conectando com banco de dados mysql
        con=mysql.connector.connect(host='localhost', user='root', password='123456', db='hotel')
        #retornando conexao
        return con