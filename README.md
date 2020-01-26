# _python_flask_snake_eyes

# Extended

* FAQ page
* Test for FAQ page

# How to run tests

## Tests
`docker-compose exec website py.test snakeeyes/tests`

## Investigating our code test coverage
`docker-compose exec website py.test --cov-report term-missing --cov snakeeyes`

## Static analysis 

`docker-compose exec website flake8 .`

`docker-compose exec website flake8 . --exclude __init__.py`
