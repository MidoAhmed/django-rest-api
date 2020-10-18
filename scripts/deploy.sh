#!/bin/bash

git config --global push.default matching
git remote add deploy ssh://momo@104.41.159.59/home/momo/bar-repository-folder/project.git
git remote show deploy
git push deploy HEAD:test2
#git push --quiet --set-upstream deploy HEAD:master
#git push --set-upstream deploy main
