import pyodbc 

server = '192.168.10.250' 
database = 'barsottisolucoes' 
username = 'sa' 
password = 'sql@964012' 
conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conexao.cursor()

id_cliente = 295

comando = f"""SELECT top 3 C.Nome, P.Data, P.Valor_Total
FROM TbL_Clientes C, Tbl_Pedidos P
WHERE  p.Cod_Cliente = C.Id_Cliente and p.Cod_Cliente =  {id_cliente}
ORDER BY p.Data desc"""

cursor.execute(comando) 
row = cursor.fetchone() 
while row: 
    print(row[0], row[1], row[2])
    row = cursor.fetchone()

print("Conexão concluida")