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

## Stripe

Sync Stripe plans

`docker-compose exec website snakeeyes stripe sync_plans`

List of all Stripe plans

`docker-compose exec website snakeeyes stripe list_plans`

Delete plan by id

`docker-compose exec website snakeeyes stripe delete_plans bronze`

## Others

Generate secure token, by default 128 bytes

`docker-compose exec website snakeeyes secret`

Generate secure token, e.g 64 bytes

`docker-compose exec website snakeeyes secret 64`

List all of the available routes

`docker-compose exec website snakeeyes routes`

Lines of code

`docker-compose exec website snakeeyes loc`

# Database

Run PostgreSQL related tasks

`docker-compose exec website snakeeyes db`

Initialize the database

`docker-compose exec website snakeeyes db init`

Init and seed automatically 

`docker-compose exec website snakeeyes db reset`

`docker-compose exec website snakeeyes db reset --with-testdb`

Seed the database with an initial user

`docker-compose exec website snakeeyes db seed`

# ngrok (for Stripe Webhooks)

ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels.

## Download 

https://ngrok.com/download

## Run

Download and run `ngrok http localhost:8888`, then you will see Session Status and section forwarding e.g. http://4d5edf40.ngrok.io

Add to SERVER_NAME variable in `./instance/setting.py` without `http://` or `https://`.
