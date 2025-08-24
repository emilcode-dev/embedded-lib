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
    cmake \
    doxygen \
    graphviz \
    locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

# Set locale environment variables
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install needed python packages
RUN pip3 install conan sphinx_rtd_theme breathe --break-system-packages