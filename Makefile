.PHONY: init ci analyze build rebuild migrate lang-make lang-compile

init:
	curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
	poetry install
ci:
	pytest --cov=./
analyze:
	pipenv run flake8 .
	pipenv run isort -v
build:
	docker-compose build
rebuild:
	docker-compose build --force-rm --no-cache
migrate:
	docker-compose run --rm web python manage.py migrate
lang-make:
	pipenv run python manage.py makemessages --no-location --no-wrap
lang-compile:
	pipenv run python manage.py compilemessages
