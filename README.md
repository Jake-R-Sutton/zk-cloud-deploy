# Configurable Deployment of Zookeepers to AWS 
## CSE 223B
----------------------------------------------
### Jake Sutton, Andrew Whitaker, Deepak Karki

To leverage this repository to deploy clusters to AWS, follow these configuration steps:

0. Install the AWS CLI and configure it for the account you plan to deploy to.

2. Create an Key Pair that can be used to create the AWS EC2 instances 

        $ aws ec2 create-key-pair --key-name my-key-pair --query "KeyMaterial" --output text > my-key-pair.pem
        $ chmod 400 my-key-pair.pem

2. Run

        $ ./deploy zookeeper
