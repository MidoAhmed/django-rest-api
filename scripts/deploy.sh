#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.com"
  git config --global user.name "Travis CI"
}

setup_git

# Remove existing "origin"
git remote rm origin
# Add new "origin"
git remote add origin ssh://momo@104.41.159.59:22/home/momo/bar-repository-folder/project.git > /dev/null 2>&1
echo '---------'
git branch
git branch -r
git remote set-head origin master
echo '---------'
git push -u origin main:master --quiet