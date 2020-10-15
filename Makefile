SETTINGS := dev
TEST_SETTINGS := test
MANAGE=python manage.py
SEED_TARGET_APP?=api
SEED_NUMBER?=15


.PHONY: all help dev-up dev-down clean install installed-packages serve showmigrations makemigrations migrate superuser seed flake8 test
.DEFAULT_GOAL = help



all: help

help:
	@echo "Usage:"
	@echo "  make dev-up - start development environment"
	@echo "  make dev-down - stop development environment"
	@echo "  make clean - clean project"
	@echo "  make install - install dependencies"
	@echo "  make installed-packages - list all installed packages with their versions"
	@echo "  make serve - serve the django project"
	@echo "  make showmigrations - show migrations"
	@echo "  make makemigrations - create migrations"
	@echo "  make migrate - run migrations"
	@echo "  make superuser - create a superuser"
	@echo "  make seed SEED_TARGET_APP=? SEED_NUMBER=?  - seed your database with model instances"
	@echo "  make flake8  - run flake8"
	@echo "  make test  - run tests"

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

installed-packages:
	pip freeze

serve:
	$(MANAGE) runserver

showmigrations:
	$(MANAGE) showmigrations

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

seed:
	$(MANAGE) seed $(SEED_TARGET_APP) --number=$(SEED_NUMBER)

flake8:
	flake8

test:
	$(MANAGE) test

#deploy:
#	git pull --ff-only
#	$(MAKE) install
