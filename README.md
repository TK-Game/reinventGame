# Event Management API

A serverless event management system built with FastAPI, AWS Lambda, API Gateway, and DynamoDB.

## Project Structure

```
.
├── backend/              # FastAPI application
│   ├── main.py          # FastAPI application (for local development)
│   ├── lambda_handler_simple.py  # Lambda handler
│   ├── requirements.txt
│   ├── docs/            # API documentation
│   └── README.md
├── infrastructure/       # AWS CDK Infrastructure as Code
│   ├── app.py
│   ├── cdk.json
│   ├── requirements.txt
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── infrastructure_stack.py
│   └── README.md
├── cloudformation-template.yaml  # SAM template
└── .kiro/               # Kiro workspace configuration
    └── settings/
        └── mcp.json
```

## Features

- **CRUD Operations**: Create, Read, Update, and Delete events
- **DynamoDB Storage**: Persistent event storage with DynamoDB
- **Serverless Architecture**: AWS Lambda + API Gateway for scalability
- **CORS Support**: Full CORS configuration for web applications
- **Query Filtering**: Filter events by status
- **Error Handling**: Comprehensive error handling and validation

## API Endpoints

- `GET /events` - List all events
- `GET /events?status=active` - Filter events by status
- `POST /events` - Create a new event
- `GET /events/{eventId}` - Get a specific event
- `PUT /events/{eventId}` - Update an event
- `DELETE /events/{eventId}` - Delete an event

## Deployed API

**Endpoint**: `https://n0oxmp7oui.execute-api.us-west-2.amazonaws.com/prod/`

## Quick Start

### Prerequisites

- Python 3.12+
- AWS CLI configured
- Node.js and npm (for CDK)

### Local Development

See [backend/README.md](backend/README.md) for detailed setup instructions.

### Deployment

See [infrastructure/README.md](infrastructure/README.md) for deployment instructions.

## Documentation

API documentation is available in the `backend/docs/` folder.
