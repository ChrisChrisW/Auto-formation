import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateItemRequest;

import java.util.HashMap;
import java.util.Map;

public class AwsDynamoDBExample {
    public static void main(String[] args) {
        // Utilisation d'Amazon DynamoDB
        DynamoDbClient dynamoDbClient = DynamoDbClient.create();

        // Utilisez les variables d'environnement
        String tableName = "MaTable";
        String id = "1";

        // Insérer un nouvel item dans une table DynamoDB
        Map<String, Object> item = new HashMap<>();
        item.put("Id", id);
        item.put("Nom", "John Doe");
        item.put("Age", 30);

        PutItemRequest putItemRequest = PutItemRequest.builder()
                .tableName(tableName)
                .item(item)
                .build();
        dynamoDbClient.putItem(putItemRequest);

        System.out.println("Nouvel item inséré dans la table DynamoDB \"" + tableName + "\".");

        // Récupérer un item à partir de la table DynamoDB
        GetItemRequest getItemRequest = GetItemRequest.builder()
                .tableName(tableName)
                .key(Collections.singletonMap("Id", AttributeValue.builder().s(id).build()))
                .build();
        Map<String, AttributeValue> itemResponse = dynamoDbClient.getItem(getItemRequest).item();

        System.out.println("ID : " + itemResponse.get("Id").s());
        System.out.println("Nom : " + itemResponse.get("Nom").s());
        System.out.println("Age : " + itemResponse.get("Age").n());

        // Mettre à jour un item dans la table DynamoDB
        Map<String, AttributeValueUpdate> updatedValues = new HashMap<>();
        updatedValues.put("Nom",
                AttributeValueUpdate.builder().value(AttributeValue.builder().s("Jane Doe").build()).build());
        updatedValues.put("Age",
                AttributeValueUpdate.builder().value(AttributeValue.builder().n("32").build()).build());

        UpdateItemRequest updateItemRequest = UpdateItemRequest.builder()
                .tableName(tableName)
                .key(Collections.singletonMap("Id", AttributeValue.builder().s(id).build()))
                .attributeUpdates(updatedValues)
                .build();
        dynamoDbClient.updateItem(updateItemRequest);

        System.out.println("Item mis à jour dans la table DynamoDB \"" + tableName + "\".");
    }
}
