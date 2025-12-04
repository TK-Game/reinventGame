---
inclusion: always
---

# Documentation and Best Practices

## Always Check Documentation

When working with libraries, frameworks, or AWS services:

1. **Check official documentation** for the latest APIs, best practices, and examples
2. **Verify syntax and patterns** especially for:
   - FastAPI and Pydantic (note: `pattern` instead of `regex` in recent versions)
   - AWS CDK constructs and properties
   - AWS SDK (boto3) methods and parameters
   - DynamoDB operations and reserved keywords

3. **Use web search** when uncertain about:
   - Current version compatibility
   - Breaking changes in recent releases
   - Common pitfalls and solutions
   - Community best practices

4. **Prefer official sources**:
   - FastAPI: https://fastapi.tiangolo.com/
   - Pydantic: https://docs.pydantic.dev/
   - AWS CDK: https://docs.aws.amazon.com/cdk/
   - boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/

## When to Check

- Before implementing new features
- When encountering errors or unexpected behavior
- When using unfamiliar APIs or services
- When updating dependencies or versions
