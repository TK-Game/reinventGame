# Event Management Backend API

FastAPI-based REST API for managing events, deployed as an AWS Lambda function.

## Features

- RESTful API with FastAPI
- DynamoDB for data persistence
- CORS enabled for web applications
- Comprehensive error handling
- Input validation with Pydantic

## Event Schema

```json
{
  "eventId": "string (UUID or custom)",
  "title": "string",
  "description": "string",
  "date": "string (YYYY-MM-DD)",
  "location": "string",
  "capacity": "integer",
  "organizer": "string",
  "status": "string (active|cancelled|completed)"
}
```

## API Endpoints

### List Events
```
GET /events
GET /events?status=active
```
Returns a list of all events or filtered by status.

### Create Event
```
POST /events
Content-Type: application/json

{
  "eventId": "optional-custom-id",
  "title": "Event Title",
  "description": "Event description",
  "date": "2024-12-15",
  "location": "Event Location",
  "capacity": 100,
  "organizer": "Organizer Name",
  "status": "active"
}
```
Returns: 201 Created

### Get Event
```
GET /events/{eventId}
```
Returns: 200 OK with event details

### Update Event
```
PUT /events/{eventId}
Content-Type: application/json

{
  "title": "Updated Title",
  "capacity": 150
}
```
Returns: 200 OK with updated event

### Delete Event
```
DELETE /events/{eventId}
```
Returns: 204 No Content

## Local Development

### Setup

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Generate Documentation

```bash
pip install pdoc
pdoc lambda_handler_simple.py -o docs/
```

## Deployment

The backend is deployed as an AWS Lambda function behind API Gateway. See the infrastructure folder for deployment details.

## Environment Variables

- `DYNAMODB_TABLE`: Name of the DynamoDB table (default: "Events")
