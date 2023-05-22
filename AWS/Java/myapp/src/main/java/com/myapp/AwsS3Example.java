import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

public class AwsS3Example {
    public static void main(String[] args) {
        // Utilisation d'Amazon S3
        S3Client s3Client = S3Client.create();

        // Utilisez les variables d'environnement
        String bucketName = "mon-seau-s3";
        String objectKey = "mon-objet.txt";
        String filePath = "/chemin/vers/mon-fichier.txt";

        // Uploader un objet dans un seau S3
        PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                .bucket(bucketName)
                .key(objectKey)
                .build();
        s3Client.putObject(putObjectRequest, RequestBody.fromFile(filePath));

        System.out.println("L'objet \"" + objectKey + "\" a été uploadé dans le seau S3 \"" + bucketName + "\".");
    }
}
