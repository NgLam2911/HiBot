import discord
from discord.ext import commands
from bot_constant import bot_constant


class command_handler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hi !")

    @commands.command()
    async def sum(self, ctx, numOne: int, numTwo: int):
        await ctx.send(numOne + numTwo)

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="NgBot", description="Bot infomation", color=discord.Color.green())
        embed.add_field(name="Version", value=bot_constant.bot_version)
        embed.add_field(name="Author", value=bot_constant.bot_author)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        ctx.send("Pong :>")
