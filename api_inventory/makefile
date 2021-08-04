include etc/environment.sh

settings: settings.package settings.deploy
settings.package:
	sam package --profile ${PROFILE2} -t ${SETTINGS_TEMPLATE} --output-template-file ${SETTINGS_OUTPUT} --s3-bucket ${S3BUCKET2}
settings.deploy:
	sam deploy --profile ${PROFILE2} -t ${SETTINGS_OUTPUT} --stack-name ${SETTINGS_STACK} --capabilities CAPABILITY_NAMED_IAM

api: api.package api.deploy
api.package:
	sam package --profile ${PROFILE2} -t ${APIGW_TEMPLATE} --output-template-file ${APIGW_OUTPUT} --s3-bucket ${S3BUCKET2}
api.deploy:
	sam deploy --profile ${PROFILE2} -t ${APIGW_OUTPUT} --stack-name ${APIGW_STACK} --parameter-overrides ${APIGW_PARAMS} --capabilities CAPABILITY_NAMED_IAM

bpm: bpm.package bpm.deploy
bpm.package:
	sam package --profile ${PROFILE1} -t ${BPM_TEMPLATE} --output-template-file ${BPM_OUTPUT} --s3-bucket ${S3BUCKET1}
bpm.deploy:
	sam deploy --profile ${PROFILE1} -t ${BPM_OUTPUT} --stack-name ${BPM_STACK} --parameter-overrides ${BPM_PARAMS} --capabilities CAPABILITY_NAMED_IAM

api.local.invoke:
	sam local invoke -t ${APIGW_TEMPLATE} --parameter-overrides ${APIGW_PARAMS} --env-vars etc/environment.json -e etc/event_api.json Fn | jq
api.local.api:
	sam local start-api -t ${APIGW_TEMPLATE} --parameter-overrides ${APIGW_PARAMS}
api.invoke:
	aws --profile ${PROFILE2} lambda invoke --function-name ${OUT_FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode
api.curl:
	curl -s -XGET ${OUT_API} | jq
