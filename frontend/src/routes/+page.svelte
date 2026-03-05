<script lang="ts">
    let weatherCodes: number[] = []
    let dates: string[] = []

    async function loadWeather(latitude: number = 51.5, longitude: number = -0.12) {
        const response = await fetch(
            `http://127.0.0.1:8000/weather?latitude=${latitude}&longitude=${longitude}`
        )

        const data = await response.json()

        weatherCodes = data.weather_codes
        dates = data.dates
    }

    loadWeather()
</script>

<h1>Weather Codes</h1>

<ul>
{#each weatherCodes as code, i}
    <li>{dates[i]} : {code}</li>
{/each}
</ul>