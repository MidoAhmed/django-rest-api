#!/bin/bash

git remote add deploy ssh://momo@104.41.159.59/home/momo/bar-repository-folder/prj.git
#git remote show deploy
git fetch --unshallow deploy
git branch -M master
git push -u deploy master:refs/heads/master



#git push -u deploy HEAD:refs/heads/master
#git push --quiet --set-upstream deploy HEAD:master
#git push --set-upstream deploy main
