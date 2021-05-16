# Must specify the name of the template
if [ $# -ne 1 ]
then
    echo Needs one argument: template name
    exit 1
fi

# Deploy the cloud formation stack to aws
aws cloudformation deploy \
 --template         templates/$1.yml \
 --stack-name       cse223b-zk-stack 

