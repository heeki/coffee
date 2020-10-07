#!/bin/bash

while getopts p:t:s:v:b: flag
do
    case "${flag}" in
        t) TEMPLATE=${OPTARG};;
        s) STACK=${OPTARG};;
        v) VERB=${OPTARG};;
        b) BUILD=${OPTARG};;
    esac
done

function usage {
    echo "deploy.sh -t [template_file] -s [stack_name] -v [deploy|local] -b [true|false]" && exit 1
}

if [ -z "$TEMPLATE" ]; then usage; fi
if [ -z "$STACK" ]; then usage; fi
if [ -z "$VERB" ]; then VERB="deploy"; fi
if [ -z "$BUILD" ]; then BUILD="false"; fi

BASENAME=`basename $TEMPLATE .yaml`
OUTPUT="iac/${BASENAME}_output.yaml"
LOCAL="$OUTPUT"
source etc/${BASENAME}.sh

aws s3 cp iac/swagger.yaml s3://${P_SWAGGER_BUCKET}/${P_SWAGGER_KEY}

echo
case $BUILD in
true)
    sam build --profile $PROFILE --build-dir build --manifest requirements.txt --template $TEMPLATE --parameter-overrides $PARAMS --use-container 
    sam package --template-file build/template.yaml --output-template-file $OUTPUT --s3-bucket $S3BUCKET
    LOCAL="build/template.yaml"
    ;;
*)
    sam package --template-file $TEMPLATE --output-template-file $OUTPUT --s3-bucket $S3BUCKET
    ;;
esac

case $VERB in
deploy)
    sam deploy --template-file $OUTPUT --stack-name $STACK --parameter-overrides $PARAMS --capabilities CAPABILITY_NAMED_IAM
    ;;
local)
    sam local invoke -e etc/event.json -t $LOCAL ExampleFn
    ;;
esac