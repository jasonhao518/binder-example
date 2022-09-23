# Note that there must be a tag
FROM ubuntu:bionic
RUN  apt update && apt --assume-yes  install ca-certificates curl gnupg lsb-release
RUN  mkdir -p /etc/apt/keyrings
RUN  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
