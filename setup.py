# https://docs.python.org/3/library/sqlite3.html
import sqlite3

conn = sqlite3.connect ('exemplo.db')

c = conn.cursor ()
# Criar a tabela
c.execute ('' 'CREATE TABLE ações
             (texto de data, texto trans, texto de símbolo, quantidade real, preço real) '' ')

# Insira uma linha de dados
c.execute ("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.14)")

# Salvar (confirmar) como mudança
conn.commit ()

# Também podemos fechar a conexão se terminarmos com isso.
# Apenas declarar-se de que todas as alterações foram confirmadas ou serão perdidas.
conn.close ()
