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

        $ ./deploy.sh 3


----------------------------------------------
### Deploying the Testing Cluster

        aws cloudformation deploy --template basic_cluster.yml --stack-name pub-sub-cluster-testt

### Multiplexed SSSH

        csshx --ssh_args "-i my-key-pair.pem" ec2-user@52.207.237.244 ec2-user@34.239.124.237 ec2-user@3.82.247.135

### Finishing Zookeeper Configuration 

1. Update the Zookeeper configurations at `/usr/local/zookeeper/conf/zoo.cfg`
   
        server.1=<IP_Address if remote else 0.0.0.0>:2888:3888
        server.2=<IP_Address if remote else 0.0.0.0>:2888:3888
        
2. Update the Zookeepers ID at `/var/lib/zookeeper/myid`

3. Start Zookeeper:

        sudo /usr/local/zookeeper/bin/zkServer.sh start
        sudo /usr/local/zookeeper/bin/zkServer.sh status
        ...
        sudo /usr/local/zookeeper/bin/zkServer.sh stop

----------------------------------------------
  Random useful command:

        aws ec2 describe-instances \
            --query "Reservations[*].Instances[*].PublicIpAddress" \
            --output=text
----------------------------------------------
### Useful References 
1. https://medium.com/@pacuna/running-a-zookeeper-ensemble-on-aws-8025a66e0c1
2. https://zookeeper.apache.org/doc/r3.7.0/zookeeperStarted.html
