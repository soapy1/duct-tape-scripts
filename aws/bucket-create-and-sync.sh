SOURCE_BUCKET=$1
DEST_BUCKET=$2

echo "source: $SOURCE_BUCKET"
echo "destination: $DEST_BUCKET"

echo "creating destination bucket"
aws s3api create-bucket --bucket $DEST_BUCKET

echo "syncing"
aws s3 sync s3://$SOURCE_BUCKET s3://$DEST_BUCKET

echo "delete source bucket $SOURCE (yes/no)?"
read DELETE_BUCKET

if [ $DELETE_BUCKET == "yes" ]; then
  echo "deleting $SOURCE_BUCKET"
  aws s3 rb s3://$SOURCE_BUCKET --force
else
  echo "NOT deleting"
fi
