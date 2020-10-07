#!/bin/bash

while getopts p:s: flag
do
    case "${flag}" in
        s) STACK=${OPTARG};;
    esac
done

function usage {
    echo "describe.sh -p [profile] -s [stack]" && exit 1
}

if [ -z "$STACK" ]; then usage; fi

source etc/vars.sh

OUTPUT=$(aws --profile $PROFILE cloudformation describe-stacks --stack-name $STACK)
case $STACK in
unicorn-api-certificate)
    P_CERTARN=$(echo $OUTPUT | jq -r -c '.["Stacks"][]["Outputs"][]  | select(.OutputKey == "certificateArn") | .OutputValue')
    echo "export P_CERTARN=${P_CERTARN}"
    ;;
unicorn-api-domain)
    P_DOMAINID=$(echo $OUTPUT | jq -r -c '.["Stacks"][]["Outputs"][]  | select(.OutputKey == "apiDomain") | .OutputValue')
    P_DOMAINSET=$(echo $OUTPUT | jq -r -c '.["Stacks"][]["Outputs"][]  | select(.OutputKey == "apiDomainRecordSet") | .OutputValue')
    for var in {P_DOMAINID,P_DOMAINSET}; do echo "export $var=${!var}"; done
    ;;
esac