# Docker sample

Three basic docker files to deploy applicaitons in Python without installing 
any dependencies locally.

```dockerSample/jupyter_dev```

Contains the dockerfile for a jupyter notebook and pre-install some basic 
Python libraries in order to test Python scripts. Everything is built and run inside 
the Docker container.


```dockerSample/vscode_dev```

Contains the dockerfile for a vscode dev environment and pre-install some basic 
Python libraries in order to test Python scripts. Everything is built and run inside 
the Docker container.

```dockerSample/python_dev```

Contains the dockerfile for a python deployment along with dependencies installation.
