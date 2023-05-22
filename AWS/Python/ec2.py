import os
from dotenv import load_dotenv
import boto3

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Utilisation d'Amazon EC2
ec2_client = boto3.client('ec2')

# Utilisez les variables d'environnement
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Utilisez les variables dans votre code AWS avec les clients et les appels API appropriés
instance_id = 'i-0123456789abcdef0'

# Exemple 1: Démarrer une instance EC2
ec2_client.start_instances(InstanceIds=[instance_id])
print(f'L\'instance EC2 avec l\'ID "{instance_id}" a été démarrée.')

# Exemple 2: Arrêter une instance EC2
ec2_client.stop_instances(InstanceIds=[instance_id])
print(f'L\'instance EC2 avec l\'ID "{instance_id}" a été arrêtée.')

# Exemple 3: Obtenir des informations sur une instance EC2
response = ec2_client.describe_instances(InstanceIds=[instance_id])
instance = response['Reservations'][0]['Instances'][0]
print(f'ID de l\'instance : {instance["InstanceId"]}')
print(f'Type d\'instance : {instance["InstanceType"]}')
print(f'État de l\'instance : {instance["State"]["Name"]}')
