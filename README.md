# Project

This project contains:

- **backend/**: FastAPI Python backend application
- **infrastructure/**: AWS CDK Infrastructure as Code

## Structure

```
.
├── backend/              # FastAPI application
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── infrastructure/       # CDK project
│   ├── app.py
│   ├── cdk.json
│   ├── requirements.txt
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── infrastructure_stack.py
│   └── README.md
└── .kiro/               # Kiro workspace configuration
    └── settings/
        └── mcp.json
```
