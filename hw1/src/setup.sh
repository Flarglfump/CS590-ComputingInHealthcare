#!/bin/bash

# Set up vars
MINICONDA_DIR="$HOME/miniconda3"
CONDA_EXE="$MINICONDA_DIR/bin/conda"
# CONDA_ENV_NAME="gwitske_env"

# Update environment, install htop and screen
sudo apt-get update
sudo apt-get install -y htop screen

# Setup miniconda
mkdir -p $MINICONDA_DIR
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O $MINICONDA_DIR/miniconda.sh
bash $MINICONDA_DIR/miniconda.sh -b -u -p $MINICONDA_DIR
rm -rf $MINICONDA_DIR/miniconda.sh
$CONDA_EXE init bash


# Below this line is experimental code which does not work
# source "$HOME/.bashrc"
# if test ! -f $CONDA_EXE; then
#   echo "Could not find conda executable"
#   exit
# else
#   echo "Initializing conda bash environment..."
#   $CONDA_EXE init bash
# fi

# echo "Env Name: "$CONDA_ENV_NAME
# # Create/activate conda environment
# if $CONDA_EXE env list | grep -q $CONDA_ENV_NAME;
# then
#   echo "Environment $CONDA_ENV_NAME exists"
# else
#   echo "Environment $CONDA_ENV_NAME will be created..."
#   $CONDA_EXE create --name $CONDA_ENV_NAME python=3.11 -y
# fi

# $CONDA_EXE init bash
# $CONDA_EXE activate $CONDA_ENV_NAME