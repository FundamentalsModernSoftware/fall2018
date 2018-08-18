#!/bin/bash

echo "Starting"
DST_FOLDER="samples"
REPO="https://github.com/FundamentalsModernSoftware/fall2018.git"
BRANCH="master"

GIT=$(type -p git)
ROOT="/home/codio/workspace"
DIR="$ROOT"

echo "checking out ${REPO} to directory $DIR"
if cd $DIR; then
  $GIT checkout -f; git checkout master; git pull;
else
  $GIT clone -b ${BRANCH} --single-branch $REPO $DIR
fi