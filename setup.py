# https://docs.python.org/3/library/sqlite3.html
import  sqlite3

conn  =  sqlite3 . conectar ( 'exemplo.db' )

c  =  con . cursor ()
# Criar a tabela
c . execute ( '' ' CRIAR  TABELA  a çõ es
             ( texto  de  data , texto  trans , texto  de  s í mbolo , quantidade  real , pre ç o  real ) '' ')

# Insira uma linha de dados
c . execute ( "INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.14)" )

# Salvar (confirmar) como mudança
con . commit ()

# Também podemos fechar a conexão se terminarmos com isso.
# Apenas declarar-se de que todas as mudanças foram confirmadas ou serão perdidas.
con . fechar ()
