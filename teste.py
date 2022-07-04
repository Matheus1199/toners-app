import pyodbc
import pandas as pd 

def retornar_conexap_sql():
    server = '192.168.10.250' 
    database = 'barsottisolucoes' 
    username = 'sa' 
    password = 'sql@964012' 
    string_conexao = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password + ';TrustedConnection=true'
    conexao = pyodbc.connect(string_conexao)
    return conexao

conn = retornar_conexap_sql()

cursor = conn.cursor()

id = 1

id_cliente = """SELECT c.Id_Cliente
FROM TbL_Clientes C, Tbl_Pedidos P
WHERE  p.Cod_Cliente = C.Id_Cliente and p.Data >= '2022' and c.Ativo = 1 and Id_Cliente <> 1
ORDER BY p.Data desc"""

comando = f"""SELECT top 3 C.Nome, P.Data, P.Valor_Total
    FROM TbL_Clientes C, Tbl_Pedidos P
    WHERE  p.Cod_Cliente = C.Id_Cliente and p.Cod_Cliente = {id}
    ORDER BY p.Data desc"""

comando2 = f"""SELECT C.Nome
    FROM TbL_Clientes C"""

tabela = pd.read_sql(comando2, conn)

tabela.head()

tabela["Nome"].head()

