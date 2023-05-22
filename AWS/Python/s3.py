import os
from dotenv import load_dotenv
import boto3

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Utilisation d'Amazon S3
s3_client = boto3.client('s3')

# Utilisez les variables d'environnement
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Utilisez les variables dans votre code AWS avec les clients et les appels API appropriés
bucket_name = 'mon-seau-s3' # TODO : changer le nom
object_key = 'mon-objet.txt' # TODO : nom du ficher en question
local_file_path = '/chemin/vers/mon-fichier.txt' # TODO : le parcours du fichier

# Exemple 1: Uploader un objet dans un seau S3
s3_client.upload_file(local_file_path, bucket_name, object_key)
print(f'L\'objet "{object_key}" a été uploadé dans le seau S3 "{bucket_name}".')

# Exemple 2: Télécharger un objet depuis un seau S3
s3_client.download_file(bucket_name, object_key, local_file_path)
print(f'L\'objet "{object_key}" a été téléchargé depuis le seau S3 "{bucket_name}".')

# Exemple 3: Lister tous les objets dans un seau S3
response = s3_client.list_objects(Bucket=bucket_name)
objects = response['Contents']
for obj in objects:
    print(f'Objet : {obj["Key"]}, Taille : {obj["Size"]} octets')
