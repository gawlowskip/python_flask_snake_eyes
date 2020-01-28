# _python_flask_snake_eyes

# Extended

* FAQ page
* Test for FAQ page
* Custom CLI command `hello`
* Feedback page
* Tests for Feedback page and tasks

# How to run tests

## Tests
`docker-compose exec website py.test snakeeyes/tests`

## Investigating our code test coverage
`docker-compose exec website py.test --cov-report term-missing --cov snakeeyes`

## Static analysis with Flake8

`docker-compose exec website flake8 .`

`docker-compose exec website flake8 . --exclude __init__.py`

# CLI

## List of all commands

`docker-compose exec website snakeeyes`

## Static analysis with Flake8

`docker-compose exec website snakeeyes flake8`

`docker-compose exec website snakeeyes flake8 --help`

`docker-compose exec website snakeeyes flake8 --no-skip-init`

## Generate fake data

List of all commands 

`docker-compose exec website snakeeyes add`

Generate fake Users

`docker-compose exec website snakeeyes add users`

Generate all data

`docker-compose exec website snakeeyes add all`

# Database

Run PostgreSQL related tasks

`docker-compose exec website snakeeyes db`

Initialize the database

`docker-compose exec website snakeeyes db init`

Init and seed automatically 

`docker-compose exec website snakeeyes db reset`

Seed the database with an initial user

`docker-compose exec website snakeeyes db seed`
