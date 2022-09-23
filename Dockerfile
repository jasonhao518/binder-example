# Note that there must be a tag
FROM python:3.10.7-alpine3.16
RUN apk add build-base linux-headers
RUN python3 -m pip install --no-cache-dir notebook jupyterlab
RUN pip install --no-cache-dir jupyterhub

USER root

RUN apk add docker
