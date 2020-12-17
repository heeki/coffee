include etc/execute_env.sh

sam: sam.package sam.deploy
sam.build:
	sam build --profile ${PROFILE} --template ${TEMPLATE} --parameter-overrides ${PARAMS} --build-dir build --manifest requirements.txt --use-container
sam.package:
	aws s3 cp iac/asl.json s3://${P_ASLBUCKET}/${P_ASLKEY}
	sam package -t ${TEMPLATE} --output-template-file ${OUTPUT} --s3-bucket ${S3BUCKET}
sam.deploy:
	sam deploy -t ${OUTPUT} --stack-name ${STACK} --parameter-overrides ${PARAMS} --capabilities CAPABILITY_NAMED_IAM

sam.local.invoke.labels:
	sam local invoke -t ${TEMPLATE} --parameter-overrides ${PARAMS} --env-vars etc/envvars.json -e etc/event.json FnLabels | jq
sam.local.invoke.processor:
	sam local invoke -t ${TEMPLATE} --parameter-overrides ${PARAMS} --env-vars etc/envvars.json -e etc/event.json FnProcessor | jq
sam.local.api:
	sam local start-api -t ${TEMPLATE} --parameter-overrides ${PARAMS}
lambda.invoke:
	aws --profile ${PROFILE} lambda invoke --function-name ${FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode
sf.invoke:
	aws --profile ${PROFILE} stepfunctions start-execution --state-machine-arn ${P_SF} --input file://etc/event.json | jq

s3.cp:
	aws s3 cp var/w3_1.png s3://${P_REKBUCKET}/w3_1.png
s3.rm:
	aws s3 rm s3://${P_REKBUCKET}/w3_1.png
presigned.upload:
	curl -v --upload-file ${P_FILE} ${P_PRESIGNED_URL}