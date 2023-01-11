import csv
import mysql.connector

# Conecte-se ao servidor MySQL
cnx = mysql.connector.connect(user='xxxxx', password='xxxxx', host='xxxxx', database='xxxxx')
cursor = cnx.cursor()

# Leia o arquivo CSV
with open('C:\\xxxxx\\xxxxx\\xxxxx\\xxxxx\\todaspalavrasemportugues2.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    # Percorra cada linha do arquivo
    for row in reader:
        # Inserir cada palavra na tabela 'dic_palavras'
        cursor.execute("INSERT INTO dic_palavras (dic_palavra) VALUES (%s)", (row[0],))

# Feche a conexão com o banco de dados
cnx.commit()
cursor.close()
cnx.close()