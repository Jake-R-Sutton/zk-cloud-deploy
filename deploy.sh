if [ $# -ne 1 ]
then
    echo Missing an argument: zookeeper count
    exit 1
fi

# generate the new EC2 templates
python cfgen/zk_cf_gen.py $1 > templates/cluster.yml 

# deploy the generated template
aws cloudformation deploy \
 --template         templates/cluster.yml \
 --stack-name       cse223b-zk-stack 
