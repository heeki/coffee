include etc/environment.sh

api: api.package api.deploy
api.package:
	sam package --profile ${PROFILE} -t ${APIGW_TEMPLATE} --output-template-file ${APIGW_OUTPUT} --s3-bucket ${S3BUCKET}
api.deploy:
	sam deploy --profile ${PROFILE} -t ${APIGW_OUTPUT} --stack-name ${APIGW_STACK} --parameter-overrides ${APIGW_PARAMS} --capabilities CAPABILITY_NAMED_IAM

api.local.invoke:
	sam local invoke -t ${APIGW_TEMPLATE} --parameter-overrides ${APIGW_PARAMS} --env-vars etc/environment.json -e etc/event_api.json Fn | jq
api.local.api:
	sam local start-api -t ${APIGW_TEMPLATE} --parameter-overrides ${APIGW_PARAMS}
api.invoke:
	aws --profile ${PROFILE1} lambda invoke --function-name ${OUT_FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode
api.curl1:
	curl -s -H "x-api-key: ${OUT_APIKEY1}" -XGET ${OUT_API1} | jq '. | {"path": .path, "httpMethod": .httpMethod, "headers": .headers, "requestContext": .requestContext, "body": .body}'
api.curl21:
	curl -s -H "x-api-key: ${OUT_APIKEY1}" -XGET ${OUT_API2} | jq '. | {"path": .path, "httpMethod": .httpMethod, "headers": .headers, "requestContext": .requestContext, "body": .body}'
api.curl22:
	curl -s -H "x-api-key: ${OUT_APIKEY2}" -XGET ${OUT_API2} | jq '. | {"path": .path, "httpMethod": .httpMethod, "headers": .headers, "requestContext": .requestContext, "body": .body}'
