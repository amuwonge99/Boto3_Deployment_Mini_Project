# connect EC2 client
# Get response using client to information on all instances
# print the status of the instance

#frontend-1 i-05cf40adaf7800117
#frontend-2 i-0a11a649c3d2667cd

import boto3
import schedule


ec2_client = boto3.client("ec2", region_name= "eu-west-2")

def health_check_job():
    instance_statuses = ec2_client.describe_instance_status()["InstanceStatuses"]

    for status in instance_statuses:
        instance_id = status['InstanceId']
        instance_state = status['InstanceState']["Name"]
        system_status = status['SystemStatus']["Status"]
        instance_status = status["InstanceStatus"]["Status"]
        print(f"Instance ID {instance_id} has a state of {instance_state} with system status of {system_status} and instance status of {instance_status}")

schedule.every(5).seconds.do(health_check_job)

while True:
    schedule.run_pending()







