#!/bin/bash

git config --global push.default matching
git remote add deploy ssh://momo@$HOST/$DEPLOY_DIR
git remote show deploy
git remote show origin
#git push deploy master --force
git push deploy HEAD:refs/heads/master
