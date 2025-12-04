from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    RemovalPolicy,
    Duration,
    CfnOutput
)
from constructs import Construct
import os

class InfrastructureStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # DynamoDB Table
        events_table = dynamodb.Table(
            self, "EventsTable",
            table_name="Events",
            partition_key=dynamodb.Attribute(
                name="eventId",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )
        
        # Lambda Function
        backend_path = os.path.join(os.path.dirname(__file__), "../../backend")
        
        api_lambda = lambda_.Function(
            self, "EventAPIFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="lambda_handler.handler",
            code=lambda_.Code.from_asset(backend_path),
            environment={
                "DYNAMODB_TABLE": events_table.table_name
            },
            timeout=Duration.seconds(30),
            memory_size=512
        )
        
        # Grant DynamoDB permissions to Lambda
        events_table.grant_read_write_data(api_lambda)
        
        # API Gateway
        api = apigateway.LambdaRestApi(
            self, "EventAPI",
            handler=api_lambda,
            proxy=True,
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=["*"]
            )
        )
        
        # Output the API URL
        CfnOutput(
            self, "APIEndpoint",
            value=api.url,
            description="Event Management API Endpoint"
        )
