import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "test"


try:
    connection = mysql.connection.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connexion à la base de donnée MySQL réussie.")

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de donnée: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connexion à la base de donnée MySQL fermée")


def get(connection):
    cursor = connection.cursor()

    select_query = "SELECT * FROM first"
    cursor.execute(select_query)

    result = cursor.fetchall()

    data = []
    for row in result:
        data.append(row)
    
    cursor.close
    return data

def post(connection):
    cursor = connection.cursor()

    insert_query = "INSERT INTO first (value1, value2) VALUES (%s, %s)"
    data_to_insert = ("valeur1", "valeur2")

    cursor.execute(insert_query, data_to_insert)
    connection.commit()

    cursor.close
    return

def update(connection):
    cursor = connection.cursor()

    update_query = "UPDATE first SET colonne1 = %s WHERE colonne2 = %s"
    data_to_update = ("valeur1", "valeur2")

    cursor.execute(update_query, data_to_update)
    connection.commit()

    cursor.close
    return

def delete(connection):
    cursor = connection.cursor()

    delete_query = "DELETE FROM first WHERE condition"

    cursor.execute(delete_query)
    connection.commit()

    cursor.close
    return