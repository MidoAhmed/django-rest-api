#!/bin/bash

#git config --global push.default matching
git remote add deploy ssh://$USER@$HOST/$DEPLOY_DIR
git remote show deploy
#git push deploy main:master
git push deploy master
