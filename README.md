# Paywall Bypass BOT

This project is a BOT for [Reddit](https://www.reddit.com).

It is supposed to reply to all [mentions to its username](https://www.reddit.com/r/announcements/comments/1erzth/new_reddit_gold_feature_orangereds_when_your/) with links provided to bypass paywalls from news or articles links contained within the parent submission or comment. More explanations further.

It was developed using Python and [Python Reddit API Wrapper](https://praw.readthedocs.io/en/stable/).

Deployed without any cost using [Fly.io](https://fly.io).


## Development Initialization

You need to edit `.example.env` file to change environment variables. Check how acquire a `client_id` or `client_secret` [here](https://praw.readthedocs.io/en/stable/getting_started/authentication.html).

You could also set `DEBUG_MODE` to `True` to log info on console.

After editing, use the command `source .example.env`.

Then you could run a BOT container using the following command:
```
docker compose up
```


## Usage

It may be used by mentioning the user `PaywallBypassBOT` (just like this: [u/PaywallBypassBOT](https://www.reddit.com/user/PaywallBypassBOT)), in two ways:

1. In any top-level comment (comments that directly replies to a submission, also called post or thread). Bot will then check for links within the `POST text`, `POST title` and `POST url` if its the case;


2. In any comment that replies another comment. Bot will then check for links within the `PARENT COMMENT text`.

