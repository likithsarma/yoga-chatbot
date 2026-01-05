# Yoga ChatBot Design

## Overview
A retrieval based chatbot that answers yoga FAQs and guides users to video categories, payments, courses. It uses Langchain for embeddings and vector search.

## System Flow
1. User asks a question in the app
2. App sends the question to backend API
3. Chatbot converts question to embedding
4. Vector search is performed on stored FAQ data
5. Closest matching answer is returned
6. If no match found, fallback reply is given

## Architecture Components
-**API Layer** (FastAPI)
-**Landchain Embeddings**
-**Chroma Vector Store**
-**Retriever** for similarity search
-**Knowledge Base** stored in data/faq.json

## Data Source
Location: data/faq.json

Format:
[
    {"question":"","answer":""},
    ....
]

## Endpoint Design
POST /chatbot
Request:
{
    "question":"How to start yoga"
}
Response:
{
    "answer":"Start with beginner routines like Hatha yoga..."
}

## Similarity Logic
- Score based selection using cosing similarity
- Threshold based fallback message

## Performance Goals
- Response time under 2 seconds
- Support 50 requests per minute for this version

## Error Handling
- Friendly fallback message
- Logging for failed matches and errors
