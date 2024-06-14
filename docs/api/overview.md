# API Overview

## Endpoints

### GET /api/status
- Description: Check the status of the API.
- Response: `{ "status": "ok" }`

### POST /api/grade
- Description: Submit a student submission for grading.
- Request: `{ "submission": "text", "rubric": "criteria" }`
- Response: `{ "grade": "A", "feedback": "Well done!" }`

## Authentication

- Details on how to authenticate API requests.

## Examples

- Example API calls using `curl` or Postman.
