#!/bin/bash

#git config --global push.default matching
git remote add deploy ssh://momo@104.41.159.59:bar-repository-folder/project.git
#git push deploy --all
git remote show deploy
git push deploy --all