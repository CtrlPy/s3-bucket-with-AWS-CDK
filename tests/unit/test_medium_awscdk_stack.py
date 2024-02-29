import aws_cdk as core
import aws_cdk.assertions as assertions

from medium_awscdk.medium_awscdk_stack import MediumAwscdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in medium_awscdk/medium_awscdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MediumAwscdkStack(app, "medium-awscdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
