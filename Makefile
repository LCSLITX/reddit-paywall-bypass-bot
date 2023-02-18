# https://stackoverflow.com/a/43566158/15077313
SHELL := /bin/zsh

freeze:
	pip freeze | cat > requirements.txt

execute_pylint: 
	python3 -m pylint --rcfile=.pylintrc --verbose --clear-cache-post-run=y src/*.py tests/*.py

execute_tests: execute_pylint
	source .env && python3 -m pytest -vv --cache-clear --cov=. tests/*test.py

execute_bot: 
	source .env && python3 -m src.main

docker_build_image: 
	source .env && docker build -t reddit-bot .

docker_remove_bot_container:
	docker container remove $$(docker container stop BOT)

execute_container: docker_remove_bot_container docker_build_image 
	source .env && docker run -d -ti -e REDDIT_BOT_CLIENT_ID -e REDDIT_BOT_CLIENT_SECRET -e REDDIT_BOT_USERNAME -e REDDIT_BOT_PASSWORD -e REDDIT_BOT_DEBUG_MODE --name BOT reddit-bot