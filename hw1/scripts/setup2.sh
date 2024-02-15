#!/bin/bash
source "$HOME/.bashrc"

# Set up vars
CONDA_ENV_NAME="jupyter"
PYTHON_VERSION="3.9"
SCREEN_NAME=$CONDA_ENV_NAME
PORT_NUMBER="5910"

# Create environments for jupyter notebook and for pytorch
conda create --name $CONDA_ENV_NAME python=$PYTHON_VERSION -y
conda activate $CONDA_ENV_NAME

# Install jupyter nb and pytorch
conda install -c conda-forge notebook -y
conda install -c conda-forge nb_conda_kernels -y
conda install nb_conda -y
conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 cpuonly -c pytorch -y

# Handle problematic python package issues
pip uninstall traitlets -y
pip install traitlets==5.9.0 -y

# Open new screen instance and initialize server
screen -S $SCREEN_NAME
conda activate $CONDA_ENV_NAME
jupyter notebook --no-browser --port=$PORT_NUMBER | grep http://localhost: >> ./serverinfo.txt&