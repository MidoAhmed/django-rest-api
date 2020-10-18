#!/bin/bash

#git config --global push.default matching
git remote add deploy ssh://git@104.41.159.59/home/momo/project.git
#git push deploy --all
git remote show deploy