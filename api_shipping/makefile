include etc/execute_env.sh

sam.v1: sam.v1.package sam.v1.deploy
sam.v1.build:
	sam build --profile ${PROFILE} --template ${V1_TEMPLATE} --parameter-overrides ${V1_PARAMS} --build-dir build --manifest requirements.txt --use-container
sam.v1.package:
	aws s3 cp iac/swagger_v1.yaml s3://${P_SWAGGER_BUCKET}/${P_SWAGGERV1_KEY}
	sam package -t ${V1_TEMPLATE} --output-template-file ${V1_OUTPUT} --s3-bucket ${S3BUCKET}
sam.v1.deploy:
	sam deploy -t ${V1_OUTPUT} --stack-name ${V1_STACK} --parameter-overrides ${V1_PARAMS} --capabilities CAPABILITY_NAMED_IAM

sam.v1p: sam.v1p.package sam.v1p.deploy
sam.v1p.build:
	sam build --profile ${PROFILE} --template ${V1P_TEMPLATE} --parameter-overrides ${V1P_PARAMS} --build-dir build --manifest requirements.txt --use-container
sam.v1p.package:
	aws s3 cp iac/swagger_v1p.yaml s3://${P_SWAGGER_BUCKET}/${P_SWAGGERV1_KEY}
	sam package -t ${V1P_TEMPLATE} --output-template-file ${V1P_OUTPUT} --s3-bucket ${S3BUCKET}
sam.v1p.deploy:
	sam deploy -t ${V1P_OUTPUT} --stack-name ${V1P_STACK} --parameter-overrides ${V1P_PARAMS} --capabilities CAPABILITY_NAMED_IAM

sam.v2: sam.v2.package sam.v2.deploy
sam.v2.build:
	sam build --profile ${PROFILE} --template ${V2_TEMPLATE} --parameter-overrides ${V2_PARAMS} --build-dir build --manifest requirements.txt --use-container
sam.v2.package:
	aws s3 cp iac/swagger_v2.yaml s3://${P_SWAGGER_BUCKET}/${P_SWAGGERV2_KEY}
	sam package -t ${V2_TEMPLATE} --output-template-file ${V2_OUTPUT} --s3-bucket ${S3BUCKET}
sam.v2.deploy:
	sam deploy -t ${V2_OUTPUT} --stack-name ${V2_STACK} --parameter-overrides ${V2_PARAMS} --capabilities CAPABILITY_NAMED_IAM

sam.local.invoke:
	sam local invoke -t ${TEMPLATE} --parameter-overrides ${PARAMS} --env-vars etc/envvars.json -e etc/event.json Fn
sam.local.api:
	sam local start-api -t ${TEMPLATE} --parameter-overrides ${PARAMS}
lambda.invoke:
	aws --profile ${PROFILE} lambda invoke --function-name ${FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode
test:
	$(eval P_SWAGGER_KEY=$(shell shasum -a 256 iac/swagger.yaml | awk '{print $$1}'))
clean:
	rm -rf build/*