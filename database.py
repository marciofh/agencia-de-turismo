import psycopg2

host = "localhost"
dbname = "turismo"
user = "Marcio"
password = "1290"
sslmode = "require"

try :
    conn = psycopg2.connect("host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode))
    cursor = conn.cursor()
except Exception as e:
    print(e)
    exit()

cursor.execute("INSERT INTO turismo_schemas.passagem_aerea(origem, destino, duracao, conexao, preco) VALUES ('MELHOR', 'DO', 'MUNDO', 'RECEBA', 1);")
conn.commit()

try:
    cursor.execute("SELECT * FROM turismo_schemas.passagem_aerea")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print(e)
    exit()

