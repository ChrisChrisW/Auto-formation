# Guide d'utilisation d'AWS avec Python

Ce guide fournit des exemples de code et des instructions pour utiliser AWS (Amazon Web Services) avec Python. Les exemples couvrent les services AWS tels que Amazon S3, Amazon EC2 et Amazon DynamoDB. Les variables d'environnement sont utilisées pour stocker les informations d'identification AWS afin de garantir la sécurité.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Vous pouvez télécharger la dernière version de Python depuis le site officiel : [python.org](https://www.python.org/downloads/)

## Installation des dépendances

1. Installez la bibliothèque `python-dotenv` en exécutant la commande suivante :

`pip install python-dotenv`

1. Installez la bibliothèque `boto3` en exécutant la commande suivante :

`pip install boto3`

## Configuration des variables d'environnement

1. Créez un fichier `.env` dans le même répertoire que vos scripts Python. Ce fichier contiendra vos variables d'environnement sensibles, comme les informations d'identification AWS.

## Fichier .env

AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY

Assurez-vous de remplacer les valeurs `'YOUR_ACCESS_KEY'` et `'YOUR_SECRET_KEY'` par vos propres informations d'identification AWS.

## Utilisation des exemples de code

Voici une description de chaque exemple de code pour les services AWS spécifiques :

### Amazon S3 (stockage d'objets)

- **[s3.py](https://github.com/ChrisChrisW/Auto-formation/blob/main/AWS/Python/s3.py)** : Ce code montre comment utiliser les variables d'environnement pour interagir avec Amazon S3. Il comprend des exemples d'opérations courantes telles que l'upload d'un objet, le téléchargement d'un objet et la liste des objets dans un seau S3.

### Amazon EC2 (instances de calcul)

- **[ec2.py](https://github.com/ChrisChrisW/Auto-formation/blob/main/AWS/Python/ec2.py)** : Ce code montre comment utiliser les variables d'environnement pour interagir avec Amazon EC2. Il comprend des exemples d'opérations courantes telles que le démarrage et l'arrêt d'une instance EC2, ainsi que l'obtention d'informations sur une instance EC2 spécifique.

### Amazon DynamoDB (base de données NoSQL)

- **[dynamodb.py](https://github.com/ChrisChrisW/Auto-formation/blob/main/AWS/Python/dynamodb.py)** : Ce code montre comment insérer, récupérer et mettre à jour des items dans une table DynamoDB.*

Assurez-vous d'avoir correctement configuré vos variables d'environnement avant d'exécuter les codes.

## Remarques

- Gardez le fichier `.env` sécurisé et ne le partagez pas avec d'autres personnes ou ne le versionnez pas dans un système de contrôle de code source public.
- Assurez-vous d'avoir les autorisations appropriées pour accéder et utiliser les services AWS que vous ciblez.
- N'hésitez pas à consulter la documentation officielle d'AWS pour obtenir plus d'informations sur chaque service et ses fonctionnalités.

## Licence

Ce projet est sous licence [MIT](LICENSE).
