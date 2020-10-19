#!/bin/bash

git remote add deploy ssh://momo@104.41.159.59/home/momo/bar-repository-folder/project.git
#git fetch --unshallow deploy
git push -u deploy HEAD:refs/heads/main



#git push -u deploy HEAD:refs/heads/master
#git push --quiet --set-upstream deploy HEAD:master
#git push --set-upstream deploy main
