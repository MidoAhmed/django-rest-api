#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

setup_git

git remote add production ssh://$USER@$HOST/$GIT_SERVER_DIR
#git remote show production
git push production main:master