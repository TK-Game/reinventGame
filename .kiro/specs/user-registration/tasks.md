# User Registration Implementation Tasks

## Task 1: Update Infrastructure (CDK)
**Properties**: P1, P2, P3, P4, P5
**Acceptance Criteria**: AC2.1, AC2.2, AC2.3

Create DynamoDB tables and update Events table schema.

### Subtasks:
- [ ] Create Users table in CDK stack
- [ ] Create Registrations table with GSI in CDK stack
- [ ] Update Events table to add capacity, hasWaitlist, currentRegistrations fields
- [ ] Deploy infrastructure changes

## Task 2: Implement User Management API
**Properties**: None (foundational)
**Acceptance Criteria**: AC1.1, AC1.2, AC1.3

Create endpoints for user creation and retrieval.

### Subtasks:
- [ ] Add POST /users endpoint with validation
- [ ] Add GET /users/{userId} endpoint
- [ ] Add User model with Pydantic validation
- [ ] Update Lambda handler with new routes

## Task 3: Implement Event Registration Logic
**Properties**: P1, P2, P3
**Acceptance Criteria**: AC3.1, AC3.2, AC3.3, AC3.4

Core registration functionality with capacity and waitlist handling.

### Subtasks:
- [ ] Add POST /events/{eventId}/register endpoint
- [ ] Implement capacity check logic
- [ ] Implement waitlist logic when event is full
- [ ] Add duplicate registration prevention
- [ ] Update event currentRegistrations counter

## Task 4: Implement Unregistration with Waitlist Promotion
**Properties**: P4, P5
**Acceptance Criteria**: AC4.1, AC4.2, AC4.3

Unregister users and promote from waitlist.

### Subtasks:
- [ ] Add DELETE /events/{eventId}/register/{userId} endpoint
- [ ] Implement unregister logic with capacity update
- [ ] Implement waitlist promotion (move first waitlisted to registered)
- [ ] Use DynamoDB transactions for atomicity

## Task 5: Implement User Events Listing
**Properties**: None (read-only)
**Acceptance Criteria**: AC5.1, AC5.2, AC5.3

Allow users to view their registered events.

### Subtasks:
- [ ] Add GET /users/{userId}/events endpoint
- [ ] Query Registrations GSI by userId
- [ ] Fetch event details for each registration
- [ ] Return combined data with registration status
