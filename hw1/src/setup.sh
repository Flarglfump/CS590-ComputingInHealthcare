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



# Below this line is code that must be run manually
# source "$HOME/.bashrc"

# Create environments for jupyter notebook and for pytorch
# conda create --name jupyter python=3.9 -y
# conda activate jupyter
# mkdir jupyter

# conda install -c conda-forge notebook -y
# conda install -c conda-forge nb_conda_kernels -y
# conda install nb_conda -y
# conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 cpuonly -c pytorch

# screen -S jupyter

# file:///users/gwitske/.local/share/jupyter/runtime/jpserver-15370-open.html
# http://localhost:5910/tree?token=7c26565964a4007e5ba2eda985ceb43dd13114d35f60714c
# http://127.0.0.1:5910/tree?token=7c26565964a4007e5ba2eda985ceb43dd13114d35f60714c
# ssh -L 59000:localhost:5910 gwitske@pc417.emulab.net
