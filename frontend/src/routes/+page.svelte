<script lang="ts">
    import { fetchWeather } from "$lib/api/weather"

    let weatherCodes: number[] = []
    let dates: string[] = []
    let precipitation: boolean[] = []

    let latitude: number
    let longitude: number

    let loading = false
    let error: string | null = null

    async function loadWeather(lat: number, lon: number) {
        loading = true
        error = null

        try {
            const data = await fetchWeather(lat, lon)

            weatherCodes = data.weather_codes
            dates = data.dates
            precipitation = data.precipitation

        } catch (err) {
            error = "Could not load weather data"
        } finally {
            loading = false
        }
    }
</script>

<h1>Weather Codes</h1>
<p>Displays the weather for the past 6 days</p>
<label>
Latitude:
<input type="number" bind:value={latitude} step="0.01" />
</label>

<label>
Longitude:
<input type="number" bind:value={longitude} step="0.01" />
</label>

<button onclick={() => loadWeather(latitude, longitude)} disabled={loading}>
Load Weather
</button>

{#if loading}
<p>Loading weather...</p>

{:else if error}
<p>{error}</p>

{:else if weatherCodes.length > 0}
<ul>
{#each weatherCodes as code, i}
    <li class={precipitation[i] ? "rain" : "norain"}>{dates[i]} : {code}</li>
{/each}
</ul>
{/if}

<style>
p {
    color: burlywood;
}

h1 {
    font-size: 2em;
}

button {
    margin-top: 1em;
    padding: 0.5em 1em;
    font-size: 1em;
    background-color: #279c6f;
}
button:active {
    background-color: #1e6b4a;
    transform: translateY(4px);
}

.rain {
    color: rgb(67, 167, 255);
}

.norain {
    color: rgb(11, 128, 0);
}
</style>