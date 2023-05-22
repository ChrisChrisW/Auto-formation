import AWS from "aws-sdk";

// Charger les variables d'environnement depuis le fichier .env
require("dotenv").config();

// Configuration du SDK AWS avec les informations d'identification
AWS.config.update({
	accessKeyId: process.env.AWS_ACCESS_KEY_ID,
	secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
});

// Utilisation d'Amazon S3
const s3 = new AWS.S3();

// Utilisez les variables d'environnement
const bucketName = "mon-seau-s3";
const objectKey = "mon-objet.txt";
const filePath = "/chemin/vers/mon-fichier.txt";

// Uploader un objet dans un seau S3
const uploadParams = {
	Bucket: bucketName,
	Key: objectKey,
	Body: require("fs").createReadStream(filePath),
};

s3.upload(uploadParams, (err: any, data: any) => {
	if (err) {
		console.error("Erreur lors de l'upload de l'objet:", err);
	} else {
		console.log(
			`L'objet "${objectKey}" a été uploadé dans le seau S3 "${bucketName}".`
		);
	}
});
