include etc/execute_env.sh
PARAMS="ParameterKey=busName,ParameterValue=${P_NAME} ParameterKey=sfnConsumption,ParameterValue=${P_SF} "

sam: sam.package sam.deploy

sam.build:
	sam build --profile ${PROFILE} --template ${TEMPLATE} --parameter-overrides ${PARAMS} --build-dir build --manifest requirements.txt --use-container

sam.package:
	sam package -t ${TEMPLATE} --output-template-file ${OUTPUT} --s3-bucket ${S3BUCKET}

sam.deploy:
	sam deploy -t ${OUTPUT} --stack-name ${STACK} --parameter-overrides ${PARAMS} --capabilities CAPABILITY_NAMED_IAM

sam.local.invoke:
	sam local invoke -t ${TEMPLATE} --parameter-overrides ${PARAMS} --env-vars etc/envvars.json -e etc/event.json Fn

sam.local.api:
	sam local start-api -t ${TEMPLATE} --parameter-overrides ${PARAMS}

lambda.invoke:
	aws --profile ${PROFILE} lambda invoke --function-name ${FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode

eb.generator.fn:
	python3 util/generator.py --bus coffee --source heeki.generator --payload etc/event.json --count 1 | jq

eb.generator.sf:
	python3 util/generator.py --bus coffee --source heeki.iot --payload etc/event.json --count 1 | jq

test:
	echo $$(eval shasum -a 256 iac/swagger.yaml | awk '{print $$1}')

clean:
	rm -rf build/*