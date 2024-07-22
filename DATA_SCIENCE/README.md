# Getting Started 

Add the followings to your .zshrc / .bash_profile

alias jupyter='docker run --rm -p 8888:8888 -v $(PWD):/opt/notebooks continuumio/anaconda3 /bin/bash -c "/opt/conda/bin/jupyter notebook --ip=0.0.0.0 --port=8888 --notebook-dir=/opt/notebooks --allow-root --no-browser --NotebookApp.token="'

alias jupyterlab='docker run --rm -p 8888:8888 -v $(PWD):/opt/notebooks continuumio/anaconda3 /bin/bash -c "/opt/conda/bin/jupyter lab --ip=0.0.0.0 --port=8888 --notebook-dir=/opt/notebooks --allow-root --no-browser --NotebookApp.token="'

[How to Run Python 3 and Jupyter Lab using an Anaconda Docker Container and VS Code](https://www.youtube.com/watch?v=cK7vgjOntqM)
