from discord.ext import commands
from bot_constant import bot_constant
from command_handler import command_handler
from bot_listener import bot_listener


class bot_manager:

    def __init__(self):
        self.bot = commands.Bot(command_prefix=bot_constant.bot_prefix, description=bot_constant.bot_description)
        self.command_handler = command_handler(self.bot)
        self.bot.add_cog(self.command_handler)

        self.bot_listener = bot_listener()
        self.bot.add_cog(self.bot_listener)
        self.start_bot()

    def start_bot(self) -> None:
        self.bot.run(bot_constant.bot_token)

    def get_command_handler(self) -> command_handler:
        return self.command_handler

    def get_bot_listener(self) -> bot_listener:
        return self.bot_listener

    def get_bot(self) -> commands.Bot:
        return self.bot
