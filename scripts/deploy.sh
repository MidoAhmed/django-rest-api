#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

setup_git

# Remove existing "origin"
git remote rm origin
# Add new "origin"
git remote add origin ssh://momo@104.41.159.59:22/home/momo/bar-repository-folder/project.git > /dev/null 2>&1
git branch
git push origin main:master --quiet