# Must specify the name of the template
if [ $# -ne 1 ]
then
    echo Needs one argument: template name
    exit 1
fi

echo "Deleting AWS Infrastructure..."
aws cloudformation delete-stack --stack-name $1

echo "Cleaning up local cluster data..."
rm out/*

echo "Done."