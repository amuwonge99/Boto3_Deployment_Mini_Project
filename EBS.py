import boto3
import schedule

ec2_client = boto3.client("ec2", region_name= "eu-west-2")

def daily_backups():
        instance_volumes = ec2_client.describe_volumes(["Volumes"])

instance_volumes = ec2_client.describe_volumes()["Volumes"]

for volume in instance_volumes:
        volume_id = volume['VolumeId']
        new_snapshot = ec2_client.create_snapshot(
                VolumeId=volume_id
                )
        print(f"Create snapshot {new_snapshot}")

schedule.every(5).seconds.do(daily_backups)

while True:
        schedule.run_pending()







