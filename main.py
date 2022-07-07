import pyodbc
import pandas as pd
import numpy as np

server = '192.168.10.250' 
database = 'barsottisolucoes' 
username = 'sa' 
password = 'sql@964012' 
conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conexao.cursor()


id_cliente = """SELECT c.Id_Cliente
    FROM TbL_Clientes C, Tbl_Pedidos P
    WHERE  p.Cod_Cliente = C.Id_Cliente and p.Data >= '2022' and c.Ativo = 1 and Id_Cliente <> 1
    ORDER BY p.Data desc"""


tabela = pd.read_sql(id_cliente, conexao)


cont = 0
id = tabela.to_numpy()
cliente = int(id[cont])


for cliente in range(cont, len(id)):
    comando = f"""SELECT top 3 C.Nome, P.Data, P.Valor_Total
        FROM TbL_Clientes C, Tbl_Pedidos P
        WHERE  p.Cod_Cliente = C.Id_Cliente and p.Cod_Cliente = {cliente}
        ORDER BY p.Data desc"""
    tabela2 = pd.read_sql(comando, conexao)
    print(tabela2)
    cont += 1

var = tabela2.to_numpy()


