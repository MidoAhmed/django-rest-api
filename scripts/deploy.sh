#!/bin/bash

#git config --global push.default matching
git remote add deploy ssh://momo@104.41.159.59/srv/git/myapp.git
git remote show deploy
git remote show origin
git push deploy --all
