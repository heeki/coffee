include etc/execute_env.sh

nlb: nlb.package nlb.deploy
nlb.package:
	sam package -t ${NLB_TEMPLATE} --output-template-file ${NLB_OUTPUT} --s3-bucket ${S3BUCKET}
nlb.deploy:
	sam deploy -t ${NLB_OUTPUT} --stack-name ${NLB_STACK} --parameter-overrides ${NLB_PARAMS} --capabilities CAPABILITY_NAMED_IAM

api.v1: api.v1.package api.v1.deploy
api.v1.build:
	sam build --profile ${PROFILE} --template ${V1_TEMPLATE} --parameter-overrides ${V1_PARAMS} --build-dir build --manifest requirements.txt --use-container
api.v1.package:
	sam package -t ${V1_TEMPLATE} --output-template-file ${V1_OUTPUT} --s3-bucket ${S3BUCKET}
api.v1.deploy:
	sam deploy -t ${V1_OUTPUT} --stack-name ${V1_STACK} --parameter-overrides ${V1_PARAMS} --capabilities CAPABILITY_NAMED_IAM

api.v1p: api.v1p.package api.v1p.deploy
api.v1p.build:
	sam build --profile ${PROFILE} --template ${V1P_TEMPLATE} --parameter-overrides ${V1P_PARAMS} --build-dir build --manifest requirements.txt --use-container
api.v1p.package:
	sam package -t ${V1P_TEMPLATE} --output-template-file ${V1P_OUTPUT} --s3-bucket ${S3BUCKET}
api.v1p.deploy:
	sam deploy -t ${V1P_OUTPUT} --stack-name ${V1P_STACK} --parameter-overrides ${V1P_PARAMS} --capabilities CAPABILITY_NAMED_IAM

api.v2: api.v2.package api.v2.deploy
api.v2.build:
	sam build --profile ${PROFILE} --template ${V2_TEMPLATE} --parameter-overrides ${V2_PARAMS} --build-dir build --manifest requirements.txt --use-container
api.v2.package:
	sam package -t ${V2_TEMPLATE} --output-template-file ${V2_OUTPUT} --s3-bucket ${S3BUCKET}
api.v2.deploy:
	sam deploy -t ${V2_OUTPUT} --stack-name ${V2_STACK} --parameter-overrides ${V2_PARAMS} --capabilities CAPABILITY_NAMED_IAM

sam.local.invoke:
	sam local invoke -t ${V1_TEMPLATE} --parameter-overrides ${V1_PARAMS} --env-vars etc/envvars.json -e etc/event.json Fn
sam.local.api:
	sam local start-api -t ${V1_TEMPLATE} --parameter-overrides ${V1_PARAMS}
lambda.invoke:
	aws --profile ${PROFILE} lambda invoke --function-name ${FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode
test:
	$(eval P_SWAGGER_KEY=$(shell shasum -a 256 iac/swagger.yaml | awk '{print $$1}'))
clean:
	rm -rf build/*