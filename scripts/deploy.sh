#!/bin/bash

git config --global push.default matching
git remote add deploy ssh://momo@$IP/$DEPLOY_DIR.git
git push deploy
