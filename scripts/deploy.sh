#!/bin/bash

setup_git() {
  echo 'setup git'
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

setup_git

git remote add production ssh://momo@104.41.159.59:22/home/momo/bar-repository-folder/project.git
git remote show production

git fetch --unshallow origin
git fetch --unshallow production
git push production HEAD:refs/heads/main