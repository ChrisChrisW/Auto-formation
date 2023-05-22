import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.StartInstancesRequest;
import software.amazon.awssdk.services.ec2.model.StopInstancesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesResponse;
import software.amazon.awssdk.services.ec2.model.Reservation;
import software.amazon.awssdk.services.ec2.model.Instance;

public class AwsEc2Example {
    public static void main(String[] args) {
        // Utilisation d'Amazon EC2
        Ec2Client ec2Client = Ec2Client.create();

        // Utilisez les variables d'environnement
        String instanceId = "i-0123456789abcdef0";

        // Démarrer une instance EC2
        StartInstancesRequest startInstancesRequest = StartInstancesRequest.builder()
                .instanceIds(instanceId)
                .build();
        ec2Client.startInstances(startInstancesRequest);

        System.out.println("L'instance EC2 avec l'ID \"" + instanceId + "\" a été démarrée.");

        // Arrêter une instance EC2
        StopInstancesRequest stopInstancesRequest = StopInstancesRequest.builder()
                .instanceIds(instanceId)
                .build();
        ec2Client.stopInstances(stopInstancesRequest);

        System.out.println("L'instance EC2 avec l'ID \"" + instanceId + "\" a été arrêtée.");

        // Obtenir des informations sur une instance EC2
        DescribeInstancesRequest describeInstancesRequest = DescribeInstancesRequest.builder()
                .instanceIds(instanceId)
                .build();
        DescribeInstancesResponse describeInstancesResponse = ec2Client.describeInstances(describeInstancesRequest);

        Reservation reservation = describeInstancesResponse.reservations().get(0);
        Instance instance = reservation.instances().get(0);

        System.out.println("ID de l'instance : " + instance.instanceId());
        System.out.println("Type d'instance : " + instance.instanceType());
        System.out.println("État de l'instance : " + instance.state().nameAsString());
    }
}
