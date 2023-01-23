import aws_cdk as core
import aws_cdk.assertions as assertions

from health_tracker.health_tracker_stack import HealthTrackerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in health_tracker/health_tracker_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HealthTrackerStack(app, "health-tracker")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
