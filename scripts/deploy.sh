#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

setup_git

#
#git remote add production ssh://momo@104.41.159.59:22/home/momo/bar-repository-folder/project
#git remote show production
#git fetch --unshallow production
#git push production main:refs/heads/master

pwd
#scp -r scripts momo@104.41.159.59:~/.
cd ..
pwd
git clone ssh://momo@104.41.159.59/~/git/djangoRestApi.git testproject
ls
cd testproject
git status
touch test.txt
git add .
git commit 'init commit'
git push origin master

