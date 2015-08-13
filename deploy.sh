#!/bin/bash

pyenv activate website

# saving to not loose any changes (better to do it before)
git add .
git commit -m "deploying"
git push origin master

## buidling
./build.py --clean

git branch -D gh-pages
git checkout --orphan gh-pages

./build.py --full

if [ -d ./bin ]; then
  mv bin .tmp
  mv build.log .build.log

  rm -rf *
  rm .gitignore

  mv .tmp/* .
  rm -r .tmp
  mv .build.log build.log
  ##
  git add .
  git commit -m "build"

  git push origin --delete gh-pages

  git push origin gh-pages

else

  echo ""
  echo "###"
  echo "Could not build, coming back on master."
  echo "###"
  echo ""

fi

##
git checkout master
