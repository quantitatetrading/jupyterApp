ARG BASE_CONTAINER=jupyter/tensorflow-notebook
FROM $BASE_CONTAINER

USER root

RUN pip install -q jupyter_contrib_nbextensions && jupyter contrib nbextensions install --InstallContribNbextensionsApp.log_level=0
ADD jupyterExtension /usr/local/share/jupyter/nbextensions/jupyterExtension
RUN python /usr/local/share/jupyter/nbextensions/jupyterExtension/setup.py
