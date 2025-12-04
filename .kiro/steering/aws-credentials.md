---
inclusion: always
---

# AWS Credentials Management

## Important Reminders

When working with AWS CLI commands, remember:

1. **Check for existing credentials**: Before running AWS commands, verify that AWS credentials are set in the current shell session.

2. **Prompt for credentials if needed**: If AWS commands fail with authentication errors, prompt the user to provide:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_SESSION_TOKEN (if using temporary credentials)
   - AWS_DEFAULT_REGION

3. **Reuse existing terminal sessions**: Avoid creating new terminal sessions unnecessarily, as they lose environment variables including AWS credentials.

4. **Set credentials in the current session**: When credentials are provided, set them using:
   ```powershell
   $Env:AWS_ACCESS_KEY_ID="..."
   $Env:AWS_SECRET_ACCESS_KEY="..."
   $Env:AWS_SESSION_TOKEN="..."
   $Env:AWS_DEFAULT_REGION="..."
   ```

5. **Test credentials**: After setting credentials, test them with a simple command like:
   ```powershell
   aws sts get-caller-identity
   ```

## Example Workflow

```
User: Deploy the Lambda function
Kiro: I notice we need AWS credentials. Do you have them available?
User: [provides credentials]
Kiro: [sets credentials and proceeds with deployment]
```
