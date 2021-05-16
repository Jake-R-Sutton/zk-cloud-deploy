# Configurable Deployment of Zookeepers to AWS 
## CSE 223B
----------------------------------------------
### Jake Sutton, Andrew Whitaker, Deepak Kharki

To leverage this repository to deploy clusters to AWS, follow these 
configuration steps:

1. Create an Key Pair that can be used to create the AWS instances 

    $ aws ec2 create-key-pair --key-name my-key-pair --query "KeyMaterial" --output text > my-key-pair.pem
    $ chmod 400 my-key-pair.pem


