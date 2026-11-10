import discord
from discord.ext import commands


class ProfileCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(
            title=f"User information — {member}",
            colour=discord.Colour.green()
        )

        embed.set_thumbnail(url=member.display_avatar.url)

        embed.add_field(
            name="Username",
            value=str(member),
            inline=True
        )

        embed.add_field(
            name="User ID",
            value=str(member.id),
            inline=True
        )

        embed.add_field(
            name="Bot",
            value="Yes" if member.bot else "No",
            inline=True
        )

        embed.add_field(
            name="Created",
            value=discord.utils.format_dt(member.created_at, "D"),
            inline=False
        )

        if member.joined_at:
            embed.add_field(
                name="Joined server",
                value=discord.utils.format_dt(member.joined_at, "R"),
                inline=False
            )

        await ctx.send(embed=embed)

    @commands.command(name="avatar")
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(
            title=f"{member.display_name}'s avatar",
            colour=discord.Colour.green()
        )

        embed.set_image(
            url=member.display_avatar.with_size(1024).url
        )

        await ctx.send(embed=embed)

    @commands.command(name="banner")
    async def banner(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        user = await self.bot.fetch_user(member.id)

        if user.banner is None:
            return await ctx.send(
                "That user does not have a profile banner."
            )

        embed = discord.Embed(
            title=f"{user}'s banner",
            colour=discord.Colour.green()
        )

        embed.set_image(url=user.banner.url)

        await ctx.send(embed=embed)

    @commands.command(name="servericon")
    @commands.guild_only()
    async def servericon(self, ctx):
        if ctx.guild.icon is None:
            return await ctx.send(
                "This server does not have an icon."
            )

        embed = discord.Embed(
            title=f"{ctx.guild.name} icon",
            colour=discord.Colour.green()
        )

        embed.set_image(url=ctx.guild.icon.url)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ProfileCommands(bot))