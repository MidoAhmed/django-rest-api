
SETTINGS := dev
TEST_SETTINGS := test
MANAGE=python manage.py

.PHONY: all help clean static install serve migration migrate superuser

all: help

help:
	@echo "Usage:"
	@echo "  make dev-up - start development environment"
	@echo "  make dev-down - stop development environment"
	@echo "  make clean - clean project"
	@echo "  make install - install dependencies"
	@echo "  make serve - serve the django project"
	@echo "  make migration - create migrations"
	@echo "  make migrate - run migrations"
	@echo "  make superuser - create a superuser"

dev-up:
	echo "starting development environment services..."
	docker-compose -f scripts/docker-compose-dev.yml -p django_rest_api up -d
	echo "development environment up"

dev-down:
	docker-compose -f scripts/docker-compose-dev.yml -p django_rest_api down

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf src/*.egg-info

install:
	pip install -r requirements/$(SETTINGS).txt

serve:
	$(MANAGE) runserver

migration:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

#deploy:
#	git pull --ff-only
#	$(MAKE) install
