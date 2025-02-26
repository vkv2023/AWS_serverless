import aws_cdk as core
import aws_cdk.assertions as assertions

from apigw_lambda_bedrock_s3_imaging.apigw_lambda_bedrock_s3_imaging_stack import ApigwLambdaBedrockS3ImagingStack

# example tests. To run these tests, uncomment this file along with the example
# resource in apigw_lambda_bedrock_s3_imaging/apigw_lambda_bedrock_s3_imaging_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApigwLambdaBedrockS3ImagingStack(app, "apigw-lambda-bedrock-s3-imaging")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
