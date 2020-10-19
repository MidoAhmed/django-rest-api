#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

setup_git

git remote add production ssh://momo@104.41.159.59:22/home/momo/bar-repository-folder/project
git remote show production
git push production main:master