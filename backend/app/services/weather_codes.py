# This module provides a mapping from weather codes to human-readable descriptions and whether they indicate precipitation.

WEATHER_CODE_MAP = {
    0: ("Clear sky", False),
    1: ("Mainly clear", False),
    2: ("Partly cloudy", False),
    3: ("Overcast", False),
    45: ("Fog", False),
    48: ("Depositing rime fog", False),

    51: ("Light drizzle", True),
    53: ("Moderate drizzle", True),
    55: ("Dense drizzle", True),

    61: ("Slight rain", True),
    63: ("Moderate rain", True),
    65: ("Heavy rain", True),

    71: ("Slight snow", True),
    73: ("Moderate snow", True),
    75: ("Heavy snow", True),

    80: ("Rain showers", True),
    81: ("Heavy rain showers", True),
    82: ("Violent rain showers", True)
}


def decode_weather(code: int):
    return WEATHER_CODE_MAP.get(code, ("Unknown", False))