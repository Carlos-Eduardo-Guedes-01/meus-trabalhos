#impotando datetime
import datetime
class data:
    def ler_data():
        #Lendo datas
        ano=int(input('Informe o ano(YYY-mm-dd): '))
        mes=int(input('Informe o número do mês: '))
        dia=int(input('Informe o dia: '))
        #convertendo para tipo date do banco de dados
        data_entrada = datetime.datetime(ano,mes,dia,12,00,00,000)
        #retornando data_entrada
        return data_entrada