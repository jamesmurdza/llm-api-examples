## OpenAI

### Chat
```bash
curl "https://api.openai.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You will be provided with statements, and your task is to convert them to standard English."
    },
    {
      "role": "user",
      "content": "She no went to the market."
    }
  ],
  "temperature": 0.7,
  "max_tokens": 64,
  "top_p": 1
}'
```

### Embeddings
```bash
curl "https://api.openai.com/v1/embeddings" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "The food was delicious and the waiter...",
    "model": "text-embedding-ada-002",
    "encoding_format": "float"
  }'
```

## Mistral

### Chat
```bash
curl "https://api.mistral.ai/v1/chat/completions" \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -H "Authorization: Bearer $MISTRAL_API_KEY" \
     -d '{
    "model": "mistral-tiny",
    "messages": [{"role": "user", "content": "Who is the most renowned French painter?"}]
  }'
```

### Embeddings
```bash
curl "https://api.mistral.ai/v1/embeddings" \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -H "Authorization: Bearer $MISTRAL_API_KEY" \
     -d '{
    "model": "mistral-embed",
    "input": ["Embed this sentence.", "As well as this one."]
  }'
```
