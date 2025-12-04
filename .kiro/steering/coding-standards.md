---
inclusion: always
---

# General Coding Standards

## Python Code Style

1. **Follow PEP 8**: Use consistent naming conventions and formatting
2. **Type Hints**: Use type hints for function parameters and return values
3. **Docstrings**: Add docstrings for modules, classes, and functions
4. **Error Handling**: Use try-except blocks with specific exception types
5. **Logging**: Use proper logging instead of print statements in production code

## Code Organization

1. **Keep functions focused**: Each function should do one thing well
2. **Avoid deep nesting**: Refactor complex nested logic into separate functions
3. **Use meaningful names**: Variables and functions should have descriptive names
4. **Constants**: Use UPPER_CASE for constants
5. **Magic numbers**: Avoid magic numbers; use named constants

## Testing Considerations

1. **Write testable code**: Design functions to be easily testable
2. **Separate concerns**: Keep business logic separate from infrastructure code
3. **Mock external dependencies**: Use mocks for AWS services, databases, etc.

## Security Best Practices

1. **Never commit secrets**: Use environment variables for sensitive data
2. **Validate input**: Always validate and sanitize user input
3. **Use parameterized queries**: Prevent injection attacks
4. **Principle of least privilege**: Grant minimal necessary permissions

## Performance

1. **Avoid unnecessary operations**: Check if work needs to be done before doing it
2. **Use appropriate data structures**: Choose the right data structure for the task
3. **Cache when appropriate**: Cache expensive operations when possible
4. **Batch operations**: Batch DynamoDB operations when possible

## Comments

1. **Explain why, not what**: Code should be self-explanatory; comments explain reasoning
2. **Keep comments updated**: Update comments when code changes
3. **Avoid obvious comments**: Don't comment on self-evident code
