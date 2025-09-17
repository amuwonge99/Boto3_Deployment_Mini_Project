import boto3

ec2_client_london = boto3.client('ec2', region_name="eu-west-2")
ec2_client_ireland = boto3.client('ec2', region_name="eu-west-1")

instance_ids_london = []
res_london = ec2_client_london.describe_instances()["Reservations"]
for reservation in res_london:
    for instance in reservation["Instances"]:
        instance_ids_london.append(instance["InstanceId"])

print("London Instances:", instance_ids_london)

instance_ids_ireland = []
res_ireland = ec2_client_ireland.describe_instances()["Reservations"]
for reservation in res_ireland:
    for instance in reservation["Instances"]:
        instance_ids_ireland.append(instance["InstanceId"])

print("Ireland Instances:", instance_ids_ireland)

if instance_ids_london:
    ec2_client_london.create_tags(
        Resources=instance_ids_london,
        Tags=[{'Key': 'Env', 'Value': 'prod'}]
    )

if instance_ids_ireland:
    ec2_client_ireland.create_tags(
        Resources=instance_ids_ireland,
        Tags=[{'Key': 'Env', 'Value': 'dev'}]
    )

def tagger(tag_value, region):
    ec2_client = boto3.client('ec2', region_name=region)
    instance_ids = []
    res = ec2_client.describe_instances()["Reservations"]

    for reservation in res:
        for instance in reservation["Instances"]:
            instance_ids.append(instance["InstanceId"])

    if instance_ids:
        ec2_client.create_tags(
            Resources=instance_ids,
            Tags=[
                {
                    'Key': 'Env',
                    'Value': tag_value
                }
            ]
        )
        print(f"Tagged {len(instance_ids)} instances in {region} with Env={tag_value}")
    else:
        print(f"No instances found in {region}. Tagging skipped.")


tagger("dev", "eu-west-1")
tagger("prod", "eu-west-2")
