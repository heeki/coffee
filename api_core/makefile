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
