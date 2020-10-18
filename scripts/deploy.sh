#!/bin/bash

git config --global push.default matching
git remote add deploy ssh://$USER@$HOST/$DEPLOY_DIR
#git remote show deploy
git branch -r
git fetch --unshallow deploy
git push deploy HEAD:refs/heads/master