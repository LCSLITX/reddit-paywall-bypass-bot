"""Module reddit. initialize Reddit isntance."""
import os
import praw
from src import configuration as c

reddit_instance = praw.Reddit(
    client_id=c.config.get("BOT", "REDDIT_BOT_CLIENT_ID", vars=os.environ),
    client_secret=c.config.get("BOT", "REDDIT_BOT_CLIENT_SECRET", vars=os.environ),
    username=c.config.get("BOT", "REDDIT_BOT_USERNAME", vars=os.environ),
    password=c.config.get("BOT", "REDDIT_BOT_PASSWORD", vars=os.environ),
    user_agent="USER_AGENT",
    rate_limit=300
    )
