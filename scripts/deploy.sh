#!/bin/bash

git remote
git config --global push.default matching
git remote add deploy ssh://momo@104.41.159.59/srv/git/myapp.git/
git remote show deploy
#git push deploy
