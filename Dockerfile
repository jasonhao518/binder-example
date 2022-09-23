# Note that there must be a tag
FROM ubuntu:bionic
RUN sudo apt install python3.8 ca-certificates curl gnupg lsb-release
RUN sudo mkdir -p /etc/apt/keyrings
RUN sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
