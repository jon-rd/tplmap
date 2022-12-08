all: test check

test:
	poetry run pytest ./tests

## CHECK
#
#
check: check_flake

check_flake:
	poetry run flake8 ./tplmap ./tests

## FIX
#
#
fix:
	poetry run autoflake --in-place --remove-unused-variables --recursive ./tplmap ./tests
	poetry run isort ./tplmap ./tests
	poetry run black ./tplmap ./tests

.PHONY: test check_flake fix
