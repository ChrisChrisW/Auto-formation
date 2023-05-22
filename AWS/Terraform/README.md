# Guide d'utilisation d'AWS avec Terraform

Ce guide vous montre comment utiliser Terraform pour créer des ressources AWS (Amazon S3, Amazon EC2, Amazon DynamoDB). Les exemples de configurations Terraform présentés ici vous guideront à travers la création des ressources dans votre compte AWS.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Terraform : [Installation de Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- Un compte AWS avec les informations d'identification appropriées

## Installation

1. Clonez ce dépôt GitHub ou téléchargez les fichiers nécessaires.

2. Accédez au répertoire du projet dans votre terminal.

## Configuration des variables

1. Créez un fichier `.env` dans le répertoire racine de votre projet.

2. Ouvrez le fichier `.env` et ajoutez les variables d'environnement nécessaires avec vos informations d'identification AWS. Par exemple :

   ```plaintext
   # Fichier .env
   AWS_ACCESS_KEY_ID=VOTRE_ACCESS_KEY
   AWS_SECRET_ACCESS_KEY=VOTRE_SECRET_KEY

Remplacez les valeurs VOTRE_ACCESS_KEY et VOTRE_SECRET_KEY par vos propres informations d'identification AWS.

## Utilisation des exemples de configurations Terraform

Dans les exemples suivants, nous utiliserons Terraform pour créer des ressources AWS.

***Amazon S3 (Simple Storage Service)***

- Configuration : s3.tf
- Cette configuration Terraform crée un seau S3 avec les autorisations appropriées.

***Amazon EC2 (Elastic Compute Cloud)***

- Configuration : ec2.tf
- Cette configuration Terraform crée une instance EC2 avec les paramètres spécifiés.

***Amazon DynamoDB (NoSQL Database Service)***

- Configuration : dynamodb.tf
- Cette configuration Terraform crée une table DynamoDB avec les attributs et paramètres spécifiés.

Assurez-vous d'avoir correctement configuré vos variables d'environnement avant d'exécuter les exemples de configurations Terraform.

## Exécution de Terraform

Pour exécuter Terraform, assurez-vous de vous trouver dans le répertoire contenant les fichiers de configuration Terraform et suivez les étapes suivantes :

Initialisez le répertoire Terraform :

1. Initialisez le répertoire Terraform :

> terraform init

2. Affichez un plan des ressources qui seront créées :

> terraform plan

3. Appliquez les changements et créez les ressources :
> terraform apply

4. Une fois que vous avez terminé avec les ressources, vous pouvez les détruire en utilisant la commande suivante :

> terraform destroy

Assurez-vous d'avoir vérifié et compris les effets de chaque commande Terraform avant de les exécuter.

N'hésitez pas à consulter la documentation officielle de Terraform et d'AWS pour obtenir plus d'informations sur chaque service et ses fonctionnalités.

## Licence

Ce projet est sous licence MIT.

N'oubliez pas d'ajuster le contenu en fonction de vos propres besoins spécifiques et d'inclure les fichiers de configuration Terraform correspondants dans votre répertoire.
