// A simple token-based authorizer example to demonstrate how to use an authorization token 
// to allow or deny a request. In this example, the caller named 'user' is allowed to invoke 
// a request if the client-supplied token value is 'allow'. The caller is not allowed to invoke 
// the request if the token value is 'deny'. If the token value is 'unauthorized' or an empty
// string, the authorizer function returns an HTTP 401 status code. For any other token value, 
// the authorizer returns an HTTP 500 status code. 
// Note that token values are case-sensitive.

exports.handler =  function(event, context, callback) {
    console.log(JSON.stringify(event));
    var token = event.headers.authorization;
    var context = {};
    context.token = token;
    switch (token) {
        case 'allow':
            callback(null, generatePolicy('user', 'Allow', event.routeArn, context));
            break;
        case 'deny':
            context.reason = 'deny';
            callback(null, generatePolicy('user', 'Deny', event.routeArn, context));
            break;
        default:
            context.reason = 'invalid';
            callback(null, generatePolicy('user', 'Deny', event.routeArn, context));
    }
};

var generatePolicy = function(principalId, effect, resource, context) {
    var authResponse = {};
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
    authResponse.context = context;
    console.log(JSON.stringify(authResponse));
    return authResponse;
}