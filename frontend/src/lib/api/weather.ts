export async function fetchWeather(latitude: number, longitude: number) {
    const response = await fetch(
        `http://127.0.0.1:8000/weather?latitude=${latitude}&longitude=${longitude}`
    )

    if (!response.ok) {
        throw new Error("Failed to fetch weather")
    }

    return response.json()
}