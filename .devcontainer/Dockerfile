# Use Ubuntu 24.04 LTS as the base image
FROM ubuntu:24.04
LABEL maintainer="emilcode-dev"

# Update the package list and install dev tools
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    git \
    build-essential \
    gdb \
    cmake

# Install python packages
RUN pip3 install numpy --break-system-packages