# Set-ExecutionPolicy Restricted
from programy.clients import CommandLineBot

bot = CommandLineBot()
bot.load_configuration("config/config.config.yaml")
bot.run()
