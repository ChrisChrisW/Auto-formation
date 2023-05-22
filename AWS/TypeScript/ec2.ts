import AWS from "aws-sdk";

// Charger les variables d'environnement depuis le fichier .env
require("dotenv").config();

// Configuration du SDK AWS avec les informations d'identification
AWS.config.update({
	accessKeyId: process.env.AWS_ACCESS_KEY_ID,
	secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
});

// Utilisation d'Amazon EC2
const ec2 = new AWS.EC2();

// Utilisez les variables d'environnement
const instanceId = "i-0123456789abcdef0";

// Démarrer une instance EC2
const startParams = {
	InstanceIds: [instanceId],
};

ec2.startInstances(startParams, (err: any, data: any) => {
	if (err) {
		console.error("Erreur lors du démarrage de l'instance EC2:", err);
	} else {
		console.log(`L'instance EC2 avec l'ID "${instanceId}" a été démarrée.`);
	}
});

// Arrêter une instance EC2
const stopParams = {
	InstanceIds: [instanceId],
};

ec2.stopInstances(stopParams, (err: any, data: any) => {
	if (err) {
		console.error("Erreur lors de l'arrêt de l'instance EC2:", err);
	} else {
		console.log(`L'instance EC2 avec l'ID "${instanceId}" a été arrêtée.`);
	}
});

// Obtenir des informations sur une instance EC2
const describeParams = {
	InstanceIds: [instanceId],
};

ec2.describeInstances(describeParams, (err: any, data: any) => {
	if (err) {
		console.error(
			"Erreur lors de l'obtention des informations sur l'instance EC2:",
			err
		);
	} else {
		const instance = data.Reservations[0].Instances[0];
		console.log("ID de l'instance:", instance.InstanceId);
		console.log("Type d'instance:", instance.InstanceType);
		console.log("État de l'instance:", instance.State?.Name);
	}
});
