# Must specify the name of the template
if [ $# -ne 1 ]
then
    echo Needs one argument: template name
    exit 1
fi

aws cloudformation delete-stack --stack-name $1