### frontend
```npm run dev``` to run frontend

Browser
  ↓
Svelte fetch("/api/weather")

### backend
```uvicorn app.main:app --reload``` to run backend

FastAPI
  ↓
Open-Meteo API
  ↓
Aggregate rain/sun days
  ↓
Return clean JSON

Here, uvicorn is the server that runs the FastAPI app and listens on port 8000. 