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

        $ ./deploy zookeeper


----------------------------------------------

### Remaining Work 

1. Create multiple instances with templating and correct configuration. Useful command: 

        aws ec2 describe-instances \
            --query "Reservations[*].Instances[*].PublicIpAddress" \
            --output=text

    - Update ZK Configuration
    - Start ZK instances
    - Debug instance connectivity

2. Try to use the a client like Kazoo against the remote cluster.
    - Debug connectivity. 