
SETTINGS := dev
TEST_SETTINGS := test


docker-compose-up:
	docker-compose -f scripts/docker-compose-dev.yml -p django_rest_api up -d

docker-compose-down:
	docker-compose -f scripts/docker-compose-dev.yml -p django_rest_api down

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf src/*.egg-info


pip:
	pip install -r requirements/$(SETTINGS).txt

