Part 1 - Status of Instances

Requirements:

Connect to EC2 client
Get a response using client to information on all instances
Print the status of the instances

Part 2 Automating EBS Backups for Disaster Recovery

Requirements:

Connect to EC2 instances in the London region.

Find the volumes attached to the instances, and for each volume create a snapshot.

Print a confirmation with:
-InstanceId, VolumeId, SnapshotId, and timestamp.

Ensure the script can be scheduled to run daily

-------------------------------------------------------------------------------------------------------

Part 3 - Tag EC2 Instances by environment

Requirements:

Connect to and retrieves EC2 instances in both regions.

Add a tag called Environment with value:

"prod" for London

"dev" for Ireland

Ensure all instances get tagged correctly.

Confirm on AWS console showing InstanceId and the tag added.

