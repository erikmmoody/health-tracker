import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk import SecretValue

# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

#{"github-token":"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"}
class PipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        github_access_token = SecretValue.secrets_manager("github-token")
        print(f"token json {github_access_token.to_json()}")
        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="HealthTrackerPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub("erikmmoody/health-tracker", "master", authentication=github_access_token),
                commands=["npm install -g aws-cdk",
                          "python -m pip install -r requirements.txt",
                          "cdk synth"]
            ),
        )