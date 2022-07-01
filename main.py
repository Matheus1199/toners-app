import pyodbc 

server = '192.168.10.250' 
database = 'barsottisolucoes' 
username = 'sa' 
password = 'sql@964012' 
conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conexao.cursor()
cursor2 = conexao.cursor()

id = 1

id_cliente = """SELECT c.Id_Cliente
FROM TbL_Clientes C, Tbl_Pedidos P
WHERE  p.Cod_Cliente = C.Id_Cliente and p.Data >= '2022' and c.Ativo = 1 and Id_Cliente <> 1
ORDER BY p.Data desc"""

comando = f"""SELECT top 3 C.Nome, P.Data, P.Valor_Total
    FROM TbL_Clientes C, Tbl_Pedidos P
    WHERE  p.Cod_Cliente = C.Id_Cliente and p.Cod_Cliente = {id}
    ORDER BY p.Data desc"""



cursor.execute(id_cliente) 
row = cursor.fetchone()
while row: 
    print(row[0])
    id = row[0]
    comando = f"""SELECT top 3 C.Nome, P.Data, P.Valor_Total
    FROM TbL_Clientes C, Tbl_Pedidos P
    WHERE  p.Cod_Cliente = C.Id_Cliente and p.Cod_Cliente = {id}
    ORDER BY p.Data desc"""
    cursor.execute(comando)  
    row2 = cursor.fetchone()
    while row2:
        print(id)
        print(row2[0])
        row2 = cursor.fetchone()
    row = cursor.fetchone()




print("Conexão concluida")