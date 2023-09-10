import psycopg2

host = "localhost"
user = "root"
password = "root"
database = "test"


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connexion à la base de donnée MySQL réussie.")

except psycopg2.Error as err:
    print(f"Erreur de connexion à la base de donnée: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connexion à la base de donnée MySQL fermée")
