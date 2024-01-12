import mysql.connector
#fornece os dados e faz conexão com o banco de dados
conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '2012',
    database= 'banco_viteco',
)

cursor = conexao.cursor() #cria o cursor

#CREATE
nome_produto = 'pedro'
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})' #CRIA NO BANCO DE DADOS O PRODUTO E O NOME
cursor.execute(comando)
conexao.commit() #edita um banco de dados

#UPDATE
nome_produto = "pedro"
valor = 10
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"' #ATUALIZA NO BANCO DE DADOS O PRODUTO E O NOME
cursor.execute(comando)
conexao.commit()

#DELETE
nome_produto = 'açai'
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"' #Deleta do banco de dados pelo nome (poderia ser por id, valor e etc...)
cursor.execute(comando)
conexao.commit()

#READ

comando = f'SELECT * FROM vendas' #CRIA NO BANCO DE DADOS O PRODUTO E O NOME
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)


cursor.close()
conexao.close()