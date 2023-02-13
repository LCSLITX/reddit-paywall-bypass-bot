# Bypass Paywall BOT

This project is a BOT for [Reddit](https://www.reddit.com). It is supposed to reply mentions with links provided by some paywall bypassing providers to make it easier to fully access news from reddit app or site.

It was developed with Python and PRAW ([Python Reddit API Wrapper](https://praw.readthedocs.io/en/stable/)).


## Development Initialization

You need to setup the environment variables contained in `.example.env` file and rename it to `.env`.

Then you could run a BOT container using the following command:
```
docker compose up
```


## Production Usage
It may be used by mentioning the user `BypassPaywall` (just like this: [u/BypassPaywall](https://www.reddit.com/user/BypassPaywall)), in two ways:
1. In any top-level comment (comments that directly replies to a post/thread/submission). The bot will then check for links within the `POST text` or `url`;


2. In any comment that replies another comment. The bot will then check for links within the `parent comment text`.

