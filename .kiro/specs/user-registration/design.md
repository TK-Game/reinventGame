# User Registration Feature Design

## Architecture

### Data Model

#### Users Table (DynamoDB)
- **Table Name**: Users
- **Partition Key**: userId (String)
- **Attributes**:
  - userId: String (unique identifier)
  - name: String
  - createdAt: String (ISO timestamp)

#### Registrations Table (DynamoDB)
- **Table Name**: Registrations
- **Partition Key**: eventId (String)
- **Sort Key**: userId (String)
- **Attributes**:
  - eventId: String
  - userId: String
  - status: String (registered | waitlisted)
  - registeredAt: String (ISO timestamp)
- **GSI**: UserRegistrations
  - Partition Key: userId
  - Sort Key: eventId

#### Events Table Updates
- Add fields:
  - capacity: Number (maximum attendees)
  - hasWaitlist: Boolean
  - currentRegistrations: Number

## API Endpoints

### User Management
- `POST /users` - Create user
- `GET /users/{userId}` - Get user details

### Registration Management
- `POST /events/{eventId}/register` - Register for event
  - Body: `{ "userId": "string" }`
  - Returns: 200 (registered), 200 (waitlisted), 409 (full)
  
- `DELETE /events/{eventId}/register/{userId}` - Unregister from event
  - Returns: 200 (success), 404 (not found)

- `GET /users/{userId}/events` - List user's registered events
  - Returns: List of events with registration status

## Correctness Properties

### P1: Capacity Enforcement (AC3.1, AC3.2)
For any event, the number of registered users never exceeds capacity.

### P2: Waitlist Behavior (AC3.3)
When event is full and hasWaitlist=true, new registrations are added to waitlist.

### P3: No Duplicate Registrations (AC3.4)
A user cannot be registered for the same event multiple times.

### P4: Waitlist Promotion (AC4.3)
When a user unregisters, the first waitlisted user is automatically promoted.

### P5: Data Consistency (NFR2)
Registration operations are atomic and prevent race conditions.

## Implementation Notes

### DynamoDB Operations
- Use conditional writes to prevent capacity violations
- Use transactions for unregister + promote operations
- Query GSI for user's registered events

### Error Handling
- 400: Invalid request (missing userId, invalid eventId)
- 404: User or event not found
- 409: Event full (no waitlist) or already registered
- 500: Internal server error
