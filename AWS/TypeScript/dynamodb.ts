import AWS from "aws-sdk";

// Charger les variables d'environnement depuis le fichier .env
require("dotenv").config();

// Configuration du SDK AWS avec les informations d'identification
AWS.config.update({
	accessKeyId: process.env.AWS_ACCESS_KEY_ID,
	secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
});

// Utilisation d'Amazon DynamoDB
const dynamodb = new AWS.DynamoDB();

// Utilisez les variables d'environnement
const tableName = "MaTable";
const id = "1";

// Insérer un nouvel item dans une table DynamoDB
const putParams = {
	TableName: tableName,
	Item: {
		Id: { S: id },
		Nom: { S: "John Doe" },
		Age: { N: "30" },
	},
};

dynamodb.putItem(putParams, (err: any, data: any) => {
	if (err) {
		console.error(
			"Erreur lors de l'insertion de l'item dans la table DynamoDB:",
			err
		);
	} else {
		console.log(`Nouvel item inséré dans la table DynamoDB "${tableName}".`);
	}
});

// Récupérer un item à partir de la table DynamoDB
const getParams = {
	TableName: tableName,
	Key: {
		Id: { S: id },
	},
};

dynamodb.getItem(getParams, (err: any, data: any) => {
	if (err) {
		console.error(
			"Erreur lors de la récupération de l'item depuis la table DynamoDB:",
			err
		);
	} else {
		const item = data.Item;
		console.log("ID:", item.Id.S);
		console.log("Nom:", item.Nom.S);
		console.log("Age:", item.Age.N);
	}
});

// Mettre à jour un item dans la table DynamoDB
const updateParams = {
	TableName: tableName,
	Key: {
		Id: { S: id },
	},
	AttributeUpdates: {
		Nom: { Action: "PUT", Value: { S: "Jane Doe" } },
		Age: { Action: "PUT", Value: { N: "32" } },
	},
};

dynamodb.updateItem(updateParams, (err: any, data: any) => {
	if (err) {
		console.error(
			"Erreur lors de la mise à jour de l'item dans la table DynamoDB:",
			err
		);
	} else {
		console.log(`Item mis à jour dans la table DynamoDB "${tableName}".`);
	}
});
