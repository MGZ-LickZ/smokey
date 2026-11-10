import discord
from discord.ext import commands
import asyncio
import time

import config_selfbot
from utils import lang, random_cooldown


class UtilsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sniped_messages = {}

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return

        try:
            attachments_urls = [
                attachment.url for attachment in message.attachments
            ]

            self.sniped_messages[message.channel.id] = {
                "author": message.author,
                "content": message.content,
                "images": attachments_urls if attachments_urls else None,
                "time": round(time.time())
            }

        except Exception:
            return

    @commands.command(name="snipe")
    async def snipe(self, ctx):
        sniped_message = self.sniped_messages.get(ctx.channel.id)

        if not sniped_message:
            return await ctx.send("There are no recently deleted messages to show.")

        images_text = (
            ", ".join(sniped_message["images"])
            if sniped_message["images"]
            else "None"
        )

        embed = discord.Embed(
            title="🔫 Sniped Message",
            colour=discord.Colour.green()
        )

        embed.add_field(
            name="Author",
            value=str(sniped_message["author"]),
            inline=False
        )

        embed.add_field(
            name="Message",
            value=sniped_message["content"] or "No text content",
            inline=False
        )

        embed.add_field(
            name="Images",
            value=images_text[:1000],
            inline=False
        )

        embed.add_field(
            name="Deleted",
            value=f"<t:{sniped_message['time']}:R>",
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.command(name="clear")
    async def clear(self, ctx, amount: int = 19):
        if amount < 1 or amount > 100:
            return await ctx.send("Choose an amount between 1 and 100.")

        deleted = 0

        async for message in ctx.channel.history(limit=amount + 1):
            if message.author.id == self.bot.user.id:
                try:
                    await message.delete()
                    deleted += 1
                    await asyncio.sleep(random_cooldown(0.4, 1))
                except discord.HTTPException:
                    continue

        await ctx.send(f"Cleared {deleted} of my own messages.", delete_after=5)

    @commands.command(name="ping")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latency: **{latency}ms**",
            colour=discord.Colour.green()
        )

        await ctx.send(embed=embed)

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        user = await self.bot.fetch_user(member.id)

        roles = [
            role.name
            for role in member.roles[1:]
            if role.name != "@everyone"
        ] if isinstance(member, discord.Member) else []

        embed = discord.Embed(
            title=f"User information — {user}",
            colour=discord.Colour.green()
        )

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(
            name="Global name",
            value=user.global_name or "None",
            inline=True
        )

        embed.add_field(
            name="Username",
            value=user.name,
            inline=True
        )

        embed.add_field(
            name="User ID",
            value=str(user.id),
            inline=True
        )

        embed.add_field(
            name="Created",
            value=discord.utils.format_dt(user.created_at, "F"),
            inline=False
        )

        embed.add_field(
            name="Banner",
            value="[View banner](" + user.banner.url + ")" if user.banner else "None",
            inline=True
        )

        embed.add_field(
            name="Avatar",
            value=f"[View avatar]({user.display_avatar.url})",
            inline=True
        )

        if roles:
            embed.add_field(
                name="Roles",
                value=", ".join(roles)[:1000],
                inline=False
            )

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(UtilsCommands(bot))