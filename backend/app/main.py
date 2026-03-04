from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/weather")
async def get_weather(latitude: float, longitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "weather_code",
        "timezone": "auto",
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()  # raises if 4xx/5xx
            data = response.json()

            # Debug: print the entire response data
            for i in data:
                print(i, ":", data[i])

            weather_codes = data["daily"]["weather_code"]  # list of 7 days
            dates = data["daily"]["time"]

            # zip them together to get day-by-day data
            forecast = [
                {"date": date, "weather_code": code}
                for date, code in zip(dates, weather_codes)
            ]

            return {"forecast": forecast}

    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error: {e.response.status_code}", "detail": e.response.text}
    except KeyError as e:
        return {"error": f"Unexpected response structure, missing key: {e}", "raw": data}
    except Exception as e:
        return {"error": str(e)}