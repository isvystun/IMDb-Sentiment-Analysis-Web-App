import boto3

def lambda_handler(event, context):

    runtime = boto3.Session().client('sagemaker-runtime')

    # Now we use the SageMaker runtime to invoke our endpoint, sending the review we were given
    # response = runtime.invoke_endpoint(EndpointName = '**ENDPOINT NAME HERE**',    # The name of the endpoint we created
    #                                    ContentType = 'text/plain',                 # The data format that is expected
    #                                    Body = event['body'])                       # The actual review
    response = runtime.invoke_endpoint(EndpointName = 'sagemaker-pytorch-2021-06-26-06-36-48-004',
                                       ContentType = 'text/plain',                
                                       Body = event['body'])  

    result = response['Body'].read().decode('utf-8')

    return {
        'statusCode' : 200,
        'headers' : { 'Content-Type' : 'text/plain', 'Access-Control-Allow-Origin' : '*' },
        'body' : result
    }