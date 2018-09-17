SECURITY_GROUPS=$(aws ec2 describe-security-groups | jq '.SecurityGroups[].GroupId' -r)

for sg in $SECURITY_GROUPS
do
    NUM_INSTANCE=$(aws ec2 describe-instances --filters "Name=instance.group-id,Values=${sg}" | jq '.Reservations | length')
    if [[ $NUM_INSTANCE -lt 1 ]]
    then
      echo "${sg} is unused, deleting"
      echo $sg >> unsued.txt
      aws ec2 delete-security-group --group-id $sg
    fi
done
