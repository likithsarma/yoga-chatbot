# Yoga Chatbot API Documentation

## Base URL
Backend service that will be integrated into the main yoga app.

## Endpoint
POST /chatbot

### Request
Content Type: application/json

Body:
{
  "question": "How often should I practice yoga?"
}

### Response
Success:
{
  "answer": "Practicing 3 to 5 days a week is ideal for flexibility and strength gains."
}

Fallback:
{
  "answer": "Try asking me about yoga routines, categories, or practice benefits."
}

## Error Codes
400 Bad Request:
- When question field is missing

500 Internal Server Error:
- When server fails to process request

## Notes for Frontend Team
- Expect a fast response within 2 seconds
- Send only message text, no formatting needed
- Chatbot only supports English questions for now
