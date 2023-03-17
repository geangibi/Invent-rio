
import sqlite3 as lite


con = lite.connect('dados.db')

with con: 
        cur=con.cursor()
        cur.execute("CREATE TABLE invertario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")


'''import pyodbc

def conecta_ao_banco(driver='SQL Server Native Client 11.0', server='PR028GSC008\SQLEXPRESS', database='dbagenda', username=None, password=None, trusted_connection='yes'):

    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conecta_ao_banco()

cursor.execute('Create table iventario (id int identity(1,1) primary key, nome varchar(30), local varchar(50), descricao varchar(100), marcar varchar(50), data_compra date, valor_compra float, serie varchar(30), imagem varchar(100))')

conexao.commit()
conexao.close()'''