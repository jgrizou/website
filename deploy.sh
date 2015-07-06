#!/bin/bash

git add .
git commit -m "deploying"
git push origin master

##
./build.py --clean

git branch -D gh-pages
git checkout --orphan gh-pages

./build.py --full
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

##
git checkout master
