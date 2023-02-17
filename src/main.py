"""Module main. Checks for debug mode variable and executes handle_stream function."""
import os
from src import bot
from src import utils
from src import configuration as c


debug_mode = c.config.get("DEFAULT", "REDDIT_BOT_DEBUG_MODE", vars=os.environ)
print("REDDIT_BOT_DEBUG_MODE:", debug_mode)
if debug_mode == "True":
    utils.debug_mode()


bot.handle_stream()
