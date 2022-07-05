import mysql.connector
class OP:
    def__init__(self)
    conexao = mysql.connector.connect(host="localhost", user="root", password="q1w2e3", database="workbank1")
    print(conexao)
    cur=conexao.cursor()
    
    
    def insert(): #C
        conexao = mysql.connector.connect(host="localhost", user="root", password="q1w2e3", database="workbank1")
        cur.execute( "insert into pessoas "
                     "(nome , datanasc) "
                     "value"
                    f"('{nome}', '{datanas}')")
        conexao.commit()
        conexao.fetchall()
    
    
    def select(): #R
        conexao = mysql.connector.connect(host="localhost", user="root", password="q1w2e3", database="workbank1")
        cur.execute("select * from pessoas ")
        lista = cur.fetchall()
        for i in lista:
            print(i)
        conexao.fetchall()
     
    
    def update(): #U
        conexao = mysql.connector.connect(host="localhost", user="root", password="q1w2e3", database="workbank1")
        cod = int(input("ID: "))
        nome = input("NOME: ")
        sql = f"update pessoas set nome = '{nome}' where id = {cod}"
        cur.execute(sql)  
        conexao.fetchall()
    
    def delete(): #D
        conexao = mysql.connector.connect(host="localhost", user="root", password="q1w2e3", database="workbank1")
        cod = int(input("ID: "))
        sql = f"delete from pessoas where id = {cod}"
        cur.execute(sql)
        conexao.commit()
        conexao.fetchall()


conexao.fetchall()