---
inclusion: fileMatch
fileMatchPattern: '(main|handler|api|routes|endpoints)\.py$'
---

# API Standards and Best Practices

This document defines the REST API standards and conventions for this project.

## HTTP Methods

- **GET**: Retrieve resources (read-only, idempotent)
- **POST**: Create new resources
- **PUT**: Update existing resources (full update)
- **PATCH**: Partially update existing resources
- **DELETE**: Remove resources

## HTTP Status Codes

### Success Codes
- **200 OK**: Successful GET, PUT, PATCH, or DELETE
- **201 Created**: Successful POST that creates a resource
- **204 No Content**: Successful DELETE with no response body

### Client Error Codes
- **400 Bad Request**: Invalid request format or missing required fields
- **404 Not Found**: Resource does not exist
- **409 Conflict**: Resource conflict (e.g., duplicate)
- **422 Unprocessable Entity**: Validation errors

### Server Error Codes
- **500 Internal Server Error**: Unexpected server error

## JSON Response Format

### Success Response
```json
{
  "data": { ... },
  "message": "Optional success message"
}
```

For list endpoints:
```json
{
  "data": [ ... ],
  "count": 10,
  "message": "Optional message"
}
```

### Error Response
```json
{
  "error": "Error message describing what went wrong",
  "code": "ERROR_CODE",
  "details": { ... }
}
```

## REST API Conventions

1. **Resource Naming**: Use plural nouns for collections (e.g., `/events`, `/users`)
2. **URL Structure**: Keep URLs simple and hierarchical
   - Collection: `GET /events`
   - Single resource: `GET /events/{id}`
   - Nested resources: `GET /events/{id}/attendees`

3. **Query Parameters**: Use for filtering, sorting, and pagination
   - Filtering: `GET /events?status=active`
   - Sorting: `GET /events?sort=date`
   - Pagination: `GET /events?page=1&limit=20`

4. **Request Body**: Use JSON for POST, PUT, and PATCH requests

5. **CORS**: Enable CORS headers for web applications
   ```
   Access-Control-Allow-Origin: *
   Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
   Access-Control-Allow-Headers: Content-Type, Authorization
   ```

6. **Error Handling**: Always return appropriate status codes and descriptive error messages

7. **Validation**: Validate all input data before processing
   - Required fields must be present
   - Data types must match expected types
   - Constraints (min/max length, ranges) must be enforced

8. **Idempotency**: GET, PUT, and DELETE should be idempotent

## DynamoDB Considerations

When working with DynamoDB:
- Use ExpressionAttributeNames for reserved keywords (e.g., `status`, `capacity`, `date`)
- Handle Decimal types properly in JSON responses
- Implement proper error handling for DynamoDB operations

## Example Implementation

```python
# Good: Proper status code and error handling
@app.post("/events", status_code=201)
async def create_event(event: Event):
    try:
        # Validate and create event
        return {"data": event_data}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

# Good: Proper filtering with query parameters
@app.get("/events")
async def list_events(status: Optional[str] = None):
    if status:
        # Filter by status
        pass
    return {"data": events}
```
