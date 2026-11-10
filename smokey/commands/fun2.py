import random
import requests

import discord
from discord.ext import commands


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_target(self, ctx, position=0):
        """Get a mentioned user, or resolve a supplied user ID."""
        if len(ctx.message.mentions) > position:
            return ctx.message.mentions[position]

        parts = ctx.message.content.split()
        # The command name is the first part; target IDs follow it.
        try:
            user_id = int(parts[position + 1])
            return self.bot.get_user(user_id)
        except (IndexError, ValueError, TypeError):
            return ctx.author

    @commands.command(name="8ball")
    async def eight_ball(self, ctx: commands.Context):
        parts = ctx.message.content.split(maxsplit=1)
        if len(parts) < 2:
            return await ctx.message.edit("Ask a question after the command.")

        question = parts[1]
        answers = [
            "Absolutely.", "It is certain.", "Looks likely.", "Yes.",
            "Ask again later.", "Cannot tell right now.", "Probably not.",
            "No.", "The outlook isn't great.", "Definitely not."
        ]
        await ctx.message.edit(
            f"🎱 **Question:** {question}\n"
            f"**Answer:** {random.choice(answers)}"
        )

    @commands.command()
    async def coinflip(self, ctx: commands.Context):
        result = random.choice(["Heads", "Tails"])
        await ctx.message.edit(f"🪙 It landed on **{result}**!")

    @commands.command()
    async def dice(self, ctx: commands.Context):
        parts = ctx.message.content.split()
        try:
            sides = int(parts[1]) if len(parts) > 1 else 6
        except ValueError:
            return await ctx.message.edit("Usage: dice [number of sides]")

        if not 2 <= sides <= 1000:
            return await ctx.message.edit("Choose between 2 and 1,000 sides.")

        await ctx.message.edit(
            f"🎲 You rolled **{random.randint(1, sides)}** (d{sides})."
        )

    @commands.command()
    async def roast(self, ctx: commands.Context):
        target = self.get_target(ctx)
        roasts = [
            "has the Wi-Fi signal strength of a potato.",
            "would lose a race to a loading screen.",
            "brings a spoon to a knife fight.",
            "has the strategic thinking of a broken shopping trolley.",
            "is proof that autocorrect cannot fix everything.",
            "could trip over a wireless connection."
        ]
        await ctx.message.edit(
            f"🔥 {getattr(target, 'mention', str(target))} "
            f"{random.choice(roasts)}"
        )

    @commands.command()
    async def ship(self, ctx: commands.Context):
        if len(ctx.message.mentions) < 2:
            return await ctx.message.edit(
                "Mention two users. Example: ship @user1 @user2"
            )

        first, second = ctx.message.mentions[:2]
        score = random.randint(0, 100)
        hearts = round(score / 10)
        bar = "❤️" * hearts + "🖤" * (10 - hearts)

        await ctx.message.edit(
            f"💞 **{first.display_name} + {second.display_name}**\n"
            f"{bar} **{score}%** compatibility!"
        )

    @commands.command()
    async def meme(self, ctx: commands.Context):
        try:
            response = requests.get("https://meme-api.com/gimme", timeout=12)
            response.raise_for_status()
            data = response.json()

            if data.get("nsfw"):
                return await ctx.message.edit(
                    "The meme service returned an age-restricted post, so I skipped it."
                )

            title = data.get("title") or "Random meme"
            image_url = data.get("url")
            post_url = data.get("postLink")

            if not image_url:
                return await ctx.message.edit("The meme service did not return an image.")

            await ctx.message.edit(
                f"😂 **{title}**\n{image_url}\n{post_url or ''}"
            )
        except (requests.RequestException, KeyError, ValueError) as error:
            await ctx.message.edit(f"Meme lookup failed: `{error}`")

    @commands.command()
    async def hug(self, ctx: commands.Context):
        target = self.get_target(ctx)
        hug_gifs = [
            "https://media1.tenor.com/m/l35okzAUNMgAAAAC/peach-and-goma-peachcat.gif",
            "https://media1.tenor.com/m/4-UFx3TTQK0AAAAC/november.gif",
            "https://media1.tenor.com/m/n9C4G-QEsrcAAAAC/squeeze-hug.gif",
            "https://media1.tenor.com/m/JKo6Z5x3slYAAAAC/hug-extasyxx.gif",
            "https://media1.tenor.com/m/24n__MYJspQAAAAC/hug.gif"
        ]
        await ctx.message.edit(
            f"🫂 {getattr(ctx.author, 'mention', 'Someone')} gives "
            f"{getattr(target, 'mention', str(target))} a hug!\n"
            f"{random.choice(hug_gifs)}"
        )

    @commands.command()
    async def slap(self, ctx: commands.Context):
        target = self.get_target(ctx)
        slap_gifs = [
            "https://tenor.com/bVL3e.gif",
            "https://tenor.com/h0DwLm9JkoL.gif",
            "https://tenor.com/bBKQH.gif",
            "https://tenor.com/bR6Oj.gif",
            "https://tenor.com/ptFuKOKXwCp.gif",
            "https://tenor.com/fFuVfLoRW0z.gif"
        ]
        await ctx.message.edit(
            f"👋 {getattr(ctx.author, 'mention', 'Someone')} playfully slaps "
            f"{getattr(target, 'mention', str(target))}!\n"
            f"{random.choice(slap_gifs)}"
        )

    @commands.command()
    async def cat(self, ctx: commands.Context):
        try:
            response = requests.get(
                "https://api.thecatapi.com/v1/images/search", timeout=12
            )
            response.raise_for_status()
            data = response.json()

            if not data or not data[0].get("url"):
                return await ctx.message.edit("The cat service did not return an image.")

            await ctx.message.edit(f"🐱 {data[0]['url']}")
        except (requests.RequestException, ValueError, KeyError, IndexError) as error:
            await ctx.message.edit(f"Couldn't fetch a cat right now: `{error}`")


async def setup(bot):
    await bot.add_cog(FunCommands(bot))
