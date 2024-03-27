#/usr/bin/bash

sudo apt update
sudo apt upgrade
sudo apt install gzip -y
sudo apt install bedtools -y

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/miniconda 
rm ~/miniconda.sh

which conda || echo "PATH=\$PATH:\$HOME/miniconda/bin" >> .bash_profile
which conda || echo "PATH=\$PATH:\$HOME/miniconda/bin" >> .bash_rc