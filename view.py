import sqlite3 as lite

con = lite.connect('dados.db')

#conexão com banco de dados #CREATE

'''def conecta_ao_banco(driver='SQL Server Native Client 11.0', server='PR028GSC008\SQLEXPRESS', database='dbagenda', username=None, password=None, trusted_connection='yes'):

    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

con, cursor = conecta_ao_banco()'''

#CRUD 

def inserir_form(i):

#inserir dados 

    dados = ['sofa','sala de estar','vaso que comprei no magalu','Marca x','2023/02/03','1000','xxxxxx','c:imagens']

    with con:
        cur = con.cursor()
        query = "INSERT INTO invertario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

    con.commit()
#inserir_form()



def atualizar_form(i):
# atualizar dados 

    atualizar_dados = ['sofa','cozinha','vaso que comprei no magalu','Marca x','2023-02-03','1000','xxxxxx','c:imagens', 1]

    with con:
        cur = con.cursor()
        query = "UPDATE invertario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)

con.commit()

#Deletar dados
def deletar_form(i):

    with con:
        cur = con.cursor()
        query = "DELETE FROM invertario WHERE id=?"
        cur.execute(query, i)

con.commit()

#deletar_form()

#Ver dados:

def visualizar_dados():

    ver_dados = []

    with con:
        cur = con.cursor()
        query = "SELECT * FROM invertario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
        
        return(ver_dados)


def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM invertario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
        
    return(ver_dados_individual)

def total_valor():

    with con:
        cur = con.cursor()
        query = "SELECT SUM(valor_da_compra) FROM invertario"
        cur.execute(query)

        total = cur.fetchall()
    
    return(total)





