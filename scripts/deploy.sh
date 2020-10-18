#!/bin/bash

#git config --global push.default matching
git remote add deploy ssh://$USER@$HOST:$DEPLOY_DIR
#git push deploy --all
git remote show deploy