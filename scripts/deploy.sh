#!/bin/bash

git remote add production ssh://momo@104.41.159.59:22/home/momo/bar-repository-folder/project.git/
#git fetch --unshallow deploy
git add .
git commit -m "Ready for production"
git push production master

#git push -u deploy HEAD:refs/heads/master
#git push --quiet --set-upstream deploy HEAD:master
#git push --set-upstream deploy main
