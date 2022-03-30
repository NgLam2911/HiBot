from discord.ext import commands


class bot_listener(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready !")

    @commands.Cog.listener()
    async def on_message(self, message):
        if "hello" in message.content.lower():
            await message.channel.send("Hi !")
