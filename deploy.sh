if [ $# -ne 1 ]
then
    echo Missing an argument: zookeeper count
    exit 1
fi

# generate the new EC2 templates
echo "Generating EC2 CF..."
python cfgen/zk_cf_gen.py $1 > templates/cluster.yml 

echo "Running AWS CF deploy..."
aws cloudformation deploy \
 --template         templates/cluster.yml \
 --stack-name       cse223b-zk-stack 

echo "Gathering Cluster IPs..."
aws ec2 describe-instances \
            --query "Reservations[*].Instances[*].PublicIpAddress" \
            --output=text > out/cluster_ips.txt

echo "Generating dynamic zoo.cfg..."
python cfgen/zk_conf_gen.py > out/dynamic_conf.cfg 

