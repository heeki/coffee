include etc/execute_env.sh

cert: cert.package cert.deploy

cert.package:
	sam package -t ${CERT_TEMPLATE} --output-template-file ${CERT_OUTPUT} --s3-bucket ${S3BUCKET}

cert.deploy:
	sam deploy -t ${CERT_OUTPUT} --stack-name ${CERT_STACK} --parameter-overrides ${CERT_PARAMS} --capabilities CAPABILITY_NAMED_IAM

domain: domain.package domain.deploy

domain.package:
	sam package -t ${DOMAIN_TEMPLATE} --output-template-file ${DOMAIN_OUTPUT} --s3-bucket ${S3BUCKET}

domain.deploy:
	sam deploy -t ${DOMAIN_OUTPUT} --stack-name ${DOMAIN_STACK} --parameter-overrides ${DOMAIN_PARAMS} --capabilities CAPABILITY_NAMED_IAM

auth: auth.package auth.deploy

auth.package:
	sam package --profile ${AUTH_PROFILE} -t ${AUTH_TEMPLATE} --output-template-file ${AUTH_OUTPUT} --s3-bucket ${AUTH_S3BUCKET}

auth.deploy:
	sam deploy --profile ${AUTH_PROFILE} -t ${AUTH_OUTPUT} --stack-name ${AUTH_STACK} --parameter-overrides ${AUTH_PARAMS} --capabilities CAPABILITY_NAMED_IAM

perm: perm.package perm.deploy

perm.package:
	sam package --profile ${PERM_PROFILE} -t ${PERM_TEMPLATE} --output-template-file ${PERM_OUTPUT} --s3-bucket ${PERM_S3BUCKET}

perm.deploy:
	sam deploy --profile ${PERM_PROFILE} -t ${PERM_OUTPUT} --stack-name ${PERM_STACK} --parameter-overrides ${PERM_PARAMS} --capabilities CAPABILITY_NAMED_IAM

perm.invoke:
	aws --profile ${PERM_PROFILE} lambda invoke --function-name ${PERM_FN} --invocation-type RequestResponse --payload file://etc/event.json --cli-binary-format raw-in-base64-out --log-type Tail tmp/fn.json | jq "." > tmp/response.json
	cat tmp/response.json | jq -r ".LogResult" | base64 --decode
