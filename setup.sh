#!/usr/bin/env sh
# This is for Github Codespaces set and is a subset of what would normally be installed on a mac

set -e

export BOOTSTRAP_DEV_DIR=~/code
mkdir -p $BOOTSTRAP_DEV_DIR

export BOOTSTRAP_BIN_DIR=~/bin
mkdir -p $BOOTSTRAP_BIN_DIR

# Get directory of this script
export BOOTSTRAP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export BOOTSTRAP_SCRIPT_DIR=$BOOTSTRAP_DIR/script

./script/install-dotfiles
