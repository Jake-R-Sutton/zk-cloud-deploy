# Configurable Deployment of Zookeepers to AWS 
## CSE 223B
----------------------------------------------
### Jake Sutton, Andrew Whitaker, Deepak Karki

To leverage this repository to deploy clusters to AWS, follow these configuration steps:

0. Install the AWS CLI and configure it for the account you plan to deploy to.

1. Create an Key Pair that can be used to create the AWS EC2 instances 

        $ aws ec2 create-key-pair --key-name my-key-pair --query "KeyMaterial" --output text > my-key-pair.pem
        $ chmod 400 my-key-pair.pem

2. Run

        $ ./deploy 3


----------------------------------------------
  Random useful command:

        aws ec2 describe-instances \
            --query "Reservations[*].Instances[*].PublicIpAddress" \
            --output=text

----------------------------------------------
### Remaining Work 
1. Debug cluster connectivity
2. Use a client like Kazoo to hit the remote cluster
3. Debug client connectivity. 


### Useful References 
1. https://medium.com/@pacuna/running-a-zookeeper-ensemble-on-aws-8025a66e0c1
2. https://zookeeper.apache.org/doc/r3.7.0/zookeeperStarted.html
