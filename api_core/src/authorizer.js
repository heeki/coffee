let simple = process.env.SIMPLE_RESPONSE;

exports.handler =  function(event, context, callback) {
    console.log(JSON.stringify(event));
    var token = event.headers.authorization;
    var context = {};
    context.simple = simple;
    context.token = token;
    context.pversion = event.version;
    var resource = '';
    if ('methodArn' in event) {
        resource = event.methodArn;
    } else if (event.version == '2.0' && 'routeArn' in event) {
        resource = event.routeArn + '/*';
    }
    switch (token) {
        case 'allow':
            context.reason = 'generating allow policy'
            callback(null, generatePolicy('user', 'Allow', resource, context));
            break;
        case 'deny':
            context.reason = 'generating deny policy';
            callback(null, generatePolicy('user', 'Deny', resource, context));
            break;
        default:
            context.reason = 'invalid token provided';
            callback(null, generatePolicy('user', 'Deny', resource, context));
    }
};

var generatePolicy = function(principalId, effect, resource, context) {
    var authResponse = {};
    if (simple == "true") {
        switch (effect) {
            case 'Allow':
                authResponse.isAuthorized = true;
                break;
            case 'Deny':
                authResponse.isAuthorized = false;
                break;
            default:
                authResponse.isAuthorized = false;
                break;
        }
    } else {
        authResponse.principalId = principalId;
        if (effect && resource) {
            var policyDocument = {};
            policyDocument.Version = '2012-10-17'; 
            policyDocument.Statement = [];
            var statementOne = {};
            statementOne.Action = 'execute-api:Invoke'; 
            statementOne.Effect = effect;
            statementOne.Resource = resource;
            policyDocument.Statement[0] = statementOne;
            authResponse.policyDocument = policyDocument;
        }
    }
    authResponse.context = context;
    console.log(JSON.stringify(authResponse));
    return authResponse;
}