import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",     # Endereço do servidor MySQL
        user="root",   # Usuário do MySQL
        password="", # Senha do MySQL
        database="bancogan"   # Nome do banco de dados
    )