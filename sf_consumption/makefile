include etc/execute_env.sh
$(eval P_ASLKEY=$(shell shasum -a 256 iac/asl.json | awk '{print $$1}'))
PARAMS="ParameterKey=busName,ParameterValue=${P_NAME} ParameterKey=aslBucket,ParameterValue=${P_ASLBUCKET} ParameterKey=aslKey,ParameterValue=${P_ASLKEY} "

sam: sam.package sam.deploy

sam.build:
	sam build --profile ${PROFILE} --template iac/sf.yaml --parameter-overrides ${PARAMS} --build-dir build --manifest requirements.txt --use-container

sam.package:
	aws s3 cp iac/asl.json s3://${P_ASLBUCKET}/${P_ASLKEY}
	sam package -t iac/sf.yaml --output-template-file iac/sf_output.yaml --s3-bucket ${S3BUCKET}

sam.deploy:
	sam deploy -t iac/sf_output.yaml --stack-name unicorn-sf-consumption --parameter-overrides ${PARAMS} --capabilities CAPABILITY_NAMED_IAM

sam.local.invoke:
	sam local invoke -t iac/sf.yaml --parameter-overrides ${PARAMS} --env-vars etc/envvars.json -e etc/event.json Fn

sam.local.api:
	sam local start-api -t iac/sf.yaml --parameter-overrides ${PARAMS}

lambda.invoke:
	aws --profile ${PROFILE} lambda invoke --function-name ${P_FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode

sf.invoke:
	aws --profile ${PROFILE} stepfunctions start-execution --state-machine-arn ${P_SF} --input file://etc/event.json | jq

test:
	$(eval TMP=$(shell shasum -a 256 iac/asl.json | awk '{print $$1}'))

clean:
	rm -rf build/*