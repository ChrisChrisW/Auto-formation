import os
from dotenv import load_dotenv
import boto3

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Utilisation d'Amazon DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Utilisez les variables d'environnement
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Utilisez les variables dans votre code AWS avec les clients et les appels API appropriés
table_name = 'MaTable' # TODO : changer le nom de la table
item = {
    'Id': {'N': '1'},
    'Nom': {'S': 'John Doe'},
    'Age': {'N': '30'}
} # TODO : Changer la donnée a insérer

# Exemple 1: Insérer un nouvel item dans une table DynamoDB
dynamodb_client.put_item(TableName=table_name, Item=item)
print(f'Nouvel item inséré dans la table DynamoDB "{table_name}".')

# Exemple 2: Récupérer un item à partir de la table DynamoDB
key = {'Id': {'N': '1'}} # TODO : changer la clé cherchée
response = dynamodb_client.get_item(TableName=table_name, Key=key)
item = response['Item']
print(f'ID : {item["Id"]["N"]}, Nom : {item["Nom"]["S"]}, Age : {item["Age"]["N"]}')

# Exemple 3: Mettre à jour un item dans la table DynamoDB
updated_item = {
    'Id': {'N': '1'},
    'Nom': {'S': 'Jane Doe'},
    'Age': {'N': '32'}
} # TODO : comme item
dynamodb_client.put_item(TableName=table_name, Item=updated_item)
print(f'Item mis à jour dans la table DynamoDB "{table_name}".')
