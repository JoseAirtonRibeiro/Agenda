import mysql.connector

conexao = mysql.connector.connect(host="localhost", user="root", password="q1w2e3", database="workbank1")
print(conexao)
cur=conexao.cursor()
 #C
cur.execute("insert into pessoas "
            "(nome , datanasc) "
            "value"
            "('Algum Nome Bom 2', '2004-06-04')")
conexao.commit() #Commita mudanças no banco com o codigo
 #R
cur.execute("select * from pessoas ")
lista = cur.fetchall()
for i in lista:
    print(i)
 #U
nome = input("NOME: ")
cod = int(input("ID: "))
sql = f"update pessoas set nome = '{nome}' where id = {cod}"
cur.execute(sql)
conexao.commit()
 #D