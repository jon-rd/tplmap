all: test check

test:
	./tests/run_channel_test.sh
	./tests/run_java_tests.sh
	./tests/run_node_tests.sh
#	1 php test is currently failing and marked out in the test file
	./tests/run_php_tests.sh
	./tests/run_python3_tests.sh
#	12 ruby tests are currently failing
#	./tests/run_ruby_tests.sh

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
