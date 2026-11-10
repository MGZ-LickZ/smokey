import discord
from discord.ext import commands
import requests
from urllib.parse import quote


class LookupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="weather")
    async def weather(self, ctx, *, city: str):
        try:
            geo_url = (
                "https://geocoding-api.open-meteo.com/v1/search?name="
                + quote(city) + "&count=1&language=en&format=json"
            )

            geo_response = requests.get(geo_url, timeout=12)
            geo_response.raise_for_status()

            places = geo_response.json().get("results") or []

            if not places:
                return await ctx.send(f"I couldn't find **{city}**.")

            place = places[0]

            weather_url = (
                "https://api.open-meteo.com/v1/forecast"
                f"?latitude={place['latitude']}&longitude={place['longitude']}"
                "&current=temperature_2m,relative_humidity_2m,apparent_temperature,"
                "precipitation,wind_speed_10m"
            )

            response = requests.get(weather_url, timeout=12)
            response.raise_for_status()

            current = response.json().get("current", {})

            embed = discord.Embed(
                title=f"Weather — {place['name']}, {place.get('country', '')}",
                colour=discord.Colour.green()
            )

            embed.add_field(
                name="Temperature",
                value=f"{current.get('temperature_2m', 'N/A')}°C"
            )

            embed.add_field(
                name="Feels like",
                value=f"{current.get('apparent_temperature', 'N/A')}°C"
            )

            embed.add_field(
                name="Humidity",
                value=f"{current.get('relative_humidity_2m', 'N/A')}%"
            )

            embed.add_field(
                name="Wind",
                value=f"{current.get('wind_speed_10m', 'N/A')} km/h"
            )

            embed.add_field(
                name="Precipitation",
                value=f"{current.get('precipitation', 'N/A')} mm"
            )

            await ctx.send(embed=embed)

        except (requests.RequestException, KeyError, ValueError) as error:
            await ctx.send(f"Weather lookup failed: `{error}`")

    @commands.command(name="translate")
    async def translate(self, ctx, language: str, *, text: str):
        """Example: .translate es Hello, how are you?"""

        try:
            url = (
                "https://api.mymemory.translated.net/get?q=" + quote(text)
                + "&langpair=en|" + quote(language)
            )

            response = requests.get(url, timeout=12)
            response.raise_for_status()

            translated = response.json().get(
                "responseData", {}
            ).get("translatedText")

            if not translated:
                return await ctx.send(
                    "I couldn't get a translation for that text."
                )

            await ctx.send(
                f"**Translation ({language}):** {translated[:1900]}"
            )

        except requests.RequestException as error:
            await ctx.send(f"Translation failed: `{error}`")


async def setup(bot):
    await bot.add_cog(LookupCommands(bot))