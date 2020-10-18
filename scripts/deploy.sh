#!/bin/bash

git config --global push.default matching
git remote add deploy ssh://$(USER)@$(HOST)/$(srv/git/myapp.git)
git remote show deploy
git remote show origin
git push deploy HEAD:master --force
