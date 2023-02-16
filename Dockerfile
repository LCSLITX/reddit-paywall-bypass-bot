FROM python:3.9-alpine AS build
WORKDIR /reddit-paywall-bypass-bot
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "-m", "src.main"]